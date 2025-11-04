import React, { useState } from 'react'
import { Activity, Clock, Target, Cpu } from 'lucide-react'

const PerformanceMonitoring = () => {
  const [timeFrame, setTimeFrame] = useState('24h')

  const timeFrames = [
    { value: '1h', label: '1H' },
    { value: '24h', label: '24H' },
    { value: '7d', label: '7D' },
    { value: '30d', label: '30D' },
    { value: 'all', label: 'ALL' }
  ]

  const performanceMetrics = {
    execution: [
      { metric: "Execution Speed", value: "0.8s", trend: "-0.2s", status: "optimal" },
      { metric: "Success Rate", value: "94.7%", trend: "+0.3%", status: "optimal" },
      { metric: "Trades Executed", value: "978", trend: "+47 today", status: "active" },
      { metric: "API Response", value: "120ms", trend: "-15ms", status: "optimal" }
    ],
    throughput: [
      { metric: "Trades/Hour", value: "12", capacity: "50", utilization: "24%" },
      { metric: "Opportunities/Min", value: "3.2", capacity: "10", utilization: "32%" },
      { metric: "AI Decisions/Sec", value: "4.7", capacity: "20", utilization: "23.5%" }
    ],
    system: [
      { component: "AI Engine", status: "optimal", uptime: "99.98%", latency: "45ms" },
      { component: "Blockchain Nodes", status: "stable", uptime: "99.95%", latency: "180ms" },
      { component: "API Gateway", status: "healthy", uptime: "99.99%", latency: "120ms" },
      { component: "Risk Manager", status: "active", uptime: "100%", latency: "80ms" }
    ]
  }

  return (
    <div className="glass-card p-6">
      <div className="flex items-center justify-between mb-6">
        <h2 className="text-xl font-bold text-gradient flex items-center gap-2">
          <Activity className="w-5 h-5" />
          Performance Monitoring
        </h2>
        <div className="flex space-x-2">
          {timeFrames.map((frame) => (
            <button
              key={frame.value}
              onClick={() => setTimeFrame(frame.value)}
              className={`px-3 py-1 rounded-lg text-sm ${
                timeFrame === frame.value
                  ? 'bg-nexus-green text-nexus-dark font-bold'
                  : 'bg-white/5 text-gray-400'
              }`}
            >
              {frame.label}
            </button>
          ))}
        </div>
      </div>

      <div className="space-y-6">
        {/* Execution Metrics */}
        <div>
          <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Clock className="w-4 h-4" />
            Execution Performance
          </h3>
          <div className="grid grid-cols-2 gap-4">
            {performanceMetrics.execution.map((metric, index) => (
              <div key={index} className="bg-white/5 rounded-lg p-4">
                <div className="flex justify-between items-start">
                  <div>
                    <p className="text-gray-400 text-sm">{metric.metric}</p>
                    <p className="text-xl font-bold text-nexus-green mt-1">{metric.value}</p>
                    <p className="text-nexus-green text-xs mt-1">{metric.trend}</p>
                  </div>
                  <span className="status-active">Optimal</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Throughput Metrics */}
        <div>
          <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Target className="w-4 h-4" />
            Throughput & Capacity
          </h3>
          <div className="grid grid-cols-3 gap-4">
            {performanceMetrics.throughput.map((metric, index) => (
              <div key={index} className="bg-white/5 rounded-lg p-4">
                <p className="text-gray-400 text-sm">{metric.metric}</p>
                <p className="text-xl font-bold text-nexus-green mt-1">{metric.value}</p>
                <div className="mt-2">
                  <div className="w-full bg-gray-700 rounded-full h-2">
                    <div 
                      className="bg-nexus-green h-2 rounded-full" 
                      style={{ width: metric.utilization }}
                    ></div>
                  </div>
                  <p className="text-gray-400 text-xs mt-1">
                    {metric.utilization} of {metric.capacity}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* System Health */}
        <div>
          <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Cpu className="w-4 h-4" />
            System Health
          </h3>
          <div className="grid grid-cols-2 gap-4">
            {performanceMetrics.system.map((system, index) => (
              <div key={index} className="bg-white/5 rounded-lg p-4">
                <div className="flex justify-between items-center">
                  <div>
                    <p className="text-gray-400 text-sm">{system.component}</p>
                    <p className="text-nexus-green font-semibold mt-1">{system.uptime}</p>
                  </div>
                  <div className="text-right">
                    <span className={`status-${system.status}`}>
                      {system.status}
                    </span>
                    <p className="text-gray-400 text-xs mt-1">{system.latency}</p>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}

export default PerformanceMonitoring
