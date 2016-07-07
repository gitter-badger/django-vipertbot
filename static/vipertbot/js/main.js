var Vue = require('vue');

Vue.use(require('vue-resource'));

Vue.http.headers.common['X-CSRFToken'] = document.querySelector('#token').getAttribute('value');

var BotControls = require('./components/BotControls.vue');
var FeaturesModal = require('./components/FeaturesModal.vue');
var FollowersModal = require('./components/FollowersModal.vue');
var CommandsModal = require('./components/CommandsModal.vue');
var RegularsModal = require('./components/RegularsModal.vue');

new Vue({
    el: 'body',

    components: {
        BotControls,
        FeaturesModal,
        FollowersModal,
        CommandsModal,
        RegularsModal,
    },

    data: {
        showFeaturesModal: false,
        showFollowersModal: false,
        showCommandsModal: false,
        showRegularsModal: false
    },

    methods: {

    },

    ready() {
        //alert('Ready to go ...');
    }
})