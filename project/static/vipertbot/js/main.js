var Vue = require('vue');

Vue.use(require('vue-resource'));

Vue.http.headers.common['X-CSRFToken'] = document.querySelector('#token').getAttribute('value');

var dashboard = require('./components/pages/Dashboard.vue')
var SiteSearch = require('./components/SiteSearch.vue')
var DevActivityDropdown = require('./components/DevActivityDropdown.vue')
var Breadcrumbs = require('./components/Breadcrumbs.vue')
var NotificationsDropdown = require('./components/NotificationsDropdown.vue')

new Vue({
    el: 'body',

    components: {
        dashboard,
        SiteSearch,
        DevActivityDropdown,
        Breadcrumbs,
        NotificationsDropdown

    },

    data: {
        currentView: 'dashboard',
        User: null
    },

    methods: {
        getUserObject: function() {
            this.$http.get(window.location.origin + '/api/users/'+USER_ID+'/')
                .then(function(response) {
                    this.User = response.data
                }.bind(this)).catch(function(response) {
                    alert(response)
                });
        }
    },

    ready() {
        this.getUserObject()
    }

});