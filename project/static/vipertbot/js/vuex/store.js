import Vue from 'vue'
import Vuex from 'vuex'

import regulars from './modules/regulars'
import commands from './modules/commands'

// Make vue aware of Vuex
Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        regulars,
        commands
    }
})