<template xmlns:v-on="http://www.w3.org/1999/xhtml" xmlns:v-bind="http://www.w3.org/1999/xhtml">
    <div class="modal-mask" v-show="show" transition="modal">
        <div class="modal-wrapper">
            <div class="modal-container">

                <div class="modal-header">
                    <i class="fa fa-exclamation"></i> Commands

                    <button @click="refreshCommands()" v-if="commands.length > 0"
                            class="btn btn-primary btn-sm pull-right"
                            type="button"
                    >
                        <div v-if="!isRefreshing">
                            <i class="fa fa-refresh"></i>
                        </div>
                    </button>
                </div>

                <div class="modal-body">
                    <div v-if="!isRefreshing">
                        <div class="text-center" v-if="commands.length <= 0">
                            <div class="h1 page-header">Commands Component v0.1.0 Beta</div>

                            <blockquote>
                                <p>You can load your custom commands and edit them through this component!</p>
                                <footer>Loading could take some time.</footer>
                            </blockquote>

                            <button class="btn btn-primary btn-lg" @click="getCommands()">
                                Load Commands
                            </button>
                        </div>
                    </div>

                    <div>
                        <pulse-loader :loading="isLoading"></pulse-loader>
                        <pulse-loader :loading="isRefreshing"></pulse-loader>
                    </div>

                    <div class="panel panel-default" v-for="(index, item) in commands">
                        <command :item="item"></command>
                    </div>
                </div>

                <div class="modal-footer">
                    <button class="btn btn-default btn-sm" @click="close()">
                        Close
                    </button>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Command from './Command.vue';
    import { PulseLoader } from 'vue-spinner/dist/vue-spinner.min.js'

    export default {
        components: {
            Command,
            PulseLoader
        },

        props: {
            show: {
                type: Boolean,
                required: true,
                twoWay: true
            }
        },

        data: function() {
            return {
                isLoading: false,
                isRefreshing: false,
                commands: []
            }
        },

        methods: {
            getCommands: function() {
                this.isLoading = true;
                this.$http.get(window.location.origin + '/api/commands/').then(function(response) {
                    //console.log(response.data.results);
                    this.commands = response.data.results;
                    this.isLoading = false
                }.bind(this)).catch(function(response) {
                    this.isLoading = false
                }.bind(this));
            },
            refreshCommands: function() {
                this.isRefreshing = true;
                this.commands = [];
                this.commands = this.getCommands();
                this.isRefreshing = false;
            },
            close: function() {
                this.commands = [];
                this.show = false
            }
        },

        events: {
//            'modalClosing': function () {
//                this.commands = [];
//            }
        }
    }
</script>

<style>

</style>