from asyncio import Queue
from typing import Any, AsyncIterable, Generic, TypeVar, Optional
from .utils import Countable


T= TypeVar('T')

class QueueDone(Exception):
	pass


class IterableQueue(Queue[T], AsyncIterable[T], Countable):
	"""Async.Queue subclass to support async iteration and QueueDone"""

	def __init__(self, total: int = 0, 
					count_items: bool = True, **kwargs): ...


	def add_producer(self, N : int = 1) -> int: ...


	async def finish(self) -> bool: ...
		

	async def shutdown(self) -> None: ...
		

	# @property
	# def is_done(self) -> bool:
	# 	return self._done

	
	@property
	def is_finished(self) -> bool: ...


	@property
	def maxsize(self) -> int: ...
		
	
	def full(self) -> bool: ...


	async def get(self) -> T: ...
		


	def get_nowait(self) -> T: ...


	async def put(self, item: T) -> None: ...


	def put_nowait(self, item: T) -> None: ...
		

	def qsize(self) -> int: ...


	def task_done(self) -> None: ...
	

	@property
	def count(self) -> int: ...
	

	async def __aiter__(self): ...
		
	
	async def __anext__(self) -> T: ...
