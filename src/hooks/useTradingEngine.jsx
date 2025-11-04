import React, { createContext, useContext, useState } from 'react'

const TradingContext = createContext()

export const useTradingEngine = () => {
  const context = useContext(TradingContext)
  if (!context) {
    throw new Error('useTradingEngine must be used within a TradingProvider')
  }
  return context
}

export const TradingProvider = ({ children }) => {
  const [tradingStatus, setTradingStatus] = useState('stopped')

  const value = {
    tradingStatus,
    startTradingEngine: async () => setTradingStatus('running'),
    stopTradingEngine: () => setTradingStatus('stopped'),
    emergencyStop: () => setTradingStatus('emergency')
  }

  return (
    <TradingContext.Provider value={value}>
      {children}
    </TradingContext.Provider>
  )
}
