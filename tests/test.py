import unittest
import code

class TestCases(unittest.TestCase):

	def test_sanity(self):
		self.assertEqual(1, 1)


	def test_sanity(self):
		self.assertEqual(code.no_op(), 20)

if __name__ == "__main__":
	unittest.main()
