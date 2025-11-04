import { useState } from 'react';
const useSystemControls = () => {
  const [systemMode, setSystemMode] = useState('balanced');
  const [pillarStatus, setPillarStatus] = useState({
    'Flash Loan System': true,
    'Gasless Mode': true,
    'Three-Tier System': true,
    'AI Optimization': true
  });
  const [isEmergency, setIsEmergency] = useState(false);
  const togglePillar = (pillar) => {
    setPillarStatus(prev => ({ ...prev, [pillar]: !prev[pillar] }));
  };
  const emergencyStop = () => {
    setIsEmergency(true);
    setPillarStatus({
      'Flash Loan System': false,
      'Gasless Mode': false,
      'Three-Tier System': false,
      'AI Optimization': false
    });
    setTimeout(() => setIsEmergency(false), 10000);
  };
  return { systemMode, setSystemMode, pillarStatus, togglePillar, emergencyStop, isEmergency };
};
export default useSystemControls;
