import React, { useState, useEffect } from 'react'
import Dashboard from './components/Dashboard'
import CommandCenter from './components/CommandCenter'
import { ConnectionProvider } from './hooks/useBlockchainConnection'
import { TradingProvider } from './hooks/useTradingEngine'

function App() {
  const [currentView, setCurrentView] = useState('dashboard')

  return (
    <ConnectionProvider>
      <TradingProvider>
        <div className="min-h-screen bg-nexus-dark">
          <header className="border-b border-white/10">
            <div className="container mx-auto px-4 py-4">
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-4">
                  <div className="w-8 h-8 bg-nexus-green rounded-lg nexus-glow"></div>
                  <h1 className="text-2xl font-bold text-gradient">AINEXUS ARBITRAGE</h1>
                </div>
                <nav className="flex space-x-6">
                  <button 
                    onClick={() => setCurrentView('dashboard')}
                    className={`px-4 py-2 rounded-lg transition-all ${
                      currentView === 'dashboard' 
                        ? 'bg-nexus-green text-nexus-dark font-bold' 
                        : 'text-gray-400 hover:text-white'
                    }`}
                  >
                    Dashboard
                  </button>
                  <button 
                    onClick={() => setCurrentView('command')}
                    className={`px-4 py-2 rounded-lg transition-all ${
                      currentView === 'command' 
                        ? 'bg-nexus-blue text-white font-bold' 
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
