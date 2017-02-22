import React from 'react'
import { shallow } from 'enzyme'
import { expect } from 'chai'

// Current module dependencies
import Form from '~widget-plugins/form/components/__form__'

describe('client/mobilizations/widgets/__plugins__/form/components/__form__', () => {
  let wrapper
  const props = {
    mobilization: {},
    widget: {
      settings: {
        finish_message_type: 'share'
      }
    },
    editable: true,
    configurable: true,
    hasNewField: false
  }

  beforeAll(() => {
    wrapper = shallow(<Form {...props} />)
  })

  describe('#render', () => {
    it('should render without crash', () => {
      expect(wrapper).to.be.ok
    })
  })
})
