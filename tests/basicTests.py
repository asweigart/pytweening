from __future__ import division, print_function

import doctest
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytweening


TWEENS = [
    'linear',
    'easeInQuad',
    'easeOutQuad',
    'easeInOutQuad',
    'easeInCubic',
    'easeOutCubic',
    'easeInOutCubic',
    'easeInQuart',
    'easeOutQuart',
    'easeInOutQuart',
    'easeInQuint',
    'easeOutQuint',
    'easeInOutQuint',
    'easeInSine',
    'easeOutSine',
    'easeInOutSine',
    'easeInExpo',
    'easeOutExpo',
    'easeInOutExpo',
    'easeInCirc',
    'easeOutCirc',
    'easeInOutCirc',
    'easeInElastic',
    'easeOutElastic',
    'easeInOutElastic',
    'easeInBack',
    'easeOutBack',
    'easeInOutBack',
    'easeInBounce',
    'easeOutBounce',
    'easeInOutBounce',
    'easeInPoly',
    'easeOutPoly',
    'easeInOutPoly',
]


# https://stackoverflow.com/q/6655724/
class CustomAssertions(object):
    def assertFuncValue(self, func, param, expected, funcname='function', extra_msg='', **kwargs):
        """Asserts that func(param) == expected.

        Optionally receives the function name, used in the error message
        """
        value = func(param)
        if extra_msg:
            extra_msg = ' ' + extra_msg
        self.assertAlmostEqual(
            value, expected,
            msg='{0}({1}) should be {2}, but was {3}.'.format(funcname, param, expected, value, extra_msg),
            **kwargs)


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


class TestAll(unittest.TestCase, CustomAssertions):
    def test_zero(self):
        delta = 2 ** -15  # i.e. VERY small
        for name in TWEENS:
            func = getattr(pytweening, name)
            if name in ['easeInElastic', 'easeInOutElastic']:
                delta = 2 ** -11  # around 0.0005
            elif name in ['easeInBounce', 'easeInOutBounce']:
                delta = 2 ** -7  # around 0.0078
            self.assertFuncValue(func,   0, 0, name, delta=delta)
            self.assertFuncValue(func, 0.0, 0, name, delta=delta)

    def test_one(self):
        delta = 2 ** -15  # i.e. VERY small
        for name in TWEENS:
            func = getattr(pytweening, name)
            if name in ['easeOutElastic', 'easeInOutElastic']:
                delta = 2 ** -11  # around 0.0005
            elif name in ['easeOutBounce', 'easeInOutBounce']:
                delta = 2 ** -7  # around 0.0078
            self.assertFuncValue(func,   1, 1, name, delta=delta)
            self.assertFuncValue(func, 1.0, 1, name, delta=delta)

    def test_halfway(self):
        # Check that all the easeInOut* functions are halfway when passed 0.5.
        delta = 2 ** -15  # i.e. VERY small
        for name in TWEENS:
            func = getattr(pytweening, name)
            if name.startswith('easeInOut'):
                self.assertFuncValue(func, 0.5, 0.5, name, delta=delta)

    def test_wrong_input(self):
        # We've removed the 0.0 to 1.0 range check.
        """
        for name in TWEENS:
            func = getattr(pytweening, name)
            for input in [-1, -0.5, 1.5, 2]:
                kwargs = {}
                if sys.version_info.major >= 3 and sys.version_info.minor >= 3:
                    # msg parameter was added in Python 3.3:
                    # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
                    kwargs['msg'] = '{0}({1}) should raise ValueError'.format(name, input)

                with self.assertRaises(ValueError, **kwargs):
                    func(input)
        """

    def test_iterators(self):
        # Basic test that just calls the iterators and gets all their values in a list:
        list(pytweening.iterLinear(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInQuad(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseOutQuad(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInOutQuad(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInCubic(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseOutCubic(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInOutCubic(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInQuart(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseOutQuart(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInOutQuart(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInQuint(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseOutQuint(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInOutQuint(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInPoly(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseOutPoly(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInOutPoly(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInSine(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseOutSine(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInOutSine(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInExpo(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseOutExpo(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInOutExpo(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInCirc(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseOutCirc(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInOutCirc(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInElastic(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseOutElastic(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInOutElastic(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInBack(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseOutBack(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInOutBack(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInBounce(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseOutBounce(0, 0, 100, 100, 0.01))
        list(pytweening.iterEaseInOutBounce(0, 0, 100, 100, 0.01))



if __name__ == '__main__':
    unittest.main()
