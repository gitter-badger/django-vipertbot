<template>
    <div class="panel-body">
        <div class="row">
            <div class="col-md-4">
                <a :href="twitchLink"
                   class="thumbnail" target="_blank">

                    <img class="img-responsive img-thumbnail"
                         :src="logo"
                         width="110" height="110">
                </a>
                <div class="text-center">
                    <div v-if="isFollowing">
                        <button @click="stopFollowing()" type="button" class="btn btn-primary btn-sm">
                            <i class="fa fa-twitch"></i> Stop Following
                        </button>
                    </div>
                    <div v-else>
                        <button @click="followChannel()" type="button" class="btn btn-primary btn-sm">
                            <i class="fa fa-twitch"></i> Follow
                        </button>
                    </div>
                </div>
            </div>
            <div class="col-md-8">
                <div class="h3 page-header">{{ item.user.display_name }}</div>
                <p>
                    {{ item.user.bio }}
                </p>
            </div>
        </div>
    </div>
</template>
<script>
    export default {
        data: function() {
            return {
                isFollowing: false
            }
        },

        methods: {
            getFollowing: function() {
                this.$http.get(window.location.origin + '/api/followers/following/'+this.item.user.name+'/').then(function(response) {
                    this.isFollowing = true;
                }).catch(function(response) {
                    this.isFollowing = false
                });
            },
            followChannel: function() {
                this.$http.get(window.location.origin + '/api/followers/follow/'+this.item.user.name+'/').then(function(response) {
                    this.isFollowing = true;
                }).catch(function(response) {
                    this.isFollowing = false
                });
            },
            stopFollowing: function() {
                this.$http.get(window.location.origin + '/api/followers/unfollow/'+this.item.user.name+'/').then(function(response) {
                    this.isFollowing = false;
                }).catch(function(response) {
                    this.isFollowing = true
                });
            }
        },

        computed: {
            twitchLink: function() {
                return 'http://www.twitch.tv/'+this.item.user.name;
            },
            logo: function() {
                if(this.item.user.logo == null) {
                    return "http://s.jtvnw.net/jtv_user_pictures/hosted_images/GlitchIcon_purple.png"
                }

                return this.item.user.logo
            }
        },

        props: [
            'item'
        ],

        ready: function() {
            //console.log('Item: ' + this.item.user.display_name);
            this.getFollowing();
        }
    }
</script>