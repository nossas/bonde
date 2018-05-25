import { combineReducers } from 'redux'
// Import used reducers
import { reducer as formReducer } from 'redux-form'
import { reducer as authReducer } from '../auth/redux'
import { reducer as headerReducer } from '../../components/Header/redux'
import { reducer as tourReducer } from '../../components/Tourtip'

export default combineReducers({
  // insert your reducers function
  auth: authReducer,
  form: formReducer,
  header: headerReducer,
  tour: tourReducer
})
