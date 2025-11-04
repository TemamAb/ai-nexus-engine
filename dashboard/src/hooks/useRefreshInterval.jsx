import { useState, useEffect } from 'react';
const useRefreshInterval = () => {
  const [refreshInterval, setRefreshInterval] = useState(5000);
  const [lastUpdated, setLastUpdated] = useState(new Date());
  useEffect(() => {
    const interval = setInterval(() => {
      setLastUpdated(new Date());
      window.dispatchEvent(new CustomEvent('dashboardRefresh'));
    }, refreshInterval);
    return () => clearInterval(interval);
  }, [refreshInterval]);
  return { refreshInterval, setRefreshInterval, lastUpdated };
};
export default useRefreshInterval;
