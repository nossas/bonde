// polyfill webpack require.ensure
if (typeof require.ensure !== 'function') require.ensure = (d, c) => c(require)
import { injectAsyncReducer } from '~client/store'

//
// @path (admin) /mobilizations/:mobilization_id/widgets/:widget_id/pressure/email
//
export default store => ({
  path: 'email',
  getComponent (nextState, callback) {
    require.ensure([], function (require) {
      injectAsyncReducer(store, 'mobilizations', require('~client/mobrender/redux/reducers').default)
      callback(null, require('./page.connected').default)
    })
  }
})
