import React, { createContext, useContext, useState, useCallback } from 'react'

const ConnectionContext = createContext()

export const useBlockchainConnection = () => {
  const context = useContext(ConnectionContext)
  if (!context) {
    throw new Error('useBlockchainConnection must be used within a ConnectionProvider')
  }
  return context
}

export const ConnectionProvider = ({ children }) => {
  const [connectionStatus, setConnectionStatus] = useState('disconnected')
  const [blockchainConnections, setBlockchainConnections] = useState(0)
  const [apiConnections, setApiConnections] = useState(0)

  const connectAllBlockchains = useCallback(async () => {
    setConnectionStatus('connecting')
    
    // Simulate connection process
    for (let i = 0; i <= 8; i++) {
      await new Promise(resolve => setTimeout(resolve, 500))
      setBlockchainConnections(i)
    }
    
    for (let i = 0; i <= 12; i++) {
      await new Promise(resolve => setTimeout(resolve, 200))
      setApiConnections(i)
    }
    
    setConnectionStatus('connected')
  }, [])

  const disconnectAll = useCallback(() => {
    setConnectionStatus('disconnected')
    setBlockchainConnections(0)
    setApiConnections(0)
  }, [])

  const value = {
    connectAllBlockchains,
    disconnectAll,
    connectionStatus,
    blockchainConnections,
    apiConnections
  }

  return (
    <ConnectionContext.Provider value={value}>
      {children}
    </ConnectionContext.Provider>
  )
}
