import React from 'react';
// import { connect } from 'react-redux';
import { Route } from 'react-router-dom';
// import { Context as SessionContext } from 'bonde-core-tools';
// import { Loading } from '../../../components/await';
import Sidebar from '../../../components/navigation/sidebar/Sidebar';

// Actions and Selectors
// import MobSelectors from '../../../mobrender/redux/selectors';
// import * as MobActions from '../../../mobrender/redux/action-creators';
// import * as CommunitySelectors from '../../../community/selectors';
// import DNSControlSelectors from '../../../community/dns-control-selectors';
// import * as DNSControlActions from '../../../community/action-creators/dns-control';

// SubRoutes
import MobilizationsScene from '../mobilizations';
import SidebarProvider from './Provider';

const SidebarView: React.FC = ({ children }) => {
  return (
    <SidebarProvider>
      <Sidebar>
        <Route path="/" component={MobilizationsScene} />
        {children}
      </Sidebar>
    </SidebarProvider>
  )
}

export default SidebarView;
