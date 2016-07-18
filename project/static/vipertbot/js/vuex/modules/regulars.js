import {
    SET_REGULARS,
    DELETE_REGULAR,
    ADD_REGULAR
} from '../mutation-types'

// initial state
const state = {
    list: []
}

// mutations
const mutations = {
    [SET_REGULARS] (state, data) {
        state.list = data
    },

    [ADD_REGULAR] (state, data) {
        state.list.push(data)
    },

    [DELETE_REGULAR] (state, id) {
        for (var i in state.list) {
            if (state.list[i].id == id) {
                state.list.splice(i, 1);
            }
        }
    }
}

export default {
    state,
    mutations
}