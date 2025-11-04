import React from 'react'
import SummaryMetrics from './SummaryMetrics'
import PerformanceMonitoring from './PerformanceMonitoring'
import FlashLoanAnalytics from './FlashLoanAnalytics'
import TierSystemAnalytics from './TierSystemAnalytics'
import WalletManagement from './WalletManagement'
import ProfitWithdrawal from './ProfitWithdrawal'

const Dashboard = () => {
  return (
    <div className="space-y-8">
      {/* Summary Metrics */}
      <SummaryMetrics />
      
      <div className="grid grid-cols-1 xl:grid-cols-2 gap-8">
        {/* Left Column */}
        <div className="space-y-8">
          <PerformanceMonitoring />
          <FlashLoanAnalytics />
        </div>
        
        {/* Right Column */}
        <div className="space-y-8">
          <TierSystemAnalytics />
          <WalletManagement />
          <ProfitWithdrawal />
        </div>
      </div>
    </div>
  )
}

export default Dashboard
