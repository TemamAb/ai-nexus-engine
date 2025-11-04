import React from 'react'

const Dashboard = () => {
  return (
    <div className="space-y-6">
      <div className="bg-gray-800 rounded-lg p-6">
        <h2 className="text-2xl font-bold text-white mb-4">AINEON AI Trading Dashboard</h2>
        <p className="text-green-400">íº€ Successfully deployed on Render!</p>
        <p className="text-gray-300 mt-2">Minimum configuration required: ETH_RPC_URL and WALLET_ADDRESS</p>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mt-6">
          <div className="bg-gray-700 p-4 rounded-lg">
            <h3 className="text-green-400 font-bold">System Status</h3>
            <p className="text-white">Operational</p>
          </div>
          <div className="bg-gray-700 p-4 rounded-lg">
            <h3 className="text-blue-400 font-bold">Blockchain</h3>
            <p className="text-white">Ethereum Connected</p>
          </div>
          <div className="bg-gray-700 p-4 rounded-lg">
            <h3 className="text-purple-400 font-bold">Trading</h3>
            <p className="text-white">Ready</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Dashboard
