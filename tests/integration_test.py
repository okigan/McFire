#!/usr/bin/env python

import numpy

from mcfire import mcfire
from unittest import TestCase

__author__ = 'iokulist'


class TestMcFire(TestCase):
    maxDiff = None

    def test_subtract_with_remainder(self, *args, **kvargs):
        balance, amount = mcfire.subtract_with_remainder(100, 125)

        self.assertEqual(balance, 0)
        self.assertEqual(amount, 25)

    def test_subtract_with_remainder(self, *args, **kvargs):
        post_tax_balance: numpy.ndarray = numpy.ones(5)
        tax_deferred_balance: numpy.ndarray = numpy.ones(5)
        tax_free_balance: numpy.ndarray = numpy.ones(5)
        _, _, _, d = mcfire.subtract_balances(100,
                                              1,
                                              0,
                                              post_tax_balance,
                                              tax_deferred_balance,
                                              tax_free_balance
                                              )

        self.assertEqual(97, d)
