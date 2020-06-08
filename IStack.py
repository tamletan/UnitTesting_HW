import numpy as np

class IStack:
	def Clear(self):
		raise NotImplementedError()
	def Contains(self, value):
		raise NotImplementedError()
	def Peek(self):
		raise NotImplementedError()
	def Push(self, value):
		raise NotImplementedError()
	def Pop(self):
		raise NotImplementedError()
	def IsEmpty(self):
		raise NotImplementedError()

class MyStack(IStack):
	def __init__(self):
		self.data = []

	def Clear(self):
		self.data.clear()

	def Contains(self, value):
		return True if any(np.asarray(self.data) == value) else False

	def Peek(self):
		if self.IsEmpty():
			raise StackEmptyException("Stack is Empty")
		return self.data[-1]

	def Push(self, value):
		if not isinstance(value, str):
			raise TypeError("item is not of type str")
		self.data.append(value)

	def Pop(self):
		if self.IsEmpty():
			raise StackEmptyException("Stack is Empty")
		tmp = self.data[-1]
		del self.data[-1]
		return tmp

	def IsEmpty(self):
		return True if len(self.data) == 0 else False

class StackEmptyException(Exception):
	pass

if __name__ == '__main__':
	k = MyStack()