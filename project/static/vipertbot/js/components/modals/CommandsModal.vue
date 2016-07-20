<template>
    <modal modal-id="CommandsModal">
        <div slot="title">Custom Commands</div>
        <div slot="body">

            <!-- EDITING SHOW EDIT FORM -->
            <div v-if="Editing" :transition="editTransition" transition-mode="out-in" class="panel panel-default">
                <div class="panel-body">
                    <form>
                        <legend>
                            Editing {{ formModel.name }} with id: {{ formModel.id }}
                        </legend>

                        <fieldset>
                            <div class="form-group">
                                <label class="label">Command Trigger</label>
                                <input @keydown.enter.prevent="updateEdit()" type="text" class="form-control" v-model="formModel.name">

                                <div class="note text-danger">
                                    <strong>Note:</strong> Must start with ! example: !gamertag
                                </div>
                            </div>

                            <div class="form-group">
                                <label class="label">Command Output Text</label>
                                <textarea @keydown.enter.prevent="updateEdit()" rows="4" class="form-control" v-model="formModel.text"></textarea>

                                <div class="note">
                                    <strong>Tip:</strong> Check out the <a href="#">Public Variables</a>.
                                </div>
                            </div>

                            <div class="form-group">
                                <label>Roles</label>

                                <multiselect class="my-multiselect" :selected.sync="formModel.roles"
                                             :options="allRoles"
                                             multiple="multiple"
                                             :close-on-select="true"
                                             :hide-selected="true"
                                             :allow-empty="false"
                                             label="name"
                                             key="id"
                                ></multiselect>

                                <div class="note">
                                    <strong>Note:</strong> Click the box to reveal available roles.
                                </div>
                            </div>

                            <div class="form-group">
                                <label class="label">Cooldown In Minutes</label>
                                <input @keydown.enter.prevent="updateEdit()" type="number" min="0" class="form-control" v-model="formModel.cooldown_min">

                                <div class="note text-danger">
                                    <strong>Note:</strong> 0 is disabled
                                </div>
                            </div>
                        </fieldset>

                        <div class="form-actions">
                            <div class="row">
                                <div class="col-md-12">
                                    <button @click.prevent="cancelEdit()" class="btn btn-default">
                                        Cancel
                                    </button>
                                    <button id="SaveCommandEdit" @click.prevent="updateEdit()" class="btn btn-primary">
                                        <i class="fa fa-save"></i>
                                        Save
                                    </button>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>

            <!-- NOT EDITING SHOW TABLE DATA -->
            <table v-else class="table table-striped table-bordered table-hover">
                <thead>
                <tr>
                    <th>#</th>
                    <th>Command</th>
                    <th>Text</th>
                    <th></th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="item in commands">
                    <td>{{ item.id }}</td>
                    <td class="vcenter">{{ item.name }}</td>
                    <td>{{ item.text }}</td>
                    <td style="padding-right: 20px">
                        <form class="smart-form">
                            <label class="toggle pull-left">
                                <input @click="updateActive(item)" type="checkbox" name="checkbox-toggle"
                                       checked="{{ item.active }}">
                                <i data-swchon-text="ON" data-swchoff-text="OFF"></i>
                            </label>
                        </form>
                    </td>
                    <td width="105px" class="vcenter">
                        <div class="btn-group">
                            <button id="EditCommand{{ item.id }}" @click="Edit(item)" class="btn btn-default btn-sm">
                                <i class="fa fa-pencil"></i>
                            </button>
                            <button @click="removeCommand(item.id)" class="btn btn-danger btn-sm">
                                <i class="fa fa-trash"></i>
                            </button>
                        </div>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
    </modal>
</template>

<script type="text/babel">
    import Vue from 'vue'
    import Modal from './Modal.vue'
    import Multiselect from 'vue-multiselect'

    import {
            AlertSuccess,
            AlertError
    } from '../../modules/alerts'

    import { getCommands } from '../../vuex/getters'

    import {
            toggleCommandActive,
            updateCommand,
            deleteCommand
    } from '../../vuex/actions'

    Vue.transition('fade', {
        css: false,
        enter: function (el, done) {
            // element is already inserted into the DOM
            // call done when animation finishes.
            $(el)
                    .css('opacity', 0)
                    .animate({opacity: 1}, 500, done)
        },
        enterCancelled: function (el) {
            $(el).stop()
        },
        leave: function (el, done) {
            // same as enter
            $(el).animate({opacity: 0}, 500, done)
        },
        leaveCancelled: function (el) {
            $(el).stop()
        }
    });

    export default {
        vuex: {
            actions: {
                toggleCommandActive,
                updateCommand,
                deleteCommand
            },
            getters: {
                commands: getCommands
            }
        },
        data: function () {
            return {
                Editing: false,
                editTransition: 'fade',
                allRoles: [],

                formModel: {
                    id: null,
                    name: null,
                    text: null,
                    cooldown_min: null,
                    roles: null,
                    active: null
                }
            }
        },
        components: {
            Modal,
            Multiselect
        },
        methods: {
            clearFields: function () {
                this.Editing = false

                for (var item in this.formModel) {
                    this.formModel[item] = null
                }
            },
            Edit: function (item) {
                this.Editing = true
                this.formModel.id = item.id
                this.formModel.name = item.name
                this.formModel.text = item.text
                this.formModel.cooldown_min = item.cooldown_min
                this.formModel.roles = item.roles
                this.formModel.active = item.active
            },
            cancelEdit: function () {
                this.clearFields()
            },
            updateEdit: function () {
                this.$http.put(window.location.origin + '/api/commands/' + this.formModel.id + '/edit/', this.formModel).then(function (response) {
                    this.updateCommand(response.data)

                    AlertSuccess("Command has been updated!")

                    this.clearFields()
                }.bind(this)).catch(function (response) {
                    AlertError(response.data.error, response.statusText, response.status)
                });
            },
            updateActive: function (item) {
                this.$http.patch(window.location.origin + '/api/commands/' + item.id + '/edit/', {
                    active: !item.active,
                }).then(function (response) {
                    this.toggleCommandActive(item.id, item.active)
                    AlertSuccess("Command has been updated!")
                }.bind(this)).catch(function (response) {
                    AlertError(response.data.error, response.statusText, response.status)
                });
            },
            removeCommand: function (id) {
                $.SmartMessageBox({
                    title: "Warning!",
                    content: "Are you sure you want to delete this Command?",
                    buttons: '[No][Yes]'
                }, function (ButtonPressed) {
                    if (ButtonPressed === "Yes") {
                        this.$http.delete(window.location.origin + '/api/commands/' + id + '/delete/').then(function (response) {
                            this.deleteCommand(id)
                            AlertSuccess("Command has been removed!")
                        }.bind(this)).catch(function (response) {
                            AlertError(response.data.error, response.statusText, response.status)
                        });
                    }
                }.bind(this));
            },
            getAllRoles: function () {
                this.$http.get(window.location.origin + '/api/roles/').then(function (response) {
                    this.allRoles = response.data.results;
                }).catch(function (response) {
                    AlertError(response.data.error, response.statusText, response.status)
                });
            },
        },
        events: {
            'ModalClosing': function () {
                this.clearFields()
            }
        },
        ready: function () {
            this.getAllRoles()
        }
    }
</script>

<style>

</style>