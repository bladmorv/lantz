import unittest
from time import sleep

from lantz import Driver, Feat, DictFeat, Action, Q_
from lantz.feat import MISSING

class aDriver(Driver):

    @Action()
    def run(self):
        return 42

    @Action()
    def run2(self, value):
        return 42 * value

    @Action()
    def run3(self, value):
        return 42 * value

    @Action(units='ms')
    def run4(self, value):
        return value


class ActionTest(unittest.TestCase):

    def test_action(self):
        obj = aDriver()
        self.assertEqual(obj.run(), 42)
        self.assertEqual(obj.run2(2), 42 * 2)
        self.assertEqual(obj.run3(3), 42 * 3)
        self.assertEqual(obj.run4(Q_(3, 'ms')), 3)
        self.assertEqual(obj.run4(Q_(3, 's')), 3000)

    def test_action_async(self):
        obj = aDriver()
        fut = obj.run_async()
        self.assertEqual(fut.result(), 42)
        fut = obj.run2_async(2)
        self.assertEqual(fut.result(), 42 * 2)

if __name__ == '__main__':
    unittest.main()
