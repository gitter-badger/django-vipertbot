<template>
    <widget wid-id="37691" fullscreen="true">
        <div slot="title">Regulars</div>
        <div slot="icon">
            <!-- add a icon example: <i class="fa fa-comments txt-color-white"></i> -->
            <i class="fa fa-table"></i>
        </div>

        <div slot="toolbars">
            <div class="widget-toolbar">
                <!-- add: non-hidden - to disable auto hide -->
                <div class="btn-group">
                    <button class="btn btn-xs bg-color-greenLight"
                            data-toggle="modal"
                            data-target="#AddRegularModal"
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
                Regulars Widget v1.0 Beta
            </div>

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
                        <th></th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr v-for="item in regulars | filterBy searchFilter in 'name'">
                        <td>{{ item.id }}</td>
                        <td>{{ item.name }}</td>
                        <td>
                            <button @click="remove(item.id)" class="btn btn-danger btn-xs">
                                <i class="fa fa-trash"></i>
                            </button>
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

    import {
        AlertSuccess,
        AlertError
    } from '../../modules/alerts'

    import { getRegulars } from '../../vuex/getters'
    import { deleteRegular } from '../../vuex/actions'

    export default{
        vuex: {
            actions: {
                deleteRegular
            },
            getters: {
                regulars: getRegulars
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
            remove: function (id) {
                // todo: add messagebox funtion to modules/alerts.js
                $.SmartMessageBox({
                    title: "Warning!",
                    content: "Are you sure you want to delete this user from the Regulars list?",
                    buttons: '[No][Yes]'
                }, function (ButtonPressed) {
                    if (ButtonPressed === "Yes") {
                        this.$http.delete(window.location.origin + '/api/regulars/' + id + '/delete/').then(function (response) {
                            this.deleteRegular(id)
                            AlertSuccess("Regular removed!")
                        }.bind(this)).catch(function (response) {
                            AlertError(response.data.error, response.statusText, response.status)
                        });
                    }
                }.bind(this));
            },
        },
        computed: {},
        ready: function () {

        }
    }
</script>
