import React, { useState, useEffect } from 'react'
import { Play, Square, RefreshCw, Settings, AlertTriangle } from 'lucide-react'
import { useBlockchainConnection } from '../hooks/useBlockchainConnection'
import { useTradingEngine } from '../hooks/useTradingEngine'

const CommandCenter = () => {
  const { 
    connectAllBlockchains, 
    disconnectAll,
    connectionStatus,
    blockchainConnections,
    apiConnections 
  } = useBlockchainConnection()

  const {
    startTradingEngine,
    stopTradingEngine,
    emergencyStop,
    tradingStatus
  } = useTradingEngine()

  const [startupProgress, setStartupProgress] = useState(0)
  const [systemStatus, setSystemStatus] = useState('standby')

  const blockchains = [
    { name: 'Ethereum', rpc: 'ETH_RPC_URL', status: 'disconnected' },
    { name: 'Arbitrum', rpc: 'ARB_RPC_URL', status: 'disconnected' },
    { name: 'Optimism', rpc: 'OPT_RPC_URL', status: 'disconnected' },
    { name: 'Polygon', rpc: 'POL_RPC_URL', status: 'disconnected' },
    { name: 'Base', rpc: 'BASE_RPC_URL', status: 'disconnected' },
    { name: 'BNB Chain', rpc: 'BNB_RPC_URL', status: 'disconnected' },
    { name: 'Avalanche', rpc: 'AVAX_RPC_URL', status: 'disconnected' },
    { name: 'Solana', rpc: 'SOL_RPC_URL', status: 'disconnected' }
  ]

  const apis = [
    { name: 'CoinGecko', key: 'CG_API_KEY', status: 'disconnected' },
    { name: 'The Graph', key: 'GRAPH_API_KEY', status: 'disconnected' },
    { name: 'Alchemy', key: 'ALCHEMY_API_KEY', status: 'disconnected' },
    { name: 'Infura', key: 'INFURA_API_KEY', status: 'disconnected' },
    { name: 'Moralis', key: 'MORALIS_API_KEY', status: 'disconnected' },
    { name: '1inch', key: '1INCH_API_KEY', status: 'disconnected' },
    { name: '0x API', key: 'ZEROX_API_KEY', status: 'disconnected' },
    { name: 'DeFi Pulse', key: 'DEFIPULSE_API_KEY', status: 'disconnected' }
  ]

  const handleConnectAll = async () => {
    setSystemStatus('connecting')
    await connectAllBlockchains()
    setSystemStatus('connected')
  }

  const handleStartTrading = async () => {
    setSystemStatus('starting')
    await startTradingEngine()
    setSystemStatus('running')
  }

  const handleEmergencyStop = () => {
    emergencyStop()
    setSystemStatus('emergency')
  }

  return (
    <div className="space-y-8">
      {/* Command Status Card */}
      <div className="glass-card p-6 nexus-glow">
        <div className="text-center mb-6">
          <h1 className="text-2xl font-bold text-gradient">��� AINEXUS COMMAND CENTER</h1>
          <p className="text-gray-400 mt-2">Control Panel for Arbitrage Trading System</p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
          <div className="text-center">
            <div className={`text-2xl font-bold ${
              systemStatus === 'running' ? 'text-nexus-green' : 
              systemStatus === 'emergency' ? 'text-red-400' : 'text-gray-400'
            }`}>
              {systemStatus.toUpperCase()}
            </div>
            <p className="text-gray-400 text-sm">SYSTEM STATUS</p>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-nexus-blue">
              {blockchainConnections}/8
            </div>
            <p className="text-gray-400 text-sm">BLOCKCHAIN CONNECTIONS</p>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-nexus-purple">
              {apiConnections}/12
            </div>
            <p className="text-gray-400 text-sm">API ENDPOINTS</p>
          </div>
        </div>

        {/* Control Buttons */}
        <div className="flex space-x-4 mb-6">
          <button
            onClick={handleConnectAll}
            disabled={systemStatus === 'connecting' || systemStatus === 'running'}
            className="flex-1 bg-nexus-blue text-white font-bold py-3 px-6 rounded-lg transition-all hover:bg-nexus-blue/90 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
          >
            <RefreshCw className="w-4 h-4" />
            CONNECT ALL BLOCKCHAINS
          </button>
          
          <button
            onClick={handleStartTrading}
            disabled={systemStatus !== 'connected' && systemStatus !== 'standby'}
            className="flex-1 bg-nexus-green text-nexus-dark font-bold py-3 px-6 rounded-lg transition-all hover:bg-nexus-green/90 disabled:opacity-50 disabled:cursor-not-allowed flex items-center justify-center gap-2"
          >
            <Play className="w-4 h-4" />
            START TRADING ENGINE
          </button>
          
          <button
            onClick={handleEmergencyStop}
            className="flex-1 bg-red-500 text-white font-bold py-3 px-6 rounded-lg transition-all hover:bg-red-600 flex items-center justify-center gap-2"
          >
            <Square className="w-4 h-4" />
            EMERGENCY STOP
          </button>
        </div>

        {/* Startup Progress */}
        {systemStatus === 'connecting' && (
          <div className="bg-white/5 rounded-lg p-4">
            <div className="flex justify-between text-sm mb-2">
              <span>Starting System...</span>
              <span>{startupProgress}%</span>
            </div>
            <div className="w-full bg-gray-700 rounded-full h-2">
              <div 
                className="bg-nexus-green h-2 rounded-full transition-all duration-300"
                style={{ width: `${startupProgress}%` }}
              ></div>
            </div>
          </div>
        )}
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        {/* Blockchain Connections */}
        <div className="glass-card p-6">
          <h2 className="text-xl font-bold text-gradient mb-4">Blockchain Connections</h2>
          <div className="space-y-3">
            {blockchains.map((blockchain, index) => (
              <div key={index} className="flex items-center justify-between p-3 bg-white/5 rounded-lg">
                <div className="flex items-center space-x-3">
                  <div className={`w-3 h-3 rounded-full ${
                    blockchain.status === 'connected' ? 'bg-nexus-green' : 'bg-red-400'
                  }`}></div>
                  <span className="font-semibold">{blockchain.name}</span>
                </div>
                <div className="text-right">
                  <p className="text-gray-400 text-sm">{blockchain.rpc}</p>
                  <p className="text-gray-400 text-xs">Status: {blockchain.status}</p>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* API Connections */}
        <div className="glass-card p-6">
          <h2 className="text-xl font-bold text-gradient mb-4">API Services</h2>
          <div className="space-y-3">
            {apis.map((api, index) => (
              <div key={index} className="flex items-center justify-between p-3 bg-white/5 rounded-lg">
                <div className="flex items-center space-x-3">
                  <div className={`w-3 h-3 rounded-full ${
                    api.status === 'connected' ? 'bg-nexus-green' : 'bg-red-400'
                  }`}></div>
                  <span className="font-semibold">{api.name}</span>
                </div>
                <div className="text-right">
                  <p className="text-gray-400 text-sm">{api.key}</p>
                  <p className="text-gray-400 text-xs">Status: {api.status}</p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Emergency Protocols */}
      <div className="glass-card p-6 border border-red-400/20">
        <h2 className="text-xl font-bold text-red-400 flex items-center gap-2 mb-4">
          <AlertTriangle className="w-5 h-5" />
          Emergency Protocols
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
          <div className="bg-red-400/10 p-4 rounded-lg">
            <h3 className="font-semibold text-red-400 mb-2">Immediate Actions</h3>
            <ul className="text-gray-400 space-y-1">
              <li>• Cancel pending transactions</li>
              <li>• Close open positions</li>
              <li>• Suspend new trades</li>
            </ul>
          </div>
          <div className="bg-yellow-400/10 p-4 rounded-lg">
            <h3 className="font-semibold text-yellow-400 mb-2">Safety Measures</h3>
            <ul className="text-gray-400 space-y-1">
              <li>• Preserve wallet capital</li>
              <li>• Maintain monitoring</li>
              <li>• Preserve log files</li>
            </ul>
          </div>
          <div className="bg-nexus-green/10 p-4 rounded-lg">
            <h3 className="font-semibold text-nexus-green mb-2">Recovery</h3>
            <ul className="text-gray-400 space-y-1">
              <li>• Investigate root cause</li>
              <li>• System diagnostics</li>
              <li>• Gradual restart</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  )
}

export default CommandCenter
