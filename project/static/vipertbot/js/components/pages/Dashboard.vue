<template>
    <div class="row">
        <div class="col-xs-12 col-sm-7 col-md-7 col-lg-4">
            <h1 class="page-title txt-color-blueDark"><i class="fa-fw fa fa-home"></i> Dashboard <span>> My Dashboard</span></h1>
        </div>
    </div>

    <!-- widget grid -->
    <section id="widget-grid" class="">

        <!-- row -->
        <div class="row">

            <article class="col-sm-12 col-md-12 col-lg-6">
                <smart-chat></smart-chat>
            </article>

            <article class="col-sm-12 col-md-12 col-lg-6">

                <!-- new widget -->
                <div class="jarviswidget jarviswidget-color-blue" id="wid-id-0"
                     data-widget-editbutton="false"
                     data-widget-colorbutton="false"
                     data-widget-deletebutton="false"
                     data-widget-fullscreenbutton="false"
                >

                    <!-- widget options:
                    usage: <div class="jarviswidget" id="wid-id-0" data-widget-editbutton="false">

                    data-widget-colorbutton="false"
                    data-widget-editbutton="false"
                    data-widget-togglebutton="false"
                    data-widget-deletebutton="false"
                    data-widget-fullscreenbutton="false"
                    data-widget-custombutton="false"
                    data-widget-collapsed="true"
                    data-widget-sortable="false"

                    -->

                    <header>
                        <span class="widget-icon"> <i class="fa fa-check txt-color-white"></i> </span>
                        <h2> Twitch Chat </h2>
                        <!-- <div class="widget-toolbar">
                        add: non-hidden - to disable auto hide

                        </div>-->
                    </header>

                    <!-- widget div-->
                    <div>
                        <div class="widget-body no-padding smart-form">
                            <!-- content goes here -->

                            <div v-if="TwitchURL" class="panel panel-default">
                                <div class="panel-body text-center">
                                    <iframe frameborder="0"
                                            scrolling="no"
                                            id="chat_embed"
                                            :src="TwitchURL"
                                            height="410"
                                            width="100%">
                                    </iframe>
                                </div>
                            </div>

                            <!-- end content -->
                        </div>

                    </div>
                    <!-- end widget div -->
                </div>
                <!-- end widget -->

            </article>

            <article class="col-sm-12 col-md-12 col-lg-6">
                <commands></commands>
            </article>
        </div>

        <!-- end row -->

        <div class="row">

        </div>
    </section>
    <!-- end widget grid -->
</template>
<style>
    
</style>
<script>
    import Commands from '../widgets/CommandsWidget.vue'
    import SmartChat from '../widgets/SmartChat.vue'

    export default {
        props: ['user'],

        data: function() {
            return{

            }
        },
        components:{
            Commands,
            SmartChat
        },

        computed: {
            TwitchURL: function() {
                if(this.user != null) {
                    return 'http://www.twitch.tv/'+this.user.username+'/chat'
                }

                return null
            },
        },

        methods: {

        }
    }
</script>
