// polyfill webpack require.ensure
if (typeof require.ensure !== 'function') require.ensure = (d, c) => c(require)
import { injectAsyncReducer } from '~client/store'

export default store => ({
  path: 'mobilizations/:mobilization_id/blocks/create',
  getComponent (nextState, callback) {
    require.ensure([], function (require) {
      injectAsyncReducer(store, 'mobilizations', require('~client/mobrender/redux/reducers').default)
      injectAsyncReducer(store, 'colorPicker', require('~components/color-picker/reducers').default)
      callback(null, require('./page.connected').default)
    })
  }
})
