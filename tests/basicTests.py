import unittest
import sys
import os

sys.path.insert(0, os.path.abspath('..'))
import pytweening


class LineTests(unittest.TestCase):
    def test_startAndEndCoordinates(self):
        points = [(79, 16), (-67, -44), (-95, -56), (98, 47), (72, -6), (97, -63), (-38, -39), (91, -31), (-35, 96), (-72, 64), (-42, 11), (-11, 8), (-8, -35), (4, -27), (-51, -46), (33, -95), (94, -96), (-94, -77), (6, 28), (-82, -48)]
        for startPoint in points:
            for endPoint in points:
                linePoints = pytweening.getLine(startPoint[0], startPoint[1], endPoint[0], endPoint[1])
                self.assertEqual(startPoint, linePoints[0], 'Start point returned from getLine() is not the same as the original start point.')
                self.assertEqual(endPoint, linePoints[-1], 'End point returned from getLine() is not the same as the original end point.')

                x, y = pytweening.getPointOnLine(startPoint[0], startPoint[1], endPoint[0], endPoint[1], 0.0)
                self.assertEqual((int(x), int(y)), (linePoints[0][0], linePoints[0][1]), 'Start point of getPointOnLine() is not the same as the line\'s start point.')
                x, y = pytweening.getPointOnLine(startPoint[0], startPoint[1], endPoint[0], endPoint[1], 1.0)
                self.assertEqual((int(x), int(y)), (linePoints[-1][0], linePoints[-1][1]), 'End point of getPointOnLine() is not the same as the line\'s end point.')


if __name__ == '__main__':
    unittest.main()
