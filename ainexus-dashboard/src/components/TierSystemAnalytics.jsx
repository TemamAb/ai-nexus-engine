import React from 'react'
import { Search, Send, Cpu, Network } from 'lucide-react'

const TierSystemAnalytics = () => {
  const tiers = {
    scanners: [
      { type: "DEX Scanner", status: "active", coverage: "28 DEXs", refresh: "0.8s", opportunities: "8,457" },
      { type: "CEX Scanner", status: "active", coverage: "12 CEXs", refresh: "1.2s", opportunities: "3,124" },
      { type: "Cross-Chain Scanner", status: "active", coverage: "6 Chains", refresh: "2.1s", opportunities: "876" },
      { type: "Lending Scanner", status: "partial", coverage: "8 Protocols", refresh: "1.5s", opportunities: "342" },
      { type: "NFT Market Scanner", status: "inactive", coverage: "0/5 Markets", refresh: "N/A", opportunities: "0" }
    ],
    relayers: [
      { node: "Relayer-01", status: "active", speed: "0.6s", success: "98.7%", backlog: "0" },
      { node: "Relayer-02", status: "active", speed: "0.7s", success: "98.2%", backlog: "2" },
      { node: "Relayer-03", status: "active", speed: "0.5s", success: "99.1%", backlog: "0" },
      { node: "Relayer-04", status: "warming", speed: "1.2s", success: "95.8%", backlog: "5" },
      { node: "Relayer-05", status: "inactive", speed: "N/A", success: "N/A", backlog: "N/A" },
      { node: "Relayer-06", status: "active", speed: "0.8s", success: "97.9%", backlog: "1" }
    ],
    orchestrators: [
      { name: "Main Orchestrator", status: "active", decisions: "8,457", strategies: "9/9", performance: "+27.4%" },
      { name: "Backup Orchestrator", status: "standby", decisions: "124", strategies: "6/9", performance: "+22.1%" },
      { name: "Testing Orchestrator", status: "testing", decisions: "47", strategies: "3/9", performance: "+15.8%" },
      { name: "Development Orchestrator", status: "inactive", decisions: "0", strategies: "0/9", performance: "N/A" }
    ]
  }

  const tierSummary = [
    { tier: "Scanners", active: 3, total: 5, capacity: "50 ops/sec", load: "28 ops/sec" },
    { tier: "Relayers", active: 4, total: 6, capacity: "100 tx/min", load: "42 tx/min" },
    { tier: "Orchestrators", active: 2, total: 4, capacity: "25 strategies", load: "9 strategies" }
  ]

  return (
    <div className="glass-card p-6">
      <h2 className="text-xl font-bold text-gradient flex items-center gap-2 mb-6">
        <Network className="w-5 h-5" />
        Three-Tier System Analytics
      </h2>

      <div className="space-y-6">
        {/* Tier Summary */}
        <div className="grid grid-cols-3 gap-4">
          {tierSummary.map((tier, index) => (
            <div key={index} className="bg-white/5 rounded-lg p-4 text-center">
              <p className="text-gray-400 text-sm">{tier.tier}</p>
              <p className="text-nexus-green font-bold text-lg">
                {tier.active}/{tier.total} Active
              </p>
              <p className="text-gray-400 text-xs mt-1">
                Load: {tier.load}
              </p>
            </div>
          ))}
        </div>

        {/* Scanners Tier */}
        <div>
          <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Search className="w-4 h-4" />
            Scanners Tier
          </h3>
          <div className="space-y-2">
            {tiers.scanners.map((scanner, index) => (
              <div key={index} className="flex items-center justify-between p-3 bg-white/5 rounded-lg">
                <div>
                  <p className="font-semibold">{scanner.type}</p>
                  <p className="text-gray-400 text-sm">Coverage: {scanner.coverage}</p>
                </div>
                <div className="text-right">
                  <span className={`status-${scanner.status}`}>
                    {scanner.status}
                  </span>
                  <p className="text-gray-400 text-xs mt-1">
                    {scanner.refresh} • {scanner.opportunities} ops
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Relayers Tier */}
        <div>
          <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Send className="w-4 h-4" />
            Relayers Tier
          </h3>
          <div className="space-y-2">
            {tiers.relayers.map((relayer, index) => (
              <div key={index} className="flex items-center justify-between p-3 bg-white/5 rounded-lg">
                <div>
                  <p className="font-semibold">{relayer.node}</p>
                  <p className="text-gray-400 text-sm">Speed: {relayer.speed}</p>
                </div>
                <div className="text-right">
                  <span className={`status-${relayer.status}`}>
                    {relayer.status}
                  </span>
                  <p className="text-gray-400 text-xs mt-1">
                    {relayer.success} • Queue: {relayer.backlog}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Orchestrators Tier */}
        <div>
          <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
            <Cpu className="w-4 h-4" />
            Orchestrators Tier
          </h3>
          <div className="space-y-2">
            {tiers.orchestrators.map((orchestrator, index) => (
              <div key={index} className="flex items-center justify-between p-3 bg-white/5 rounded-lg">
                <div>
                  <p className="font-semibold">{orchestrator.name}</p>
                  <p className="text-gray-400 text-sm">{orchestrator.decisions} decisions</p>
                </div>
                <div className="text-right">
                  <span className={`status-${orchestrator.status}`}>
                    {orchestrator.status}
                  </span>
                  <p className="text-nexus-green text-xs mt-1">
                    {orchestrator.performance}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  )
}

export default TierSystemAnalytics
