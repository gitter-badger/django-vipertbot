<template xmlns:v-on="http://www.w3.org/1999/xhtml" xmlns:v-bind="http://www.w3.org/1999/xhtml">
    <div class="modal-mask" v-show="show" transition="modal">
        <div class="modal-wrapper">
            <div class="modal-container">

                <div class="modal-header">
                    <i class="fa fa-twitch"></i> Followers

                    <button @click="refreshFollowers()" v-if="followers.length > 0" class="btn btn-primary btn-sm pull-right" type="button">
                        <div v-if="!isRefreshing">
                            <i class="fa fa-refresh"></i>
                        </div>
                    </button>

                </div>

                <div class="modal-body">
                    <div v-if="!isRefreshing">
                        <div class="text-center" v-if="followers.length <= 0">
                            <div class="h1 page-header">Followers Component v0.1.5 Beta</div>

                            <blockquote>
                                <p>You can load your followers and interact with them through this component!</p>
                                <footer>Limited to the most recent 100 followers</footer>
                            </blockquote>


                            <button class="btn btn-primary btn-lg" v-on:click="getFollowers()">
                                    Load Followers
                            </button>
                        </div>
                    </div>

                    <div>
                        <pulse-loader :loading="isLoading"></pulse-loader>
                        <pulse-loader :loading="isRefreshing"></pulse-loader>
                    </div>

                    <div class="panel panel-default" v-for="(index, item) in followers">
                        <follower :item="item"></follower>
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
    import Follower from './Follower.vue';
    import { PulseLoader } from 'vue-spinner/dist/vue-spinner.min.js'

    export default {
        components: {
            Follower,
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
                followers: []
            }
        },

        methods: {
            getFollowers: function() {
                this.isLoading = true;
                this.$http.get('api/twitch/followers/').then(function(response) {
                    console.log(response.data.follows);
                    this.followers = response.data.follows;
                    this.isLoading = false
                }.bind(this)).catch(function(response) {
                    this.isLoading = false
                }.bind(this));
            },
            refreshFollowers: function() {
                this.isRefreshing = true;
                this.followers = [];
                this.followers = this.getFollowers();
                this.isRefreshing = false;
            }
        }
    }
</script>

<style>

</style>