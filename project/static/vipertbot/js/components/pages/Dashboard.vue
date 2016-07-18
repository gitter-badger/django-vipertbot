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
                <twitch-chat></twitch-chat>
            </article>
        </div>

        <!-- end row -->

        <div class="row">
            <article class="col-sm-12 col-md-12 col-lg-6">
                <commands></commands>
            </article>

            <article class="col-sm-12 col-md-12 col-lg-6">
                <regulars></regulars>
            </article>
        </div>
    </section>
    <!-- end widget grid -->

    <!-- Modals Here -->
    <commands-modal></commands-modal>
    <add-regular-modal></add-regular-modal>
    <!-- End Modals -->
</template>

<script type="text/babel">
    // Widgets
    import Commands from '../widgets/CommandsWidget.vue'
    import Regulars from '../widgets/RegularsWidget.vue'
    import SmartChat from '../widgets/SmartChat.vue'
    import TwitchChat from '../widgets/TwitchChat.vue'

    // Modals
    import CommandsModal from '../modals/CommandsModal.vue'
    import AddRegularModal from '../modals/AddRegularModal.vue'

    // vuex
    import { setRegulars, setCommands } from '../../vuex/actions'

    export default {
        vuex: {
            actions: {
                setRegulars,
                setCommands
            }
        },
        components:{
            Commands,
            Regulars,
            SmartChat,
            TwitchChat,
            CommandsModal,
            AddRegularModal
        },

        computed: {

        },

        methods: {
            setRegularsStore: function() {
                this.$http.get(window.location.origin + '/api/regulars/').then(function(response) {
                    this.setRegulars(response.data.results);
                }.bind(this)).catch(function(response) {
                    $.bigBox({
                        title : "Critical Error",
                        content : response,
                        color : "#C46A69",
                        icon : "fa fa-warning shake animated",
                        //number : "",
                        timeout : 6000
                    });
                }.bind(this));
            },
            setCommandsStore: function() {
                this.$http.get(window.location.origin + '/api/commands/').then(function(response) {
                    this.setCommands(response.data.results);
                }.bind(this)).catch(function(response) {
                    $.bigBox({
                        title : "Critical Error",
                        content : response,
                        color : "#C46A69",
                        icon : "fa fa-warning shake animated",
                        //number : "",
                        timeout : 6000
                    });
                }.bind(this));
            },
        },
        ready: function () {
            this.setRegularsStore()
            this.setCommandsStore()
        }
    }
</script>
