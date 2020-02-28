import unittest
from RangeFilter import RangeFilter
from MedianFilter import MedianFilter
class MyTest(unittest.TestCase):
    def test(self):
        rn=RangeFilter(2,5)
        mf = MedianFilter(2)
        self.assertEqual(rn.Update([1,4,7,0]), [2,4,5,2])
        self.assertEqual(mf.Update([2,4]), [2,4])
        self.assertEqual(mf.Update([0,4]), [1,4])
        self.assertEqual(mf.Update([0,1]), [0,4])
        self.assertEqual(mf.Update([5,10]), [0,4])
        print('success')

def main():
    print("python main function")
    runner = MyTest()
    runner.test()


if __name__ == '__main__':
    main()