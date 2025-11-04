-- AINexus Database Schema
CREATE TABLE IF NOT EXISTS trades (
    id SERIAL PRIMARY KEY,
    trade_hash VARCHAR(66) UNIQUE NOT NULL,
    amount_eth DECIMAL(20,8) NOT NULL,
    amount_usd DECIMAL(20,2) NOT NULL,
    profit_eth DECIMAL(20,8) NOT NULL,
    profit_usd DECIMAL(20,2) NOT NULL,
    strategy VARCHAR(50) NOT NULL,
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS profits (
    id SERIAL PRIMARY KEY,
    date DATE UNIQUE NOT NULL,
    daily_profit_eth DECIMAL(20,8) NOT NULL,
    daily_profit_usd DECIMAL(20,2) NOT NULL,
    trades_count INTEGER NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS system_metrics (
    id SERIAL PRIMARY KEY,
    metric_type VARCHAR(50) NOT NULL,
    metric_value JSONB NOT NULL,
    recorded_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS withdrawals (
    id SERIAL PRIMARY KEY,
    amount_eth DECIMAL(20,8) NOT NULL,
    amount_usd DECIMAL(20,2) NOT NULL,
    transaction_hash VARCHAR(66),
    status VARCHAR(20) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_trades_created_at ON trades(created_at);
CREATE INDEX IF NOT EXISTS idx_trades_status ON trades(status);
CREATE INDEX IF NOT EXISTS idx_profits_date ON profits(date);
CREATE INDEX IF NOT EXISTS idx_system_metrics_recorded_at ON system_metrics(recorded_at);

-- Initial configuration
INSERT INTO system_metrics (metric_type, metric_value) VALUES 
('profit_target', '{"daily_target_usd": 250000, "daily_target_eth": 71.428}'),
('system_config', '{"capacity_usd": 100000000, "required_roi": 0.0025}')
ON CONFLICT DO NOTHING;
