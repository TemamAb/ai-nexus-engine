import { useState, useEffect } from 'react';
const useCurrencyDisplay = () => {
  const [currency, setCurrency] = useState('USD');
  const [exchangeRate, setExchangeRate] = useState(3500);
  useEffect(() => {
    const fetchExchangeRate = async () => {
      try {
        setExchangeRate(3500 + Math.random() * 100);
      } catch (error) {
        console.error('Failed to fetch exchange rate:', error);
      }
    };
    fetchExchangeRate();
    const interval = setInterval(fetchExchangeRate, 30000);
    return () => clearInterval(interval);
  }, []);
  const toggleCurrency = (newCurrency) => {
    setCurrency(newCurrency);
  };
  return { currency, toggleCurrency, exchangeRate };
};
export default useCurrencyDisplay;
