import React from 'react'
import PropTypes from 'prop-types'
import { FormattedMessage } from 'react-intl'

import * as paths from '../../../paths'
import { TellAFriendBase } from '../../../ux'

const FormTellAFriend = ({ preview, mobilization, widget, ...props }) => (
  <TellAFriendBase
    preview={preview}
    mobilization={mobilization}
    widget={widget}
    message={
      <FormattedMessage
        id='form-widget.components--tell-a-friend.message'
        defaultMessage='Formulário submetido com sucesso!'
      />
    }
    href={paths.mobilization(mobilization)}
    {...props}
  />
)

FormTellAFriend.propTypes = {
  preview: PropTypes.bool,
  mobilization: PropTypes.object.isRequired,
  widget: PropTypes.object.isRequired
}

export default FormTellAFriend
