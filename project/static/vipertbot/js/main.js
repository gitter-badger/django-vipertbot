var Vue = require('vue');

Vue.use(require('vue-resource'));

Vue.http.headers.common['X-CSRFToken'] = document.querySelector('#token').getAttribute('value');

// vuex Store
import store from './vuex/store'

// components
import dashboard from './components/pages/Dashboard.vue'
import SiteSearch from './components/SiteSearch.vue'
import DevActivityDropdown from './components/DevActivityDropdown.vue'
import Breadcrumbs from './components/Breadcrumbs.vue'
import NotificationsDropdown from './components/NotificationsDropdown.vue'

new Vue({
    el: 'body',

    components: {
        dashboard,
        SiteSearch,
        DevActivityDropdown,
        Breadcrumbs,
        NotificationsDropdown
    },

    store,

    data: {
        currentView: 'dashboard',
    },

    methods: {

    },

    ready() {

    }

});