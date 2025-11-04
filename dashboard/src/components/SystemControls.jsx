import React, { useState } from 'react';
import useSystemControls from '../hooks/useSystemControls';

const SystemControls = () => {
  const {
    systemMode,
    setSystemMode,
    pillarStatus,
    togglePillar,
    emergencyStop,
    isEmergency
  } = useSystemControls();

  const [confirmStop, setConfirmStop] = useState(false);

  return (
    <div className="system-controls">
      <div className="controls-header">
        <h2>Ì¥ß System Controls</h2>
        {isEmergency && <div className="emergency-alert">Ì∫® EMERGENCY STOP ACTIVE</div>}
      </div>

      <div className="control-group">
        <h3>Operation Mode</h3>
        <div className="mode-selector">
          <button 
            className={systemMode === 'performance' ? 'active' : ''}
            onClick={() => setSystemMode('performance')}
          >
            ‚ö° Performance Mode
          </button>
          <button 
            className={systemMode === 'balanced' ? 'active' : ''}
            onClick={() => setSystemMode('balanced')}
          >
            ‚öñÔ∏è Balanced Mode
          </button>
          <button 
            className={systemMode === 'safety' ? 'active' : ''}
            onClick={() => setSystemMode('safety')}
          >
            Ìª°Ô∏è Safety Mode
          </button>
        </div>
      </div>

      <div className="control-group">
        <h3>Core Pillars</h3>
        <div className="pillar-controls">
          {Object.entries(pillarStatus).map(([pillar, status]) => (
            <div key={pillar} className="pillar-item">
              <div className="pillar-info">
                <span className="pillar-name">{pillar}</span>
                <span className={`status ${status ? 'active' : 'inactive'}`}>
                  {status ? 'ACTIVE' : 'INACTIVE'}
                </span>
              </div>
              <button 
                className={`toggle-btn ${status ? 'active' : ''}`}
                onClick={() => togglePillar(pillar)}
              >
                {status ? 'Stop' : 'Start'}
              </button>
            </div>
          ))}
        </div>
      </div>

      <div className="control-group emergency">
        <h3>Emergency Protocols</h3>
        {!confirmStop ? (
          <button 
            className="emergency-btn"
            onClick={() => setConfirmStop(true)}
          >
            Ì∫® EMERGENCY STOP
          </button>
        ) : (
          <div className="emergency-confirm">
            <p>Are you sure? This will halt all trading activity.</p>
            <div className="confirm-buttons">
              <button onClick={emergencyStop} className="confirm-stop">
                CONFIRM STOP
              </button>
              <button onClick={() => setConfirmStop(false)} className="cancel">
                Cancel
              </button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default SystemControls;
