<template xmlns:v-on="http://www.w3.org/1999/xhtml" xmlns:v-bind="http://www.w3.org/1999/xhtml">
    <!-- Modal -->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
        <div class="modal-dialog">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-hidden="true">
                        &times;
                    </button>
                    <h4 class="modal-title" id="myModalLabel">Article Post</h4>
                </div>
                <div class="modal-body">

                    <div class="row">
                        <div class="col-md-12">
                            <div class="form-group">
                                <input type="text" class="form-control" placeholder="Title" required />
                            </div>
                            <div class="form-group">
                                <textarea class="form-control" placeholder="Content" rows="5" required></textarea>
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-6">
                            <div class="form-group">
                                <label for="category"> Category</label>
                                <select class="form-control" id="category">
                                    <option>Articles</option>
                                    <option>Tutorials</option>
                                    <option>Freebies</option>
                                </select>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="form-group">
                                <label for="tags"> Tags</label>
                                <input type="text" class="form-control" id="tags" placeholder="Tags" />
                            </div>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-md-12">
                            <div class="well well-sm well-primary">
                                <form class="form form-inline " role="form">
                                    <div class="form-group">
                                        <input type="text" class="form-control" value="" placeholder="Date" required />
                                    </div>
                                    <div class="form-group">
                                        <select class="form-control">
                                            <option>Draft</option>
                                            <option>Published</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <button type="submit" class="btn btn-success btn-sm">
                                            <span class="glyphicon glyphicon-floppy-disk"></span> Save
                                        </button>
                                        <button type="button" class="btn btn-default btn-sm">
                                            <span class="glyphicon glyphicon-eye-open"></span> Preview
                                        </button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>

                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">
                        Cancel
                    </button>
                    <button type="button" class="btn btn-primary">
                        Post Article
                    </button>
                </div>
            </div><!-- /.modal-content -->
        </div><!-- /.modal-dialog -->
    </div><!-- /.modal -->

    <!--<div class="modal-mask" v-show="show" transition="modal">
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
                    <button class="btn btn-default btn-sm" @click="close()">
                        Close
                    </button>

                </div>
            </div>
        </div>
    </div>-->
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
                this.$http.get(window.location.origin + '/api/followers/').then(function(response) {
                    console.log(response);
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
            },
            close: function() {
                this.show = false;
                this.followers = []
            }
        }
    }
</script>

<style>

</style>