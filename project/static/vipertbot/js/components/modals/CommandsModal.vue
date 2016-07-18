<template>
    <modal modal-id="CommandsModal">
        <div slot="title">Custom Commands</div>
        <div slot="body">
            <div class="panel panel-default">
                <div class="panel-heading">
                    Editing
                </div>
                <div class="panel-body">
                    <form class="smart-form">
                        <label class="select select-multiple">
                            <select multiple="" class="custom-scroll">
                                <option value="1">Alexandra</option>
                                <option value="2">Alice</option>
                                <option value="3">Anastasia</option>
                                <option value="4">Avelina</option>
                                <option value="5">Basilia</option>
                                <option value="6">Beatrice</option>
                                <option value="7">Cassandra</option>
                                <option value="8">Clemencia</option>
                                <option value="9">Desiderata</option>
                            </select>
                        </label>
                    </form>
                </div>
                <div class="panel-footer pull-right">
                    <button class="btn btn-default">Cancel</button>
                    <button class="btn btn-primary">Save</button>
                </div>
            </div>
            <table class="table table-striped table-bordered table-hover">
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
                                <input @click="Update(item)" type="checkbox" name="checkbox-toggle"
                                       checked="{{ item.active }}">
                                <i data-swchon-text="ON" data-swchoff-text="OFF"></i>
                            </label>
                        </form>
                    </td>
                    <td width="105px" class="vcenter">
                        <div class="btn-group">
                            <button class="btn btn-default btn-xs">
                                Actions
                            </button>
                            <button class="btn btn-default btn-xs dropdown-toggle" data-toggle="dropdown"
                                    aria-expanded="false">
                                <span class="caret"></span>
                            </button>
                            <ul class="dropdown-menu">
                                <li>
                                    <a href="javascript:void(0);">Action</a>
                                </li>
                                <li>
                                    <a href="javascript:void(0);">Another action</a>
                                </li>
                                <li>
                                    <a href="javascript:void(0);">Something else here</a>
                                </li>
                                <li class="divider"></li>
                                <li>
                                    <a href="javascript:void(0);">Separated link</a>
                                </li>
                            </ul>
                        </div>
                    </td>
                </tr>
                </tbody>
            </table>
        </div>
        <div slot="footer"></div>
    </modal>
</template>

<script type="text/babel">
    import Modal from './Modal.vue'
    import { getCommands } from '../../vuex/getters'
    import { toggleCommandActive } from '../../vuex/actions'

    export default {
        vuex: {
            actions: {
                toggleCommandActive
            },
            getters: {
                commands: getCommands
            }
        },
        data: function () {
            return {}
        },
        components: {
            Modal
        },
        methods: {
            Update: function (item) {
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
                        content: response,
                        color: "#C46A69",
                        icon: "fa fa-warning shake animated",
                        //number : "",
                        timeout: 6000
                    });
                });
            }
        },
        ready: function () {

        }
    }
</script>

<style>

</style>