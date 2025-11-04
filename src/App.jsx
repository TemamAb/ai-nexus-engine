import React from 'react'
import Dashboard from './components/Dashboard'
import CommandCenter from './components/CommandCenter'
import { ConnectionProvider } from './hooks/useBlockchainConnection'
import { TradingProvider } from './hooks/useTradingEngine'

function App() {
  const [currentView, setCurrentView] = React.useState('dashboard')

  return (
    <ConnectionProvider>
      <TradingProvider>
        <div className="min-h-screen bg-gray-900">
          <header className="border-b border-gray-700">
            <div className="container mx-auto px-4 py-4">
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-4">
                  <div className="w-8 h-8 bg-green-500 rounded-lg"></div>
                  <h1 className="text-2xl font-bold text-white">AINEON TRADING</h1>
                </div>
                <nav className="flex space-x-6">
                  <button 
                    onClick={() => setCurrentView('dashboard')}
                    className={`px-4 py-2 rounded-lg transition-all ${
                      currentView === 'dashboard' 
                        ? 'bg-green-500 text-white font-bold' 
                        : 'text-gray-400 hover:text-white'
                    }`}
                  >
                    Dashboard
                  </button>
                  <button 
                    onClick={() => setCurrentView('command')}
                    className={`px-4 py-2 rounded-lg transition-all ${
                      currentView === 'command' 
                        ? 'bg-blue-500 text-white font-bold' 
                        : 'text-gray-400 hover:text-white'
                    }`}
                  >
                    Command Center
                  </button>
                </nav>
              </div>
            </div>
          </header>

          <main className="container mx-auto px-4 py-8">
            {currentView === 'dashboard' && <Dashboard />}
            {currentView === 'command' && <CommandCenter />}
          </main>
        </div>
      </TradingProvider>
    </ConnectionProvider>
  )
}

export default App
