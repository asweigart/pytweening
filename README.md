PyTweening
==========

A collection of tweening / easing functions implemented in Python.

Example Usage
=============

All tweening / easing functions are passed an argument of a float from 0.0 (for the beginning) to 1.0 (for the end) of the tween:

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
    >>> pytweening.easeInOutSine(0.5)
    0.49999999999999994
    >>> pytweening.easeInOutSine(0.75)
    0.8535533905932737
    >>> pytweening.easeInOutSine(1.0)
    1.0

The getLine() function also provides a Bresenham line algorithm implementation:

    >>> pytweening.getLine(0, 0, 5, 10)
    [(0, 0), (0, 1), (1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9), (5, 10)]

The getLinePoint() function finds a point on the provided line (even if it extends before or past the start or end points):

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

Support
-------

If you find this project helpful and would like to support its development, [consider donating to its creator on Patreon](https://www.patreon.com/AlSweigart).
