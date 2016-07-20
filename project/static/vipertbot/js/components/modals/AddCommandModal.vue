<template>
    <modal modal-id="AddCommandModal">
        <div slot="title">New Custom Command</div>
        <div slot="body">

            <div class="panel panel-default">
                <div class="panel-body">
                    <form>
                        <legend>
                            Adding New Command {{ formModel.name }}
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
                                    <strong>Note:</strong> Click the box to reveal available roles.
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
                                    <button @click.prevent="cancelAdd()" class="btn btn-default">
                                        Cancel
                                    </button>
                                    <button @click.prevent="addNew()" class="btn btn-primary">
                                        <i class="fa fa-save"></i>
                                        Save
                                    </button>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </modal>
</template>

<script type="text/babel">
    import Modal from './Modal.vue'
    import Multiselect from 'vue-multiselect'

    import {
        AlertSuccess,
        AlertError
    } from '../../modules/alerts'

    import { getCommands } from '../../vuex/getters'
    import { toggleCommandActive, addCommand } from '../../vuex/actions'

    export default {
        vuex: {
            actions: {
                toggleCommandActive,
                addCommand
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
                    name: '',
                    text: '',
                    cooldown_min: 0,
                    roles: [],
                    active: true
                }
            }
        },
        components: {
            Modal,
            Multiselect
        },
        methods: {
            clearFields: function() {
                this.$broadcast('CloseModal')
                this.formModel.name = ''
                this.formModel.text = ''
                this.formModel.cooldown_min = 0
                this.formModel.roles = []
                this.formModel.active = true
            },
            cancelAdd: function () {
                this.clearFields()
            },
            addNew: function () {
                this.$http.post(window.location.origin + '/api/commands/create/', this.formModel).then(function (response) {
                    this.addCommand(response.data)
                    AlertSuccess("Command Created!")
                    this.clearFields()
                }.bind(this)).catch(function (response) {
                    AlertError(response.data.error, response.statusText, response.status)
                });
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