<template xmlns:v-on="http://www.w3.org/1999/xhtml" xmlns:v-bind="http://www.w3.org/1999/xhtml">
    <div class="modal-mask" v-show="show" transition="modal">
        <div class="modal-wrapper">
            <div class="modal-container">

                <div class="modal-header">
                    <i class="fa fa-users"></i> Regulars

                    <button @click="refresh()" v-if="regulars.length > 0" class="btn btn-primary btn-sm pull-right" type="button">
                        <div v-if="!isRefreshing">
                            <i class="fa fa-refresh"></i>
                        </div>
                    </button>
                </div>
                <div class="modal-body">
                    <div v-if="!isRefreshing">
                        <div class="text-center" v-if="regulars.length <= 0">
                            <div class="h1 page-header">Regulars Component v0.1.2 Beta</div>

                            <blockquote>
                                <p>
                                    Use this Component to manage your regular users.
                                    These users may have special permissions
                                </p>
                                <footer>Loading could take some time.</footer>
                            </blockquote>

                            <button class="btn btn-primary btn-lg" v-on:click="getRegulars()">
                                Load Regulars
                            </button>
                        </div>
                    </div>

                    <div>
                        <pulse-loader :loading="isLoading"></pulse-loader>
                        <pulse-loader :loading="isRefreshing"></pulse-loader>
                    </div>

                    <div class="panel panel-default" v-for="(index, item) in regulars">
                        <regular :item="item"></regular>
                    </div>
                </div>

                <div class="modal-footer">
                    <button class="btn btn-default btn-sm" v-on:click="show = false">
                        Close
                    </button>

                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import Regular from './Regular.vue';
    import { PulseLoader } from 'vue-spinner/dist/vue-spinner.min.js'

    export default {
        components: {
            Regular,
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
                regulars: []
            }
        },

        methods: {
            getRegulars: function() {
                this.isLoading = true;
                this.$http.get('api/app/regulars/').then(function(response) {
                    this.regulars = response.data;
                    this.isLoading = false
                }.bind(this)).catch(function(response) {
                    this.isLoading = false
                }.bind(this));
            },
            refresh: function() {
                this.isRefreshing = true;
                this.regulars = [];
                this.regulars = this.getRegulars();
                this.isRefreshing = false;
            }
        },

        events: {
            'refreshRequested': function () {
                this.refresh();
            }
        }
    }
</script>

<style>

</style>