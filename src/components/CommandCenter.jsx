import React from 'react'

const CommandCenter = () => {
  return (
    <div className="bg-gray-800 rounded-lg p-6">
      <h2 className="text-2xl font-bold text-white mb-4">Command Center</h2>
      <p className="text-green-400">Configure your environment variables to enable trading.</p>
      <div className="mt-4 p-4 bg-yellow-900 rounded-lg">
        <p className="text-yellow-200">Required: ETH_RPC_URL and WALLET_ADDRESS</p>
      </div>
    </div>
  )
}

export default CommandCenter
