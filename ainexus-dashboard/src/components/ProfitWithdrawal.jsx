import React, { useState } from 'react'
import { Download, Upload, Settings, History } from 'lucide-react'

const ProfitWithdrawal = () => {
  const [withdrawalMode, setWithdrawalMode] = useState('auto')
  const [selectedAccount, setSelectedAccount] = useState('primary')

  const accounts = [
    { id: 'primary', name: 'Primary Wallet', balance: '46.45 ETH' },
    { id: 'yield', name: 'Yield Account', balance: '23.23 ETH' },
    { id: 'cold', name: 'Cold Storage', balance: '6.09 ETH' }
  ]

  const withdrawalSettings = {
    auto: { threshold: '$50,000', frequency: 'Instant', destination: 'Primary Wallet' },
    limits: { daily: '$50,000', monthly: '$500,000' },
    history: { total: '47 transactions', last: '2 hours ago' }
  }

  return (
    <div className="glass-card p-6">
      <h2 className="text-xl font-bold text-gradient flex items-center gap-2 mb-6">
        <Download className="w-5 h-5" />
        Profit Withdrawal System
      </h2>

      <div className="space-y-6">
        {/* Withdrawal Mode Toggle */}
        <div className="flex space-x-4 mb-6">
          <button
            onClick={() => setWithdrawalMode('auto')}
            className={`flex-1 py-3 px-4 rounded-lg transition-all ${
              withdrawalMode === 'auto'
                ? 'bg-nexus-green text-nexus-dark font-bold'
                : 'bg-white/5 text-gray-400'
            }`}
          >
            <Settings className="w-4 h-4 inline mr-2" />
            Auto Withdrawal
          </button>
          <button
            onClick={() => setWithdrawalMode('manual')}
            className={`flex-1 py-3 px-4 rounded-lg transition-all ${
              withdrawalMode === 'manual'
                ? 'bg-nexus-blue text-white font-bold'
                : 'bg-white/5 text-gray-400'
            }`}
          >
            <Upload className="w-4 h-4 inline mr-2" />
            Manual Withdrawal
          </button>
        </div>

        {/* Auto Withdrawal Settings */}
        {withdrawalMode === 'auto' && (
          <div className="space-y-4">
            <div className="bg-white/5 rounded-lg p-4">
              <h3 className="font-semibold mb-3">Auto-Withdrawal Configuration</h3>
              <div className="space-y-3">
                <div className="flex justify-between">
                  <span className="text-gray-400">Threshold</span>
                  <span className="text-nexus-green">{withdrawalSettings.auto.threshold}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-400">Frequency</span>
                  <span className="text-nexus-green">{withdrawalSettings.auto.frequency}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-gray-400">Destination</span>
                  <span className="text-nexus-green">{withdrawalSettings.auto.destination}</span>
                </div>
              </div>
            </div>
            
            <button className="w-full bg-nexus-green text-nexus-dark font-bold py-3 px-4 rounded-lg transition-all hover:bg-nexus-green/90">
              Configure Auto-Withdrawal
            </button>
          </div>
        )}

        {/* Manual Withdrawal */}
        {withdrawalMode === 'manual' && (
          <div className="space-y-4">
            <div className="bg-white/5 rounded-lg p-4">
              <h3 className="font-semibold mb-3">Manual Withdrawal</h3>
              
              {/* Account Selection */}
              <div className="mb-4">
                <label className="text-gray-400 text-sm mb-2 block">Select Account</label>
                <div className="space-y-2">
                  {accounts.map((account) => (
                    <div
                      key={account.id}
                      onClick={() => setSelectedAccount(account.id)}
                      className={`p-3 rounded-lg cursor-pointer transition-all ${
                        selectedAccount === account.id
                          ? 'bg-nexus-blue/20 border border-nexus-blue'
                          : 'bg-white/5'
                      }`}
                    >
                      <div className="flex justify-between items-center">
                        <span className="font-semibold">{account.name}</span>
                        <span className="text-nexus-green">{account.balance}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Amount Input */}
              <div className="mb-4">
                <label className="text-gray-400 text-sm mb-2 block">Amount to Withdraw</label>
                <div className="flex space-x-2">
                  <input
                    type="text"
                    placeholder="0.00"
                    className="flex-1 bg-black/20 border border-white/10 rounded-lg px-3 py-2 text-white"
                  />
                  <button className="bg-nexus-blue text-white px-4 py-2 rounded-lg">
                    MAX
                  </button>
                </div>
                <p className="text-gray-400 text-xs mt-1">Available: $116,137 (46.45 ETH)</p>
              </div>

              {/* Security Notice */}
              <div className="bg-yellow-400/10 border border-yellow-400/20 rounded-lg p-3">
                <p className="text-yellow-400 text-sm">
                  í´’ 2FA verification required for withdrawal. Multi-sig approval needed for amounts over $10,000.
                </p>
              </div>
            </div>

            <button className="w-full bg-nexus-blue text-white font-bold py-3 px-4 rounded-lg transition-all hover:bg-nexus-blue/90">
              Execute Withdrawal
            </button>
          </div>
        )}

        {/* Withdrawal Limits & History */}
        <div className="grid grid-cols-2 gap-4 pt-4 border-t border-white/10">
          <div className="text-center">
            <History className="w-4 h-4 inline mr-2 text-gray-400" />
            <p className="text-gray-400 text-sm">Withdrawal History</p>
            <p className="text-nexus-green font-semibold">{withdrawalSettings.history.total}</p>
            <p className="text-gray-400 text-xs">Last: {withdrawalSettings.history.last}</p>
          </div>
          <div className="text-center">
            <Settings className="w-4 h-4 inline mr-2 text-gray-400" />
            <p className="text-gray-400 text-sm">Current Limits</p>
            <p className="text-nexus-green font-semibold">Daily: {withdrawalSettings.limits.daily}</p>
            <p className="text-gray-400 text-xs">Monthly: {withdrawalSettings.limits.monthly}</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ProfitWithdrawal
