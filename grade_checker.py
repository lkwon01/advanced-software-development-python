import unittest
from todo import add_task, remove_task

class TestToDo(unittest.TestCase):
    def setUp(self):
        self.to_do = []

    def test_add_task(self):
        add_task("Test task", self.to_do)
        self.assertEqual(self.to_do, ["Test task"])
        add_task("Test task2", self.to_do)
        self.assertEqual(self.to_do, ["Test task", "Test task2"])

    def test_remove_task(self):
        add_task("Test task", self.to_do)
        add_task("Test task2", self.to_do)
        add_task("Test task3", self.to_do)
        remove_task(0, self.to_do)
        self.assertEqual(self.to_do, ["Test task2", "Test task3"])
        remove_task(1, self.to_do)
        self.assertEqual(self.to_do, ["Test task2"])
        remove_task(5, self.to_do)
        self.assertEqual(self.to_do, ["Test task2"])

if __name__ == '__main__':
    unittest.main()