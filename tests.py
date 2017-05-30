import unittest

from stacks import StackQueue


class StackTests(unittest.TestCase):
    def test_is_empty(self):
        q = StackQueue()
        self.assertEqual(q.is_empty(), True)
        q.add(2)
        self.assertEqual(q.is_empty(), False)
        q.remove()
        self.assertEqual(q.is_empty(), True)

    def test_order_is_preserved(self):
        q = StackQueue()
        q.add(1)
        q.add(2)
        q.add(3)
        q.add(4)
        self.assertEqual(q.remove(), 1)
        self.assertEqual(q.remove(), 2)
        q.add(5)
        q.add(6)
        q.add(7)
        q.add(8)
        self.assertEqual(q.remove(), 3)
        self.assertEqual(q.remove(), 4)
        self.assertEqual(q.remove(), 5)
        self.assertEqual(q.remove(), 6)
        self.assertEqual(q.remove(), 7)
        self.assertEqual(q.remove(), 8)
        self.assertEqual(q.is_empty(), True)

    def test_random_order(self):
        q = StackQueue()
        import random
        n = random.randint(0, 10)
        arr = [random.randint(-10000, 10000) for _ in range(n)]
        test_arr = []
        for a in arr:
            if a % 3 == 0 and not q.is_empty():
                test_arr.append(q.remove())
            q.add(a)
        while not q.is_empty():
            test_arr.append(q.remove())
        self.assertEqual(arr, test_arr)


if __name__ == '__main__':
    unittest.main()