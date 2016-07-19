<template>
    <modal modal-id="CommandsModal">
        <div slot="title">Custom Commands</div>
        <div slot="body">

            <!-- EDITING SHOW EDIT FORM -->
            <div v-if="Editing" class="panel panel-default">
                <div class="panel-body">
                    <form>
                        <legend>
                            Editing {{ formModel.name }} with id: {{ formModel.id }}
                        </legend>

                        <fieldset>
                            <div class="form-group">
                                <label class="label">Command Trigger</label>
                                <input type="text" class="form-control" v-model="formModel.name">

                                <div class="note text-danger">
                                    <strong>Note:</strong> Must start with ! example: !gamertag
                                </div>
                            </div>

                            <div class="form-group">
                                <label class="label">Command Output Text</label>
                                <textarea rows="4" class="form-control" v-model="formModel.text"></textarea>

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
                                    <strong>Usage:</strong> &lt;select multiple style="width:100%" class="select2" &gt;...&lt;/select&gt;
                                </div>
                            </div>

                            <div class="form-group">
                                <label class="label">Cooldown In Minutes</label>
                                <input type="number" min="0" class="form-control" v-model="formModel.cooldown_min">

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
                                    <button @click.prevent="updateEdit()" class="btn btn-primary">
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
                    <th>Command</th>
                    <th>Text</th>
                    <th></th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                <tr v-for="item in commands">
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
                            <button @click="Edit(item)" class="btn btn-default btn-sm">
                                <i class="fa fa-pencil"></i>
                            </button>
                            <button class="btn btn-danger btn-sm">
                                <i class="fa fa-trash"></i>
                            </button>
                        </div>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
        <div slot="footer">

        </div>
    </modal>
</template>

<script type="text/babel">
    import Modal from './Modal.vue'
    import Multiselect from 'vue-multiselect'
    import { getCommands } from '../../vuex/getters'
    import { toggleCommandActive, updateCommand } from '../../vuex/actions'

    export default {
        vuex: {
            actions: {
                toggleCommandActive,
                updateCommand
            },
            getters: {
                commands: getCommands
            }
        },
        data: function () {
            return {
                Editing: false,
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
                //for (var item in this.formModel) {
                //    this.formModel[item] = null
                //}
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
                    // todo: add update to vuex store
                    this.updateCommand(this.formModel)

                    $.smallBox({
                        title: "Command Successfully Updated",
                        content: "",
                        color: "#739E73",
                        iconSmall: "fa fa-thumbs-up bounce animated",
                        timeout: 4000
                    });

                    this.clearFields()
                }.bind(this)).catch(function (response) {
                    $.bigBox({
                        title: "Critical Error",
                        content: response,
                        color: "#C46A69",
                        icon: "fa fa-warning shake animated",
                        //number : "",
                        timeout: 6000
                    });
                });
            },
            updateActive: function (item) {
                this.$http.patch(window.location.origin + '/api/commands/' + item.id + '/edit/', {
                    active: !item.active,
                }).then(function (response) {
                    this.toggleCommandActive(item.id, item.active)

                    $.smallBox({
                        title: "Command Successfully Updated",
                        content: "",
                        color: "#739E73",
                        iconSmall: "fa fa-thumbs-up bounce animated",
                        timeout: 4000
                    });
                }.bind(this)).catch(function (response) {
                    $.bigBox({
                        title: "Critical Error",
                        content: response.data,
                        color: "#C46A69",
                        icon: "fa fa-warning shake animated",
                        //number : "",
                        timeout: 6000
                    });
                });
            },
            getAllRoles: function () {
                this.$http.get(window.location.origin + '/api/roles/').then(function (response) {
                    this.allRoles = response.data.results;
                }).catch(function (response) {
                    $.bigBox({
                        title: "Critical Error:",
                        content: response.data,
                        color: "#C46A69",
                        icon: "fa fa-warning shake animated",
                        //number : "",
                        timeout: 6000
                    });
                });
            },
        },
        events: {
            'ModalClosing': function() {
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