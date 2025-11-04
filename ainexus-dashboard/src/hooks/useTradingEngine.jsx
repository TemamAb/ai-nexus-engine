import React, { createContext, useContext, useState, useCallback } from 'react'

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
  const [activeStrategies, setActiveStrategies] = useState(0)
  const [tradesExecuted, setTradesExecuted] = useState(0)

  const startTradingEngine = useCallback(async () => {
    setTradingStatus('starting')
    
    // Simulate startup sequence
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    setTradingStatus('running')
    setActiveStrategies(9)
    
    // Simulate ongoing trades
    const interval = setInterval(() => {
      setTradesExecuted(prev => prev + 1)
    }, 5000)
    
    return () => clearInterval(interval)
  }, [])

  const stopTradingEngine = useCallback(() => {
    setTradingStatus('stopped')
    setActiveStrategies(0)
  }, [])

  const emergencyStop = useCallback(() => {
    setTradingStatus('emergency')
    setActiveStrategies(0)
    // Additional emergency procedures would go here
  }, [])

  const value = {
    startTradingEngine,
    stopTradingEngine,
    emergencyStop,
    tradingStatus,
    activeStrategies,
    tradesExecuted
  }

  return (
    <TradingContext.Provider value={value}>
      {children}
    </TradingContext.Provider>
  )
}
