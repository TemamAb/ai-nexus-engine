import React from 'react'
import { DollarSign, TrendingUp, Zap, Shield } from 'lucide-react'

const FlashLoanAnalytics = () => {
  const providers = [
    { name: "Aave V3", utilized: "$18.7M", success: "98.2%", cost: "0.09%", status: "active" },
    { name: "dYdX", utilized: "$12.4M", success: "97.8%", cost: "0.08%", status: "active" },
    { name: "Uniswap V3", utilized: "$8.9M", success: "96.5%", cost: "0.12%", status: "active" },
    { name: "Balancer", utilized: "$5.2M", success: "95.7%", cost: "0.15%", status: "active" },
    { name: "Euler", utilized: "$3.1M", success: "94.3%", cost: "0.11%", status: "testing" }
  ]

  const metrics = [
    { label: "Total Flash Loans", value: "847", trend: "+38" },
    { label: "Success Rate", value: "97.1%", trend: "+0.4%" },
    { label: "Avg Profit/Loan", value: "$124.80", trend: "+$3.20" },
    { label: "Gas Efficiency", value: "88.7%", trend: "-0.8%" }
  ]

  return (
    <div className="glass-card p-6">
      <h2 className="text-xl font-bold text-gradient flex items-center gap-2 mb-6">
        <Zap className="w-5 h-5" />
        Flash Loan Analytics
      </h2>

      <div className="space-y-6">
        {/* Key Metrics */}
        <div className="grid grid-cols-2 gap-4">
          {metrics.map((metric, index) => (
            <div key={index} className="bg-white/5 rounded-lg p-4">
              <p className="text-gray-400 text-sm">{metric.label}</p>
              <p className="text-xl font-bold text-nexus-green mt-1">{metric.value}</p>
              <p className="text-nexus-green text-xs mt-1">{metric.trend}</p>
            </div>
          ))}
        </div>

        {/* Providers Table */}
        <div>
          <h3 className="text-lg font-semibold mb-4">Providers Performance</h3>
          <div className="space-y-3">
            {providers.map((provider, index) => (
              <div key={index} className="flex items-center justify-between p-3 bg-white/5 rounded-lg">
                <div className="flex items-center space-x-4">
                  <div className="w-8 h-8 bg-nexus-blue/20 rounded-lg flex items-center justify-center">
                    <DollarSign className="w-4 h-4 text-nexus-blue" />
                  </div>
                  <div>
                    <p className="font-semibold">{provider.name}</p>
                    <p className="text-gray-400 text-sm">Utilized: {provider.utilized}</p>
                  </div>
                </div>
                <div className="text-right">
                  <div className="flex items-center space-x-4">
                    <div>
                      <p className="text-nexus-green text-sm">Success: {provider.success}</p>
                      <p className="text-gray-400 text-xs">Cost: {provider.cost}</p>
                    </div>
                    <span className={`status-${provider.status}`}>
                      {provider.status}
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Performance Summary */}
        <div className="grid grid-cols-3 gap-4 pt-4 border-t border-white/10">
          <div className="text-center">
            <p className="text-gray-400 text-sm">Provider Utilization</p>
            <p className="text-nexus-green font-bold text-lg">78.4%</p>
          </div>
          <div className="text-center">
            <p className="text-gray-400 text-sm">Cost Efficiency</p>
            <p className="text-nexus-green font-bold text-lg">89.7%</p>
          </div>
          <div className="text-center">
            <p className="text-gray-400 text-sm">Arbitrage Margin</p>
            <p className="text-nexus-green font-bold text-lg">1.47%</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default FlashLoanAnalytics
