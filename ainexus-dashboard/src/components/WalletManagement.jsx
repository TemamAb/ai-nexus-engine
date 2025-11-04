import React from 'react'
import { Wallet, TrendingUp, Lock, PieChart } from 'lucide-react'

const WalletManagement = () => {
  const walletData = {
    total: { amount: "$189,425", eth: "75.77 ETH" },
    available: { amount: "$116,137", eth: "46.45 ETH", status: "liquid" },
    staked: { amount: "$58,068", eth: "23.23 ETH", apy: "+3.8% APY" },
    lp: { amount: "$15,220", eth: "6.09 ETH", growth: "+12.4% growth" }
  }

  const accounts = [
    { name: "Primary Wallet", balance: "46.45 ETH", type: "operational", status: "active" },
    { name: "Yield Account", balance: "23.23 ETH", type: "staking", status: "active" },
    { name: "Cold Storage", balance: "6.09 ETH", type: "security", status: "active" },
    { name: "Multi-sig Vault", balance: "0.00 ETH", type: "institutional", status: "inactive" }
  ]

  return (
    <div className="glass-card p-6">
      <h2 className="text-xl font-bold text-gradient flex items-center gap-2 mb-6">
        <Wallet className="w-5 h-5" />
        Wallet Management
      </h2>

      <div className="space-y-6">
        {/* Balance Overview */}
        <div className="grid grid-cols-2 gap-4">
          <div className="bg-white/5 rounded-lg p-4">
            <p className="text-gray-400 text-sm">Total Balance</p>
            <p className="text-2xl font-bold text-nexus-green mt-1">{walletData.total.amount}</p>
            <p className="text-gray-400 text-sm">{walletData.total.eth}</p>
          </div>
          <div className="bg-white/5 rounded-lg p-4">
            <p className="text-gray-400 text-sm">Available Funds</p>
            <p className="text-2xl font-bold text-nexus-blue mt-1">{walletData.available.amount}</p>
            <p className="text-gray-400 text-sm">{walletData.available.eth}</p>
            <span className="status-active mt-2 inline-block">Withdrawable</span>
          </div>
        </div>

        {/* Staked & LP Funds */}
        <div className="grid grid-cols-2 gap-4">
          <div className="bg-white/5 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <TrendingUp className="w-4 h-4 text-nexus-green" />
              <p className="text-gray-400 text-sm">Staked Funds</p>
            </div>
            <p className="text-xl font-bold text-nexus-green">{walletData.staked.amount}</p>
            <p className="text-gray-400 text-sm">{walletData.staked.eth}</p>
            <p className="text-nexus-green text-xs mt-1">{walletData.staked.apy}</p>
          </div>
          <div className="bg-white/5 rounded-lg p-4">
            <div className="flex items-center gap-2 mb-2">
              <PieChart className="w-4 h-4 text-nexus-blue" />
              <p className="text-gray-400 text-sm">LP Positions</p>
            </div>
            <p className="text-xl font-bold text-nexus-blue">{walletData.lp.amount}</p>
            <p className="text-gray-400 text-sm">{walletData.lp.eth}</p>
            <p className="text-nexus-green text-xs mt-1">{walletData.lp.growth}</p>
          </div>
        </div>

        {/* Account Management */}
        <div>
          <h3 className="text-lg font-semibold mb-4">Account Management</h3>
          <div className="space-y-3">
            {accounts.map((account, index) => (
              <div key={index} className="flex items-center justify-between p-3 bg-white/5 rounded-lg">
                <div className="flex items-center space-x-3">
                  <div className="w-8 h-8 bg-nexus-purple/20 rounded-lg flex items-center justify-center">
                    <Lock className="w-4 h-4 text-nexus-purple" />
                  </div>
                  <div>
                    <p className="font-semibold">{account.name}</p>
                    <p className="text-gray-400 text-sm">{account.type}</p>
                  </div>
                </div>
                <div className="text-right">
                  <p className="text-nexus-green font-semibold">{account.balance}</p>
                  <span className={`status-${account.status}`}>
                    {account.status}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Quick Actions */}
        <div className="flex space-x-3 pt-4 border-t border-white/10">
          <button className="flex-1 bg-nexus-green text-nexus-dark font-bold py-2 px-4 rounded-lg transition-all hover:bg-nexus-green/90">
            Add Funds
          </button>
          <button className="flex-1 bg-nexus-blue text-white font-bold py-2 px-4 rounded-lg transition-all hover:bg-nexus-blue/90">
            Re-stake
          </button>
          <button className="flex-1 bg-white/10 text-white font-bold py-2 px-4 rounded-lg transition-all hover:bg-white/20">
            Manage LP
          </button>
        </div>
      </div>
    </div>
  )
}

export default WalletManagement
