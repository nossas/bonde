import PropTypes from 'prop-types'
import React from 'react'
import classnames from 'classnames'
import { intlShape } from 'react-intl'
import { browserHistory } from 'react-router'
import { Loading } from '~client/components/await'
import WidgetOverlay from './widget-overlay.connected'

import widgets from '../widgets/config'

const Widget = ({ saving, mobilization, block, widget, update, editable, intl }) => {
  // Resize column widget
  const { sm_size: smSize, md_size: mdSize, lg_size: lgSize } = widget
  const className = classnames(
    `px2 col mb4 md-mb0 col-${smSize}`,
    `sm-col-${smSize} md-col-${mdSize} lg-col-${lgSize}`
  )

  const widgetFilter = w => w.kind === widget.kind
  const widgetConfig = widgets(mobilization, widget, { intl }).filter(widgetFilter)[0]
  const { component: Component, redirect } = widgetConfig

  const widgetComponent = (
    <Component
      {...{ mobilization, block, widget, update, editable }}
    />
  )

  return (
    <div className={className}>
      {saving && <Loading />}
      {editable && redirect ? (
        <WidgetOverlay
          widget={widget}
          onEdit={() => {
            browserHistory.push(redirect)
          }}
          onDelete={() => {
            const message = intl.formatMessage({
              id: 'c--content-widget.delete-widget.confirm.message',
              defaultMessage: 'Deseja remover o widget?'
            })
            if (window.confirm(message)) {
              update({
                ...widget,
                settings: undefined,
                kind: 'draft'
              })
            }
          }}
        >
          {widgetComponent}
        </WidgetOverlay>
      ) : (!editable && widget.kind === 'draft' ? null : (
        widgetComponent
      ))}
    </div>
  )
}

Widget.propTypes = {
  mobilization: PropTypes.object,
  widget: PropTypes.object.isRequired,
  editable: PropTypes.bool,
  // Injected by redux
  update: PropTypes.func.isRequired,
  saving: PropTypes.bool,
  // Injected by react-intl
  intl: intlShape.isRequired
}

export default Widget
