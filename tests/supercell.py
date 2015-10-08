#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    05.10.2015 16:54:52 CEST
# File:    supercell.py

from common import *

class SupercellTestCase(SimpleModelTestCase):
    def test_periodic_zero(self):
        self.createH(0., 0.)

        supercell_model = self.model.supercell([1, 2, 1])
        res = array([[ 1.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j, -1.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  1.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  0.+0.j, -1.+0.j]])
        res_uc = None

        self.assertFullAlmostEqual(res, supercell_model.hamilton([0.1, 0.2, 0.7]))
        self.assertFullAlmostEqual(res_uc, supercell_model.uc)

    def test_periodic(self):
        self.createH(0.2, 0.3)

        supercell_model = self.model.supercell([1, 2, 3])
        res = array([[ 1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510-0.28531695j, -0.12840790+0.1284079j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.16180340+0.08244295j, -0.39270510+0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510-0.28531695j, -0.12840790+0.1284079j ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.16180340+0.08244295j, -0.39270510+0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510-0.28531695j, -0.12840790+0.1284079j ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.16180340+0.08244295j, -0.39270510+0.28531695j],
       [ 0.39270510+0.28531695j, -0.16180340-0.08244295j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [-0.12840790-0.1284079j , -0.39270510-0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510+0.28531695j, -0.16180340-0.08244295j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.12840790-0.1284079j , -0.39270510-0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510+0.28531695j, -0.16180340-0.08244295j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.12840790-0.1284079j , -0.39270510-0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ]])
        res_uc = None

        self.assertFullAlmostEqual(res, supercell_model.hamilton([0.1, 0.2, 0.7]))
        self.assertFullAlmostEqual(res_uc, supercell_model.uc)

    def test_non_periodic_1(self):
        self.createH(0.2, 0.3)

        supercell_model = self.model.supercell([1, 2, 3], periodic=[True, True, False])
        res = array([[ 1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510-0.28531695j, -0.12840790+0.1284079j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.16180340+0.08244295j, -0.39270510+0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510-0.28531695j, -0.12840790+0.1284079j ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.16180340+0.08244295j, -0.39270510+0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510-0.28531695j, -0.12840790+0.1284079j ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.16180340+0.08244295j, -0.39270510+0.28531695j],
       [ 0.39270510+0.28531695j, -0.16180340-0.08244295j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [-0.12840790-0.1284079j , -0.39270510-0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510+0.28531695j, -0.16180340-0.08244295j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.12840790-0.1284079j , -0.39270510-0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510+0.28531695j, -0.16180340-0.08244295j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.12840790-0.1284079j , -0.39270510-0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ]])
        res_uc = None

        self.assertFullAlmostEqual(res, supercell_model.hamilton([0.1, 0.2, 0.7]))
        self.assertFullAlmostEqual(res_uc, supercell_model.uc)

    def test_non_periodic_2(self):
        self.createH(0.2, 0.3)

        supercell_model = self.model.supercell([1, 2, 3], periodic=[True, False, True])
        res = array([[ 1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.30000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.16180340+0.08244295j, -0.30000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.30000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.16180340+0.08244295j, -0.30000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.30000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.16180340+0.08244295j, -0.30000000+0.j        ],
       [ 0.30000000+0.j        , -0.16180340-0.08244295j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.30000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.30000000+0.j        , -0.16180340-0.08244295j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        , -0.30000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.30000000+0.j        , -0.16180340-0.08244295j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  0.31755705+0.1618034j ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        , -0.30000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.31755705-0.1618034j , -1.48541020+0.j        ]])
        res_uc = None

        self.assertFullAlmostEqual(res, supercell_model.hamilton([0.1, 0.2, 0.7]))
        self.assertFullAlmostEqual(res_uc, supercell_model.uc)

    def test_non_periodic_3(self):
        self.createH(0.2, 0.3)

        supercell_model = self.model.supercell([1, 2, 3], periodic=[False, True, True])
        res = array([[ 1.0000000+0.j        ,  0.2000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.3927051-0.28531695j, -0.1902113-0.0618034j ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ],
       [ 0.2000000+0.j        , -1.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.2j       , -0.3927051+0.28531695j,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ],
       [ 0.0000000+0.j        ,  0.0000000+0.j        ,
         1.0000000+0.j        ,  0.2000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.3927051-0.28531695j, -0.1902113-0.0618034j ,
         0.0000000+0.j        ,  0.0000000+0.j        ],
       [ 0.0000000+0.j        ,  0.0000000+0.j        ,
         0.2000000+0.j        , -1.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.2j       , -0.3927051+0.28531695j,
         0.0000000+0.j        ,  0.0000000+0.j        ],
       [ 0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         1.0000000+0.j        ,  0.2000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.3927051-0.28531695j, -0.1902113-0.0618034j ],
       [ 0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.2000000+0.j        , -1.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.2j       , -0.3927051+0.28531695j],
       [ 0.3927051+0.28531695j,  0.0000000-0.2j       ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         1.0000000+0.j        ,  0.2000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ],
       [-0.1902113+0.0618034j , -0.3927051-0.28531695j,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.2000000+0.j        , -1.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ],
       [ 0.0000000+0.j        ,  0.0000000+0.j        ,
         0.3927051+0.28531695j,  0.0000000-0.2j       ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         1.0000000+0.j        ,  0.2000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ],
       [ 0.0000000+0.j        ,  0.0000000+0.j        ,
        -0.1902113+0.0618034j , -0.3927051-0.28531695j,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.2000000+0.j        , -1.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ],
       [ 0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.3927051+0.28531695j,  0.0000000-0.2j       ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         1.0000000+0.j        ,  0.2000000+0.j        ],
       [ 0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
        -0.1902113+0.0618034j , -0.3927051-0.28531695j,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.0000000+0.j        ,  0.0000000+0.j        ,
         0.2000000+0.j        , -1.0000000+0.j        ]])
        res_uc = None

        self.assertFullAlmostEqual(res, supercell_model.hamilton([0.1, 0.2, 0.7]))
        self.assertFullAlmostEqual(res_uc, supercell_model.uc)

    def test_non_periodic_4(self):
        self.createH(0.9, 0.3)

        supercell_model = self.model.supercell([1, 2, 3], periodic=[False, False, True])
        res = array([[ 1.0+0.j ,  0.9+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,
         0.3+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.9+0.j , -1.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,
         0.0+0.9j, -0.3+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  1.0+0.j ,  0.9+0.j ,  0.0+0.j ,  0.0+0.j ,
         0.0+0.j ,  0.0+0.j ,  0.3+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  0.9+0.j , -1.0+0.j ,  0.0+0.j ,  0.0+0.j ,
         0.0+0.j ,  0.0+0.j ,  0.0+0.9j, -0.3+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  1.0+0.j ,  0.9+0.j ,
         0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.3+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.9+0.j , -1.0+0.j ,
         0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.9j, -0.3+0.j ],
       [ 0.3+0.j ,  0.0-0.9j,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,
         1.0+0.j ,  0.9+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j , -0.3+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,
         0.9+0.j , -1.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  0.3+0.j ,  0.0-0.9j,  0.0+0.j ,  0.0+0.j ,
         0.0+0.j ,  0.0+0.j ,  1.0+0.j ,  0.9+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  0.0+0.j , -0.3+0.j ,  0.0+0.j ,  0.0+0.j ,
         0.0+0.j ,  0.0+0.j ,  0.9+0.j , -1.0+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.3+0.j ,  0.0-0.9j,
         0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  1.0+0.j ,  0.9+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j , -0.3+0.j ,
         0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.9+0.j , -1.0+0.j ]])
        res_uc = None

        self.assertFullAlmostEqual(res, supercell_model.hamilton([0.1, 0.2, 0.7]))
        self.assertFullAlmostEqual(res_uc, supercell_model.uc)

    def test_non_periodic_5(self):
        self.createH(0.9, 0.3)

        supercell_model = self.model.supercell([1, 2, 3], periodic=[False, True, False])
        res = array([[ 1.00000000+0.j        ,  0.90000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510-0.28531695j, -0.85595086-0.27811529j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.90000000+0.j        , -1.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.9j       , -0.39270510+0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         1.00000000+0.j        ,  0.90000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510-0.28531695j, -0.85595086-0.27811529j,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.90000000+0.j        , -1.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.9j       , -0.39270510+0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.00000000+0.j        ,  0.90000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510-0.28531695j, -0.85595086-0.27811529j],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.90000000+0.j        , -1.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.9j       , -0.39270510+0.28531695j],
       [ 0.39270510+0.28531695j,  0.00000000-0.9j       ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.00000000+0.j        ,  0.90000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [-0.85595086+0.27811529j, -0.39270510-0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.90000000+0.j        , -1.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510+0.28531695j,  0.00000000-0.9j       ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.00000000+0.j        ,  0.90000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.85595086+0.27811529j, -0.39270510-0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.90000000+0.j        , -1.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.39270510+0.28531695j,  0.00000000-0.9j       ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.00000000+0.j        ,  0.90000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.85595086+0.27811529j, -0.39270510-0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.90000000+0.j        , -1.00000000+0.j        ]])
        res_uc = None

        self.assertFullAlmostEqual(res, supercell_model.hamilton([0.1, 0.2, 0.7]))
        self.assertFullAlmostEqual(res_uc, supercell_model.uc)

    def test_non_periodic_6(self):
        self.createH(0.9, 0.3)

        supercell_model = self.model.supercell([1, 2, 3], periodic=[True, False, False])
        res = array([[ 1.48541020+0.j        ,  1.42900673+0.72811529j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.30000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 1.42900673-0.72811529j, -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.72811529+0.37099327j, -0.30000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  1.42900673+0.72811529j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.30000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         1.42900673-0.72811529j, -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.72811529+0.37099327j, -0.30000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  1.42900673+0.72811529j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.30000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.42900673-0.72811529j, -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.72811529+0.37099327j, -0.30000000+0.j        ],
       [ 0.30000000+0.j        , -0.72811529-0.37099327j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  1.42900673+0.72811529j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        , -0.30000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.42900673-0.72811529j, -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.30000000+0.j        , -0.72811529-0.37099327j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  1.42900673+0.72811529j,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        , -0.30000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.42900673-0.72811529j, -1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.30000000+0.j        , -0.72811529-0.37099327j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.48541020+0.j        ,  1.42900673+0.72811529j],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        , -0.30000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.42900673-0.72811529j, -1.48541020+0.j        ]])
        res_uc = None

        self.assertFullAlmostEqual(res, supercell_model.hamilton([0.1, 0.2, 0.7]))
        self.assertFullAlmostEqual(res_uc, supercell_model.uc)

    def test_non_periodic_7(self):
        self.createH(0.1, -0.3)

        supercell_model = self.model.supercell([1, 2, 3], periodic=[False, False, False])
        res = array([[ 1.0+0.j ,  0.1+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,
        -0.3+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.1+0.j , -1.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,
         0.0+0.1j,  0.3+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  1.0+0.j ,  0.1+0.j ,  0.0+0.j ,  0.0+0.j ,
         0.0+0.j ,  0.0+0.j , -0.3+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  0.1+0.j , -1.0+0.j ,  0.0+0.j ,  0.0+0.j ,
         0.0+0.j ,  0.0+0.j ,  0.0+0.1j,  0.3+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  1.0+0.j ,  0.1+0.j ,
         0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j , -0.3+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.1+0.j , -1.0+0.j ,
         0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.1j,  0.3+0.j ],
       [-0.3+0.j ,  0.0-0.1j,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,
         1.0+0.j ,  0.1+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.3+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,
         0.1+0.j , -1.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j , -0.3+0.j ,  0.0-0.1j,  0.0+0.j ,  0.0+0.j ,
         0.0+0.j ,  0.0+0.j ,  1.0+0.j ,  0.1+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.3+0.j ,  0.0+0.j ,  0.0+0.j ,
         0.0+0.j ,  0.0+0.j ,  0.1+0.j , -1.0+0.j ,  0.0+0.j ,  0.0+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j , -0.3+0.j ,  0.0-0.1j,
         0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  1.0+0.j ,  0.1+0.j ],
       [ 0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.3+0.j ,
         0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.0+0.j ,  0.1+0.j , -1.0+0.j ]])
        res_uc = None

        self.assertFullAlmostEqual(res, supercell_model.hamilton([0.1, 0.2, 0.7]))
        self.assertFullAlmostEqual(res_uc, supercell_model.uc)

    def test_passivation_1(self):
        self.createH(0.1, -0.3)

        supercell_model = self.model.supercell([1, 2, 3], passivation = lambda x, y, z: ([1., 2.] if x else None))
        res = array([[ 1.51458980+0.j        ,  0.15877853+0.0809017j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.39270510+0.28531695j, -0.06420395+0.06420395j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.15877853-0.0809017j ,  1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.08090170+0.04122147j,  0.39270510-0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         1.51458980+0.j        ,  0.15877853+0.0809017j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.39270510+0.28531695j, -0.06420395+0.06420395j,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.15877853-0.0809017j ,  1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.08090170+0.04122147j,  0.39270510-0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.51458980+0.j        ,  0.15877853+0.0809017j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.39270510+0.28531695j, -0.06420395+0.06420395j],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.15877853-0.0809017j ,  1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.08090170+0.04122147j,  0.39270510-0.28531695j],
       [-0.39270510-0.28531695j, -0.08090170-0.04122147j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.51458980+0.j        ,  0.15877853+0.0809017j ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [-0.06420395-0.06420395j,  0.39270510+0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.15877853-0.0809017j ,  1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.39270510-0.28531695j, -0.08090170-0.04122147j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.51458980+0.j        ,  0.15877853+0.0809017j ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.06420395-0.06420395j,  0.39270510+0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.15877853-0.0809017j ,  1.48541020+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.39270510-0.28531695j, -0.08090170-0.04122147j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         1.51458980+0.j        ,  0.15877853+0.0809017j ],
       [ 0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
        -0.06420395-0.06420395j,  0.39270510+0.28531695j,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.00000000+0.j        ,  0.00000000+0.j        ,
         0.15877853-0.0809017j ,  1.48541020+0.j        ]])
        res_uc = None

        self.assertFullAlmostEqual(res, supercell_model.hamilton([0.1, 0.2, 0.7]))
        self.assertFullAlmostEqual(res_uc, supercell_model.uc)

    def test_passivation_2(self):
        self.createH(0., 0.)

        supercell_model = self.model.supercell([1, 2, 3], passivation = lambda x, y, z: ([1., -2.] if (y and z) else None))
        res = array([[ 2.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,
         0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j, -3.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,
         0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  2.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,
         0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  0.+0.j, -3.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,
         0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  2.+0.j,  0.+0.j,  0.+0.j,
         0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j, -3.+0.j,  0.+0.j,
         0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  2.+0.j,
         0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,
        -3.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,
         0.+0.j,  2.+0.j,  0.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,
         0.+0.j,  0.+0.j, -3.+0.j,  0.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,
         0.+0.j,  0.+0.j,  0.+0.j,  2.+0.j,  0.+0.j],
       [ 0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j,
         0.+0.j,  0.+0.j,  0.+0.j,  0.+0.j, -3.+0.j]])
        res_uc = None

        self.assertFullAlmostEqual(res, supercell_model.hamilton([0.1, 0.2, 0.7]))
        self.assertFullAlmostEqual(res_uc, supercell_model.uc)

if __name__ == "__main__":
    unittest.main()