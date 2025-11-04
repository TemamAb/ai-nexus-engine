import { useState, useEffect } from 'react';

const useSystemMetrics = () => {
  const [metrics, setMetrics] = useState({
    flashLoanUtilization: 75.5,
    flashLoanSuccessRate: 98.7,
    gaslessTransactions: 847,
    gasSavings: 8450.75,
    aiImprovement: 12.3,
    activeModels: 6
  });

  const [systemHealth, setSystemHealth] = useState({
    scannerTier: 'healthy',
    relayerTier: 'healthy',
    orchestratorTier: 'healthy'
  });

  const [executionStats, setExecutionStats] = useState({
    tradesToday: 7,
    successRate: 95.8,
    avgProfit: 12500,
    executionSpeed: 1450
  });

  useEffect(() => {
    // Simulate real-time metrics updates
    const interval = setInterval(() => {
      setMetrics(prev => ({
        ...prev,
        flashLoanUtilization: 75 + Math.random() * 5,
        gaslessTransactions: prev.gaslessTransactions + Math.floor(Math.random() * 3)
      }));

      setExecutionStats(prev => ({
        ...prev,
        tradesToday: prev.tradesToday + (Math.random() > 0.8 ? 1 : 0),
        avgProfit: 12000 + Math.random() * 1000
      }));
    }, 3000);

    return () => clearInterval(interval);
  }, []);

  return {
    metrics,
    systemHealth,
    executionStats
  };
};

export default useSystemMetrics;
