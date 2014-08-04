
from setuptools import setup


# Dynamically calculate the version based on pyganim.VERSION.
version = __import__('pytweening').__version__


setup(
    name='PyTweening',
    version=version,
    url='https://github.com/asweigart/pytweening',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description=('A collection of tweening / easing functions.'),
    license='BSD',
    packages=['pytweening'],
    test_suite='tests',
    keywords="2D animation tween tweening easing",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)