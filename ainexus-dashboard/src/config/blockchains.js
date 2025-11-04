export const BLOCKCHAINS = {
  ethereum: {
    name: 'Ethereum',
    rpcUrl: import.meta.env.VITE_ETH_RPC_URL,
    chainId: 1,
    explorer: 'https://etherscan.io'
  },
  arbitrum: {
    name: 'Arbitrum',
    rpcUrl: import.meta.env.VITE_ARB_RPC_URL,
    chainId: 42161,
    explorer: 'https://arbiscan.io'
  },
  optimism: {
    name: 'Optimism',
    rpcUrl: import.meta.env.VITE_OPT_RPC_URL,
    chainId: 10,
    explorer: 'https://optimistic.etherscan.io'
  },
  polygon: {
    name: 'Polygon',
    rpcUrl: import.meta.env.VITE_POL_RPC_URL,
    chainId: 137,
    explorer: 'https://polygonscan.com'
  },
  base: {
    name: 'Base',
    rpcUrl: import.meta.env.VITE_BASE_RPC_URL,
    chainId: 8453,
    explorer: 'https://basescan.org'
  },
  bnb: {
    name: 'BNB Chain',
    rpcUrl: import.meta.env.VITE_BNB_RPC_URL,
    chainId: 56,
    explorer: 'https://bscscan.com'
  },
  avalanche: {
    name: 'Avalanche',
    rpcUrl: import.meta.env.VITE_AVAX_RPC_URL,
    chainId: 43114,
    explorer: 'https://snowtrace.io'
  },
  solana: {
    name: 'Solana',
    rpcUrl: import.meta.env.VITE_SOL_RPC_URL,
    explorer: 'https://solscan.io'
  }
}

export const APIS = {
  coingecko: {
    name: 'CoinGecko',
    key: import.meta.env.VITE_CG_API_KEY,
    baseUrl: 'https://api.coingecko.com/api/v3'
  },
  thegraph: {
    name: 'The Graph',
    key: import.meta.env.VITE_GRAPH_API_KEY,
    baseUrl: 'https://api.thegraph.com'
  },
  alchemy: {
    name: 'Alchemy',
    key: import.meta.env.VITE_ALCHEMY_API_KEY,
    baseUrl: 'https://eth-mainnet.g.alchemy.com/v2'
  },
  infura: {
    name: 'Infura',
    key: import.meta.env.VITE_INFURA_API_KEY,
    baseUrl: 'https://mainnet.infura.io/v3'
  },
  moralis: {
    name: 'Moralis',
    key: import.meta.env.VITE_MORALIS_API_KEY,
    baseUrl: 'https://deep-index.moralis.io/api/v2'
  },
  oneinch: {
    name: '1inch',
    key: import.meta.env.VITE_1INCH_API_KEY,
    baseUrl: 'https://api.1inch.io/v4.0'
  },
  zerox: {
    name: '0x API',
    key: import.meta.env.VITE_ZEROX_API_KEY,
    baseUrl: 'https://api.0x.org'
  },
  defipulse: {
    name: 'DeFi Pulse',
    key: import.meta.env.VITE_DEFIPULSE_API_KEY,
    baseUrl: 'https://api.defipulse.com'
  }
}
