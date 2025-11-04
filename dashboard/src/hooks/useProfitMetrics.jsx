import { useState, useEffect } from 'react';
import useCurrencyDisplay from './useCurrencyDisplay';

const useProfitMetrics = () => {
  const { currency, exchangeRate } = useCurrencyDisplay();
  const [metrics, setMetrics] = useState({
    totalProfit: 1250157.50,
    daysOperational: 5,
    dailyAverage: 250031.50,
    currentDailyProfit: 87500,
    deploymentDate: '2024-01-01'
  });

  useEffect(() => {
    // Simulate real-time profit updates for $250K target
    const interval = setInterval(() => {
      setMetrics(prev => ({
        ...prev,
        totalProfit: prev.totalProfit + (Math.random() * 5000),
        currentDailyProfit: Math.min(250000, prev.currentDailyProfit + (Math.random() * 2500))
      }));
    }, 5000);

    return () => clearInterval(interval);
  }, []);

  const convertToETH = (usdAmount) => usdAmount / exchangeRate;

  const displayMetrics = {
    totalProfit: currency === 'ETH' ? convertToETH(metrics.totalProfit) : metrics.totalProfit,
    daysOperational: metrics.daysOperational,
    dailyAverage: currency === 'ETH' ? convertToETH(metrics.dailyAverage) : metrics.dailyAverage,
    projectedMonthly: currency === 'ETH' ? convertToETH(metrics.dailyAverage * 30) : metrics.dailyAverage * 30,
    currentDailyProfit: currency === 'ETH' ? convertToETH(metrics.currentDailyProfit) : metrics.currentDailyProfit
  };

  return displayMetrics;
};

export default useProfitMetrics;
