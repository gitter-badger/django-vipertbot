<template>
    <widget wid-id="61737" fullscreen="true">
        <div slot="title">Commands</div>
        <div slot="icon">
            <!-- add a icon example: <i class="fa fa-comments txt-color-white"></i> -->
            <i class="fa fa-table"></i>
        </div>

        <div slot="toolbars">
            <div class="widget-toolbar">
                <!-- add: non-hidden - to disable auto hide -->
                <div class="btn-group">
                    <button class="btn btn-xs bg-color-blue"
                            data-toggle="modal"
                            data-target="#CommandsModal"
                    >
                        <i class="fa fa-pencil"></i>
                    </button>
                    <button class="btn btn-xs bg-color-greenLight"
                            data-toggle="modal"
                            data-target="#AddCommandModal"
                    >
                        <i class="fa fa-plus"></i>
                    </button>
                </div>
            </div>
        </div>

        <div slot="body">
            <!-- MAIN CONTAINER -->
            <div class="alert alert-info no-margin fade in">
                <button class="close" data-dismiss="alert">
                    ×
                </button>
                <i class="fa-fw fa fa-info"></i>
                Commands Widget v1.0 Beta
            </div>

            <!-- Body Toolbars -->
            <div class="widget-body-toolbar">

                <div class="row">

                    <div class="col-xs-9 col-sm-5 col-md-5 col-lg-5">
                        <div class="input-group">
                            <span class="input-group-addon"><i class="fa fa-search"></i></span>
                            <input class="form-control"
                                   v-model="searchFilter"
                                   placeholder="Filter"
                                   type="text"
                            >
                        </div>
                    </div>
                </div>
            </div>

            <div class="custom-scroll table-responsive" style="height:200px; overflow-y: scroll;">

                <table class="table">
                    <thead>
                    <tr>
                        <th>#</th>
                        <th>Name</th>
                        <th>Cooldown Min</th>
                        <th>Active</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="item in commands | filterBy searchFilter in 'name'">
                        <td>{{ item.id }}</td>
                        <td>{{ item.name }}</td>
                        <td>{{ item.cooldown_min }}</td>
                        <td>
                            <form class="smart-form">
                                <label class="toggle pull-left">
                                    <input @click="Update(item)" type="checkbox" name="checkbox-toggle"
                                           checked="{{ item.active }}">
                                    <i data-swchon-text="ON" data-swchoff-text="OFF"></i>
                                </label>
                            </form>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>

        </div>
        <!-- end body -->
    </widget>
</template>
<style>

</style>
<script type="text/babel">
    import Widget from './Widget.vue'
    import { getCommands } from '../../vuex/getters'
    import { toggleCommandActive } from '../../vuex/actions'

    export default{
        vuex: {
            actions: {
                toggleCommandActive
            },
            getters: {
                commands: getCommands
            }
        },
        data: function () {
            return {
                searchFilter: ''
            }
        },
        components: {
            Widget
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
        computed: {},

        ready: function () {

        }
    }
</script>
