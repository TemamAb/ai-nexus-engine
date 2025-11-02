# coding: utf-8
"""
Queue Manager - Resilient message queues for opportunity and execution
Code Source: Custom async orchestration with Redis/Kafka patterns
"""
import asyncio
from typing import Any, Callable
import json

class QueueManager:
    def __init__(self):
        self.opportunity_queue = asyncio.Queue(maxsize=1000)
        self.execution_queue = asyncio.Queue(maxsize=1000)
        self.workers = []
    
    async def publish_opportunity(self, opportunity: dict):
        """Publish arbitrage opportunity to queue"""
        # Based on async queue patterns
        await self.opportunity_queue.put(opportunity)
    
    async def consume_opportunities(self, callback: Callable):
        """Consume opportunities from queue"""
        while True:
            opportunity = await self.opportunity_queue.get()
            try:
                await callback(opportunity)
            except Exception as e:
                print(f"Error processing opportunity: {e}")
            finally:
                self.opportunity_queue.task_done()
    
    async def publish_execution(self, trade_data: dict):
        """Publish trade execution to queue"""
        await self.execution_queue.put(trade_data)
    
    async def consume_executions(self, callback: Callable):
        """Consume executions from queue"""
        while True:
            execution = await self.execution_queue.get()
            try:
                await callback(execution)
            except Exception as e:
                print(f"Error processing execution: {e}")
            finally:
                self.execution_queue.task_done()
