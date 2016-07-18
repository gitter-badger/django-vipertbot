// Regulars
export const setRegulars = makeAction('SET_REGULARS')
export const addRegular = makeAction('ADD_REGULAR')
export const deleteRegular = makeAction('DELETE_REGULAR')

// Commands
export const setCommands = makeAction('SET_COMMANDS')
export const addCommand = makeAction('ADD_COMMAND')
export const updateCommand = makeAction('UPDATE_COMMAND')
export const deleteCommand = makeAction('DELETE_COMMAND')
export const toggleCommandActive = makeAction('TOGGLE_COMMAND_ACTIVE')

function makeAction (type) {
  return ({ dispatch }, ...args) => dispatch(type, ...args)
}