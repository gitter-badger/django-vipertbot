<template>
    <div class="row">
        <div class="col-xs-12 col-sm-7 col-md-7 col-lg-8">
            <h1 class="page-title txt-color-blueDark"><i class="fa-fw fa fa-home"></i> Dashboard
                <span>> My Dashboard</span></h1>
        </div>
        <div class="col-xs-12 col-sm-5 col-md-5 col-lg-4">
            <bot-controls></bot-controls>
        </div>
    </div>

    <!-- widget grid -->
    <section id="widget-grid" class="">
        <div class="row">
            <!-- LEFT COLUMN -->
            <article class="col-sm-12 col-md-12 col-lg-6">
                <commands></commands>
                <regulars></regulars>
                <smart-chat></smart-chat>
            </article>

            <!-- RIGHT COLUMN-->
            <article class="col-sm-12 col-md-12 col-lg-6">
                <twitch-chat></twitch-chat>
                <chart></chart>
            </article>
        </div>

        <!-- end row -->
    </section>
    <!-- end widget grid -->

    <!-- Modals Here -->
    <commands-modal></commands-modal>
    <add-command-modal></add-command-modal>
    <add-regular-modal></add-regular-modal>
    <!-- End Modals -->
</template>

<script type="text/babel">
    // Widgets
    import BotControls from '../widgets/BotControls.vue'
    import Chart from '../widgets/ChartWidget.vue'
    import Commands from '../widgets/CommandsWidget.vue'
    import Regulars from '../widgets/RegularsWidget.vue'
    import SmartChat from '../widgets/SmartChat.vue'
    import TwitchChat from '../widgets/TwitchChat.vue'

    // Modals
    import CommandsModal from '../modals/CommandsModal.vue'
    import AddCommandModal from '../modals/AddCommandModal.vue'
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
        components: {
            BotControls,
            Chart,
            Commands,
            Regulars,
            SmartChat,
            TwitchChat,
            CommandsModal,
            AddCommandModal,
            AddRegularModal
        },

        computed: {},

        methods: {
            setRegularsStore: function () {
                this.$http.get(window.location.origin + '/api/regulars/').then(function (response) {
                    this.setRegulars(response.data.results);
                }.bind(this)).catch(function (response) {
                    $.bigBox({
                        title: "Critical Error",
                        content: response,
                        color: "#C46A69",
                        icon: "fa fa-warning shake animated",
                        //number : "",
                        timeout: 6000
                    });
                }.bind(this));
            },
            setCommandsStore: function () {
                this.$http.get(window.location.origin + '/api/commands/').then(function (response) {
                    this.setCommands(response.data.results);
                }.bind(this)).catch(function (response) {
                    $.bigBox({
                        title: "Critical Error",
                        content: response,
                        color: "#C46A69",
                        icon: "fa fa-warning shake animated",
                        //number : "",
                        timeout: 6000
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
