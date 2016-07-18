import {
    SET_COMMANDS,
    ADD_COMMAND,
    UPDATE_COMMAND,
    DELETE_COMMAND,
    TOGGLE_COMMAND_ACTIVE
} from '../mutation-types'

// initial state
const state = {
    list: []
}

// mutations
const mutations = {
    [SET_COMMANDS] (state, data) {
        state.list = data
    },

    [ADD_COMMAND] (state, data) {
        state.list.push(data)
    },

    [UPDATE_COMMAND] (state, id, data) {
        for (var i in state.list) {
            if (state.list[i].id == id) {
                state.list.splice(i, 1, data);
                break
            }
        }
    },

    [DELETE_COMMAND] (state, id) {
        for (var i in state.list) {
            if (state.list[i].id == id) {
                state.list.splice(i, 1);
                break
            }
        }
    },

    [TOGGLE_COMMAND_ACTIVE] (state, id, active) {
        for (var i in state.list) {
            if (state.list[i].id == id) {
                state.list[i].active = !active;
                break
            }
        }
    },
}

export default {
    state,
    mutations
}