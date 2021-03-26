# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 16:59:31 2019

@author: asus
"""

class Empty(Exception):
	pass

class ArrayQueue:
	DEFAULT_CAPACITY=5
	def __init__(self):
		self._data=[None]*ArrayQueue.DEFAULT_CAPACITY
		self._size=0
		self._front=0
	
	def __len__(self):
		return self._size
	
	def is_empty(self):
		return self._size==0
	
	def first(self):
		if self.is_empty():
			raise Empty("Queue is empty.")
		return self._data[self._front]
	
	def dequeue(self):
		if self.is_empty():
			raise Empty("Queue is empty.")
		result=self._data[self._front]
		self._data[self._front]=None
		self._front=(self._front+1)%len(self._data)
		self._size-=1
		return result
	
	def enqueue(self,e):
		if self._size==len(self._data):
			self._resize(2*len(self._data))
		avail=(self._front+self._size)%len(self._data)
		self._data[avail]=e
		self._size+=1
		
	def _resize(self,cap):
		old=self._data
		self._data=[None]*cap
		walk=self._front
		for k in range(self._size):
			self._data[k]=old[walk]
			walk=(1+walk)%len(old)
		self._front=0
		
	def __repr__(self):
		data=[]
		walk=self._front
		for k in range(self._size):
			data.append(self._data[walk])
			walk=(walk+1)%len(self._data)
		return f"{data}"
	
	
if __name__=="__main__":
	q=ArrayQueue()
	print(q)
	q.enqueue(1)
	q.enqueue(2)
	q.enqueue(3)
	print(q)
	q.enqueue(4)
	print(q)
	q.enqueue(5)
	print(q)
	q.dequeue()
	print(q)
	q.enqueue(8)
	print(q)
	q.enqueue(10)
	q.__repr__()
	print(q.first())
#%%	
class ArrayDeque:
	DEFAULT_CAPACITY=5
	def __init__(self):
		self._data=[None]*ArrayDeque.DEFAULT_CAPACITY
		self._size=0
		self._front=0
		
	def __len__(self):
		return self._size
	
	def is_empty(self):
		return self._size==0
	
	def first(self):
		if self.is_empty():
			raise Empty("Deque is empty")
		return self._data[self._front]
	
	def last(self):
		if self.is_empty():
			raise Empty("Deque is empty")
		back=(self._front+self._size-1)%len(self._data)
		return self._data[back]
	
	def delete_first(self):
		if self.is_empty():
			raise Empty("Deque is empty")
		result=self._data[self._front]
		self._data[self._front]=None
		self._front=(self._front+1)%len(self._data)
		self._size-=1
		return result
	
	def delete_last(self):
		if self.is_empty():
			raise Empty("Deque is empty")
		last=(self._front+self._size-1)%len(self._data)
		result=self._data[last]
		self._data[last]=None
		self._size-=1
		return result
	
	def _resize(self,cap):
		old=self._data
		self._data=[None]*cap
		walk=self._front
		for k in range(self._size):
			self._data[k]=old[walk]
			walk=(1+walk)%len(old)
		self._front=0
		
	def add_last(self,e):
		if self._size==len(self._data):
			self._resize(2*len(self._data))
		avail=(self._front+self._size)%len(self._data)
		self._data[avail]=e
		self._size+=1
		
	def add_first(self,e):
		if self._size==len(self._data):
			self._resize(2*len(self._data))
		avail=(self._front-1)%len(self._data)
		self._data[avail]=e
		self._front=avail
		self._size+=1
		
	def __repr__(self):
		L=[]
		walk=self._front
		for k in range(self._size):
			L.append(self._data[walk])
			walk=(walk+1)%len(self._data)
		return f"{L}"
	
if __name__=="__main__":
	D=ArrayDeque()
	D.add_first(1)
	D.add_first(2)
	D.add_last(3)
	D.add_last(4)
	D.add_first(5)
	print(D)
	D.delete_last()
	print(D)
	
	
