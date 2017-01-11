import React, { Component, PropTypes } from 'react'
import { Navigation } from 'react-router'
import reactMixin from 'react-mixin'
import { connect } from 'react-redux'

// Global module dependencies
import * as Paths from '../../../scripts/Mobilization/plugins/Templates/MobilizationTemplatesPaths'

// Children module dependencies
import { selectors as BlockSelectors } from '../../../modules/mobilizations/blocks'
import { selectors as WidgetSelectors } from '../../../modules/widgets'

// Current module dependencies
import * as MobilizationSelectors from '../selectors'
import { Mobilization } from '../components'

@reactMixin.decorate(Navigation)
export class MobilizationPage extends Component {

  componentDidMount() {
    const { mobilization, blocksIsLoaded, blocks } = this.props
    if (blocksIsLoaded && blocks.length === 0) {
      this.transitionTo(Paths.mobilizationTemplatesChoose(mobilization))
    }
  }

  render() {
    return <Mobilization {...this.props} editable={true} />
  }
}

MobilizationPage.propTypes = {
  mobilization: PropTypes.object,
  blocks: PropTypes.array,
  blockEditionMode: PropTypes.bool,
  widgets: PropTypes.array
}

const mapStateToProps = state => ({
  mobilization: MobilizationSelectors.getCurrent(state),
  blocksIsLoaded: BlockSelectors.isLoaded(state),
  blocks: MobilizationSelectors.getBlocks(state),
  widgets: WidgetSelectors.getList(state),
  // TODO: Refactor to selectors
  blockEditionMode: state.blocks.editionMode
})

export default connect(mapStateToProps)(MobilizationPage)
