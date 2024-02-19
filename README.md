PyTweening
==========

A collection of tweening (aka easing) functions implemented in Python. You can learn more about it in this blog post: https://inventwithpython.com/blog/TODO and in the Nordic Game Jam talk by Martin Jonasson and Petri Purho at https://youtu.be/Fy0aCDmgnxg?si=8pgITaxjJSKFyBuB&t=159

Example Usage
=============

All tweening functions are passed an argument of a float from 0.0 (the beginning of the path) to 1.0 (the end of the path) of the tween:

    >>> pytweening.linear(0.5)
    0.5
    >>> pytweening.linear(0.75)
    0.75
    >>> pytweening.linear(1.0)
    1.0
    >>> pytweening.easeInQuad(0.5)
    0.25
    >>> pytweening.easeInQuad(0.75)
    0.5625
    >>> pytweening.easeInQuad(1.0)
    1.0
    >>> pytweening.easeInOutSine(0.75)
    0.8535533905932737
    >>> pytweening.easeInOutSine(1.0)
    1.0

The getLine() function also provides a Bresenham line algorithm implementation:

    >>> pytweening.getLine(0, 0, 5, 10)
    [(0, 0), (0, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9), (5, 10)]

The getLinePoint() function finds (interpolates) a point on the given line (even if it extends before or past the start or end points):

    >>> getLinePoint(0, 0, 5, 10, 0.0)
    (0.0, 0.0)
    >>> getLinePoint(0, 0, 5, 10, 0.25)
    (1.25, 2.5)
    >>> getLinePoint(0, 0, 5, 10, 0.5)
    (2.5, 5.0)
    >>> getLinePoint(0, 0, 5, 10, 0.75)
    (3.75, 7.5)
    >>> getLinePoint(0, 0, 5, 10, 1.0)
    (5.0, 10.0)

PyTweening also provides iterators to get the XY coordinates in a for loop between two points (though some floating-point rounding errors naturally occur):

    >>> import pytweening
    >>> for x, y in pytweening.iterLinear(0, 0, 100, 150, 0.1): print(x, y)
    ...
    0.0 0.0
    10.0 15.0
    20.0 30.0
    30.000000000000004 45.00000000000001
    40.0 60.0
    50.0 75.0
    60.0 90.0
    70.0 105.0
    80.0 119.99999999999999
    89.99999999999999 135.0
    100.0 150.0
    >>> for x, y in pytweening.iterEaseOutQuad(0, 0, 100, 150, 0.1): print(x, y)
    ...
    0.0 0.0
    19.0 28.5
    36.00000000000001 54.00000000000001
    51.0 76.5
    64.00000000000001 96.00000000000001
    75.0 112.5
    84.0 126.0
    90.99999999999999 136.5
    96.00000000000001 144.0
    99.0 148.5
    100.0 150.0


Tweens
======

Support
-------

If you find this project helpful and would like to support its development, [consider donating to its creator on Patreon](https://www.patreon.com/AlSweigart).
