import unittest
from IStack import MyStack, StackEmptyException

class Test_TestStack(unittest.TestCase):
	def setUp(self):
		self.test_stack = MyStack()

	def test_push_type_error(self):
		with self.assertRaises(TypeError):
			self.test_stack.Push(5)

	def test_push_done(self):
		self.test_stack.Push('test')
		self.assertFalse(self.test_stack.IsEmpty(), 'Push error')
		self.assertEqual(self.test_stack.Peek(), 'test', 'Wrong value')

	def test_pop_empty_exc(self):
		with self.assertRaises(StackEmptyException):
			self.test_stack.Pop()

	def test_pop_done(self):
		self.test_stack.Push('test')
		self.assertEqual(self.test_stack.Pop(), 'test', 'Wrong value')
		self.assertTrue(self.test_stack.IsEmpty(), 'Pop error')

	def test_peek_empty_exc(self):
		with self.assertRaises(StackEmptyException):
			self.test_stack.Peek()

	def test_peek_done(self):
		self.test_stack.Push('test')
		self.assertEqual(self.test_stack.Peek(), 'test', 'Wrong value')
		self.assertFalse(self.test_stack.IsEmpty(), 'Peek error')

	def test_contain_true(self):
		self.test_stack.Push('abc')
		self.assertTrue(self.test_stack.Contains('abc'), 'Must be True')

	def test_contain_false(self):
		self.test_stack.Push('abc')
		self.assertFalse(self.test_stack.Contains('cbd'), 'Must be False')

	def test_clear_done(self):
		self.test_stack.Clear()
		self.assertTrue(self.test_stack.IsEmpty(), 'Clear error')

if __name__ == '__main__':
	unittest.main()
