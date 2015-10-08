#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    05.10.2015 16:54:52 CEST
# File:    change_uc.py

from common import *

import numpy as np

class HrPrintTestCase(SimpleModelTestCase):
    def test0(self):
        self.createH(0.1, 0.211)
        res = ' created by the TBModels package    Wed, 07 Oct 2015 15:26:43 CEST\n           3\n           7\n    1    1    1    1    1    1    1\n   -1   -1    0    1    1    0.000000    0.000000\n   -1   -1    0    2    1    0.000000    0.000000\n   -1   -1    0    3    1    0.000000    0.000000\n   -1   -1    0    1    2   -0.100000    0.000000\n   -1   -1    0    2    2    0.000000    0.000000\n   -1   -1    0    3    2    0.000000    0.000000\n   -1   -1    0    1    3    0.000000    0.000000\n   -1   -1    0    2    3    0.000000    0.000000\n   -1   -1    0    3    3    0.000000    0.000000\n   -1    0    0    1    1    0.211000    0.000000\n   -1    0    0    2    1    0.000000    0.000000\n   -1    0    0    3    1    0.000000    0.000000\n   -1    0    0    1    2    0.000000    0.100000\n   -1    0    0    2    2   -0.211000    0.000000\n   -1    0    0    3    2    0.000000    0.000000\n   -1    0    0    1    3    0.000000    0.000000\n   -1    0    0    2    3    0.000000    0.000000\n   -1    0    0    3    3    0.000000    0.000000\n    0   -1    0    1    1    0.211000    0.000000\n    0   -1    0    2    1    0.000000    0.000000\n    0   -1    0    3    1    0.000000    0.000000\n    0   -1    0    1    2    0.000000   -0.100000\n    0   -1    0    2    2   -0.211000    0.000000\n    0   -1    0    3    2    0.000000    0.000000\n    0   -1    0    1    3    0.000000    0.000000\n    0   -1    0    2    3    0.000000    0.000000\n    0   -1    0    3    3    0.000000    0.000000\n    0    0    0    1    1    1.000000    0.000000\n    0    0    0    2    1    0.100000    0.000000\n    0    0    0    3    1    0.000000    0.000000\n    0    0    0    1    2    0.100000    0.000000\n    0    0    0    2    2   -1.000000    0.000000\n    0    0    0    3    2    0.000000    0.000000\n    0    0    0    1    3    0.000000    0.000000\n    0    0    0    2    3    0.000000    0.000000\n    0    0    0    3    3    0.000000    0.000000\n    0    1    0    1    1    0.211000    0.000000\n    0    1    0    2    1    0.000000    0.100000\n    0    1    0    3    1    0.000000    0.000000\n    0    1    0    1    2    0.000000    0.000000\n    0    1    0    2    2   -0.211000    0.000000\n    0    1    0    3    2    0.000000    0.000000\n    0    1    0    1    3    0.000000    0.000000\n    0    1    0    2    3    0.000000    0.000000\n    0    1    0    3    3    0.000000    0.000000\n    1    0    0    1    1    0.211000    0.000000\n    1    0    0    2    1    0.000000   -0.100000\n    1    0    0    3    1    0.000000    0.000000\n    1    0    0    1    2    0.000000    0.000000\n    1    0    0    2    2   -0.211000    0.000000\n    1    0    0    3    2    0.000000    0.000000\n    1    0    0    1    3    0.000000    0.000000\n    1    0    0    2    3    0.000000    0.000000\n    1    0    0    3    3    0.000000    0.000000\n    1    1    0    1    1    0.000000    0.000000\n    1    1    0    2    1   -0.100000    0.000000\n    1    1    0    3    1    0.000000    0.000000\n    1    1    0    1    2    0.000000    0.000000\n    1    1    0    2    2    0.000000    0.000000\n    1    1    0    3    2    0.000000    0.000000\n    1    1    0    1    3    0.000000    0.000000\n    1    1    0    2    3    0.000000    0.000000\n    1    1    0    3    3    0.000000    0.000000'
        self.assertFullEqual(res.split('\n')[1:], self.model.to_hr().split('\n')[1:])
    

if __name__ == "__main__":
    unittest.main()