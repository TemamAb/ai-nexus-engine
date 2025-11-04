import React, { createContext, useContext, useState } from 'react'

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

  const value = {
    connectionStatus,
    connectAllBlockchains: async () => setConnectionStatus('connected'),
    disconnectAll: () => setConnectionStatus('disconnected')
  }

  return (
    <ConnectionContext.Provider value={value}>
      {children}
    </ConnectionContext.Provider>
  )
}
