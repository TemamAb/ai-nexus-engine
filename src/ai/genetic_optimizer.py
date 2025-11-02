# coding: utf-8
"""
Genetic Algorithm Optimizer - Strategy evolution
Code Source: GA Python libraries, Hummingbot-inspired evolution
"""
import numpy as np
from typing import List, Dict

class GeneticOptimizer:
    def __init__(self, population_size: int = 50):
        self.population_size = population_size
        self.population = self.initialize_population()
    
    def initialize_population(self) -> List[Dict]:
        """Initialize population of trading strategies"""
        # Based on genetic algorithm initialization patterns
        population = []
        for i in range(self.population_size):
            strategy = {
                'id': i,
                'slippage_tol': np.random.uniform(0.001, 0.01),
                'profit_thresh': np.random.uniform(0.005, 0.03),
                'max_trade_size': np.random.uniform(0.01, 0.1)
            }
            population.append(strategy)
        return population
    
    def evolve_population(self, fitness_scores: List[float]) -> List[Dict]:
        """Evolve population based on fitness scores"""
        # Based on genetic algorithm selection/mutation patterns
        sorted_indices = np.argsort(fitness_scores)[::-1]
        elite_count = int(0.2 * self.population_size)
        new_population = [self.population[i] for i in sorted_indices[:elite_count]]
        
        # Fill rest with crossover and mutation
        while len(new_population) < self.population_size:
            parent1, parent2 = np.random.choice(sorted_indices[:10], 2, replace=False)
            child = self.crossover(self.population[parent1], self.population[parent2])
            child = self.mutate(child)
            new_population.append(child)
        
        return new_population
    
    def crossover(self, parent1: Dict, parent2: Dict) -> Dict:
        """Crossover two parents to create child"""
        child = {}
        for key in parent1.keys():
            if key != 'id':
                child[key] = (parent1[key] + parent2[key]) / 2
        return child
    
    def mutate(self, individual: Dict, mutation_rate: float = 0.1) -> Dict:
        """Apply mutation to individual"""
        # Based on GA mutation patterns
        for key in individual.keys():
            if key != 'id' and np.random.random() < mutation_rate:
                individual[key] *= np.random.uniform(0.9, 1.1)
        return individual
