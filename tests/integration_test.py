#!/usr/bin/env python

import base64
import mock

from mcfire import mcfire

from unittest import TestCase


# from mock import patch


__author__ = 'iokulist'


class TestMakeRequestWithToken(TestCase):
    maxDiff = None

    # @mock.patch('get_ipython', side_effect=get_ipython_xxx)
    def test_subtract(self, *args, **kvargs):
        balance, amount = mcfire.subtract_with_remainder(100, 125)

        self.assertEqual(balance, 0)
        self.assertEqual(amount, 25)
