import React from 'react'
import { TrendingUp, Wallet, Zap, Shield } from 'lucide-react'

const SummaryMetrics = () => {
  const metrics = [
    {
      title: "Total Accumulated Profit",
      value: "$20,847,392",
      subvalue: "8,338.96 ETH",
      icon: TrendingUp,
      trend: "+2.4% today",
      color: "text-nexus-green"
    },
    {
      title: "Available Funds",
      value: "$116,137", 
      subvalue: "46.45 ETH",
      icon: Wallet,
      trend: "Ready to trade",
      color: "text-nexus-blue"
    },
    {
      title: "Success Rate",
      value: "94.7%",
      subvalue: "978 trades",
      icon: Zap,
      trend: "+0.3%",
      color: "text-nexus-green"
    },
    {
      title: "Risk Score",
      value: "3.8/5.0",
      subvalue: "Low Risk",
      icon: Shield,
      trend: "+0.1 improvement",
      color: "text-nexus-green"
    }
  ]

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      {metrics.map((metric, index) => (
        <div key={index} className="glass-card p-6 nexus-glow">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-gray-400 text-sm">{metric.title}</p>
              <h3 className={`text-2xl font-bold ${metric.color} mt-2`}>
                {metric.value}
              </h3>
              <p className="text-gray-400 text-sm mt-1">{metric.subvalue}</p>
              <p className="text-nexus-green text-xs mt-2">{metric.trend}</p>
            </div>
            <div className="p-3 bg-white/5 rounded-lg">
              <metric.icon className="w-6 h-6 text-nexus-green" />
            </div>
          </div>
        </div>
      ))}
    </div>
  )
}

export default SummaryMetrics
