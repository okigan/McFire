#!/usr/bin/env python
import random

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

    def test_subtract_balances(self, *args, **kvargs):
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

    def test_simulate(self, *args, **kvargs):
        random.seed(42)  # meaning of life https://en.wikipedia.org/wiki/42_(number)

        post_tax_balance, tax_deferred_balance, tax_free_balance = mcfire.simulate()

        self.assertAlmostEqual(post_tax_balance.sum(), 21427238.320259757)
        self.assertAlmostEqual(tax_deferred_balance.sum(), 35176169.35713017)
        self.assertAlmostEqual(tax_free_balance.sum(), 102248124.22291529)

