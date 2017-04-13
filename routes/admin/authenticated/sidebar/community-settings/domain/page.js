import React, { Component, PropTypes } from 'react'
import { browserHistory } from 'react-router'
import { Loading } from '~client/components/await'
import { Dialog } from '~client/ux/components'
import {
  ButtonPreview,
  DomainPreview,
  SubdomainPreview,
  SubdomainForm
} from '~client/community/components/dns'

import * as Paths from '~client/paths'

class Page extends Component {

  constructor (props) {
    super(props)
    this.state = {
      dnsHostedZone: undefined,
      dnsRecords: undefined,
      deletedHostedZone: undefined,
      deletedDNSRecord: undefined,
      showSubdomainForm: false
    }
  }

  toggleDNSRecords (dnsHostedZone) {
    if (dnsHostedZone !== this.state.dnsHostedZone) {
      this.props.fetchDNSRecords(dnsHostedZone)
        .then(dnsRecords => {
          this.setState({ dnsHostedZone, dnsRecords })
        })
    } else {
      this.setState({ dnsHostedZone: undefined, dnsRecords: undefined })
    }
  }

  confirmDeleteDomain () {
    const { deleteHostedZone } = this.props
    if (deleteHostedZone && this.state.deletedHostedZone) {

      this.setState({ deletedHostedZone: undefined })
      deleteHostedZone(this.state.deletedHostedZone)
    }
  }

  confirmDeleteSubdomain () {
    const { deleteDNSRecord } = this.props
    if (deleteDNSRecord && this.state.deletedDNSRecord) {

      this.setState({ deletedDNSRecord: undefined })
      deleteDNSRecord(this.state.deletedDNSRecord)
        .then(dnsRecord => {
          this.setState({ dnsRecords: this.state.dnsRecords.filter(d => d.id !== dnsRecord.id) })
        })
    }
  }

  render () {

    const { createDNSRecord, dnsHostedZoneIsLoading, dnsHostedZones, dnsRecordsIsLoading, ...formProps } = this.props

    return (
      <div className='domain-page'>
        <div className='dns-hosted-zones'>
          <h2>Domínios da comunidade</h2>
          {dnsHostedZoneIsLoading && <Loading />}
          {dnsHostedZones && dnsHostedZones.map((dnsHostedZone, index) => (
            <DomainPreview
              key={`dns-hosted-zone-${index}`}
              domain={dnsHostedZone}
              isActive={this.state.dnsHostedZone === dnsHostedZone}
              onClick={() => this.toggleDNSRecords(dnsHostedZone)}
              onDelete={() => this.setState({ deletedHostedZone: dnsHostedZone })}
            />
          ))}
          <ButtonPreview
            text='Adicionar novo domínio'
            onClick={() => browserHistory.push(Paths.communityDomainCreate())}
          />
          {this.state.deletedHostedZone && (
            <Dialog
              onConfirm={() => this.confirmDeleteDomain()}
              onCancel={() => this.setState({ deletedHostedZone: undefined })}
            >
              <p>Tem certeza que deseja remover o domínio <b>{this.state.deletedHostedZone.domain_name}</b>?</p>
            </Dialog>
          )}
        </div>
        {this.state.dnsHostedZone ? (
          <div className='dns-records'>
            <h2>Subdomínios externos</h2>
            {dnsRecordsIsLoading && <Loading />}
            {this.state.dnsRecords.map((dnsRecord, index) => (
              <SubdomainPreview
                key={`dns-record-${index}`}
                subdomain={dnsRecord}
                onDelete={() => this.setState({ deletedDNSRecord: dnsRecord })}
              />
            ))}
            {this.state.showSubdomainForm ? (
              <SubdomainForm
                dnsHostedZone={this.state.dnsHostedZone}
                onSubmit={values => {
                  const name = `${values.name}.${this.state.dnsHostedZone.domain_name}`
                  return createDNSRecord({
                    ...values,
                    name,
                    ttl: 3600,
                    dns_hosted_zone_id: this.state.dnsHostedZone.id
                  })
                  .then(dnsRecord => {
                    this.setState({ dnsRecords: [...this.state.dnsRecords, dnsRecord], showSubdomainForm: false })
                    return Promise.resolve()
                  })
                }}
                {...formProps}
              />
            ) : (
              <ButtonPreview
                text='Adicionar novo subdomínio externo'
                onClick={() => this.setState({ showSubdomainForm: true })}
              />
            )}
            {this.state.deletedDNSRecord && (
              <Dialog
                onConfirm={() => this.confirmDeleteSubdomain()}
                onCancel={() => this.setState({ deletedDNSRecord: undefined })}
              >
                <p>Tem certeza que deseja remover o subdomínio <b>{this.state.deletedDNSRecord.value}</b>?</p>
              </Dialog>
            )}
          </div>
        ) : null}
      </div>
    )
  }
}

Page.propTypes = {
  dnsHostedZoneIsLoading: PropTypes.bool,
  dnsRecordsIsLoading: PropTypes.bool,
  dnsHostedZones: PropTypes.array,
  fetchDNSRecords: PropTypes.func,
  deleteHostedZone: PropTypes.func,
  createDNSRecord: PropTypes.func
}

export default Page
