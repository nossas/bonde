import React from 'react'
import ReactDOM from 'react-dom'
import FontAwesome from 'react-fontawesome'
import ReactS3Uploader from 'react-s3-uploader'
import { Button } from '../../slate-editor-components/src'
import { insertInlineImage } from './ImageUtils'

interface ImageButtonProperties {
  className?: string;
  style?: any;
  value?: any;
  onChange?: any;
  changeState?: any;
  outerState?: any;
  type?: any;
  initialState?: any;
  signingUrl?: string;
}

class ImageButton extends React.Component<ImageButtonProperties, any> {
  upload: any

  constructor(properties) {
    super(properties)
    this.state = {
      progress: 0
    }
  }

  render() {
    const { value, onChange, className, style, signingUrl, outerState, type } = this.props
    return (
      <div style={{ display: 'inline-block' }}>
        <Button
          id={`slate-image-plugin-button-${outerState.uid}`}
          type={type}
          style={{ position: 'relative', ...style }}
          className={className}
          onClick={e => {
            const upload: any = ReactDOM.findDOMNode(this.upload)
            upload.value = ''
            upload.click()
          }}
        >
          <div style={{
            position: 'absolute',
            top: 0,
            left: 0,
            height: '100%',
            width: `${this.state.progress}%`,
            opacity: 0.4,
            backgroundColor: !this.state.error ? '#000' : '#92063E'
          }} />
          <FontAwesome name='image' />
        </Button>
        <ReactS3Uploader
          signingUrl={signingUrl}
          accept='image/*'
          onProgress={progress => { this.setState({ progress }) }}
          onError={e => console.error('[SlateEditor][ImagePlugin]:', e)}
          onFinish={e => {
            const source = e.signedUrl.slice(0, Math.max(0, e.signedUrl.indexOf('?')))
            onChange(insertInlineImage({ change: value.change(), src: source }))
            this.setState({ progress: 0 })
          }}
          ref={input => { this.upload = input }}
          style={{ position: 'absolute', visibility: 'hidden' }}
        />
      </div>
    )
  }
}

export default ImageButton
