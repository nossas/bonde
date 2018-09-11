import test from 'ava'
import React from 'react'
import { shallow } from 'enzyme'
import { Button, DonationInput, DonationTypeBox, Header } from './components'
import DonationUI from './DonationUI'

test.beforeEach(t => {
  t.context.defaultProps = {
    mainColor: 'rgba(0,0,0,1)',
    headerTitle: 'DonationTitle',
    submitLabel: 'DonationSubmit',
    paymentTypes: [{ kind: 'unique' }],
    onSubmit: () => {}
  }
  t.context.node = shallow(<DonationUI {...t.context.defaultProps} />)
})

test('should render submit Button with mainColor', t => {
  const { node, defaultProps } = t.context
  const buttonProps = node.find(Button).props()

  t.is(buttonProps.bgColor, defaultProps.mainColor)
  t.is(buttonProps.children, defaultProps.submitLabel)
  t.is(buttonProps.type, 'submit')
})

test('should render Header with mainColor', t => {
  const { node, defaultProps } = t.context
  const headerProps = node.find(Header).props()

  t.is(headerProps.bgColor, defaultProps.mainColor)
  t.is(headerProps.children, defaultProps.headerTitle)
})

test('should render DonationInput for each donationValues', t => {
  const { node, defaultProps } = t.context
  const donationValues = [10, 15, 20]
  node.setProps({ donationValues })
  
  const donationValueComponents = node.find(DonationInput)
  t.is(donationValueComponents.length, donationValues.length)

  donationValues.forEach((value, i) => {
    const donationInputProps = donationValueComponents.at(i).props()
    
    t.is(donationInputProps.mainColor, defaultProps.mainColor)
    t.is(donationInputProps.children, `R$ ${value}`)
  })
})

test('should select DonationInput when fill defaultDonationValue', t => {
  const { defaultProps } = t.context
  const donationIndex = 1
  const donationValues = [10, 15, 20]
  const node = shallow(
    <DonationUI
      {...defaultProps}
      donationValues={donationValues}
      defaultDonationValue={donationValues[donationIndex]}
    />
  )
  
  const donationProps = node.find(DonationInput).at(donationIndex).props()
  
  t.is(donationProps.active, true)
})

test('should select value when click on DonationInput', t => {
  const { node, defaultProps } = t.context
  const donationIndex = 2
  const donationValues = [10, 15, 20]
  node.setProps({ donationValues })
  
  const donationInput = node.find(DonationInput).at(donationIndex)
  donationInput.simulate('click')

  t.is(node.instance().state.donationValueSelected, donationValues[donationIndex])
})

test('should render payment types to choice by user', t => {
  const { node } = t.context
  const uniquePayment = { kind: 'unique' }
  const recurringPayment = {
    kind: 'recurring',
    label: 'Apoiar todo mês',
    period: 'mês'
  }
  node.setProps({ paymentTypes: [recurringPayment, uniquePayment] })
  
  t.is(node.find(DonationTypeBox.Item).length, 2)
})

test('should active paymentType when click DonationTypeBox.Item', t => {
  const { defaultProps } = t.context
  const uniquePayment = { kind: 'unique' }
  const recurringPayment = {
    kind: 'recurring',
    label: 'Apoiar todo mês',
    period: 'mês'
  }
  const node = shallow(
    <DonationUI
      {...defaultProps}
      paymentTypes={[recurringPayment, uniquePayment]}
    />
  )
  
  node.find(DonationTypeBox.Item).at(1).simulate('click')
  
  t.is(node.find(DonationTypeBox.Item).at(1).props().active, true)
})

test('should set default active the first item in paymentTypes', t => {
  const { defaultProps } = t.context
  const uniquePayment = { kind: 'unique' }
  const recurringPayment = {
    kind: 'recurring',
    label: 'Apoiar todo mês',
    period: 'mês'
  }
  const node = shallow(
    <DonationUI
      {...defaultProps}
      paymentTypes={[recurringPayment, uniquePayment]}
    />
  )
  
  const recurring = node.find(DonationTypeBox.Item).at(0)
  t.is(recurring.props().active, true)
})
