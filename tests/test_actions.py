# Copyright (C) 2013 - Russell Bryant
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import unittest

import actions
import tests.utils


class ActionsTestCase(unittest.TestCase):
    # Make sure actions don't blow up

    def test_table(self):
        actions.table(tests.utils.Phenny(), '')

    def test_untable(self):
        actions.untable(tests.utils.Phenny(), '')

    def test_dapper(self):
        actions.dapper(tests.utils.Phenny(), '')

    def test_joyful(self):
        actions.joyful(tests.utils.Phenny(), '')

    def test_finger(self):
        actions.finger(tests.utils.Phenny(), '')

    def test_umadbro(self):
        actions.umadbro(tests.utils.Phenny(), '')

    def test_troll(self):
        actions.troll(tests.utils.Phenny(), '')

    def test_trololo(self):
        actions.trololo(tests.utils.Phenny(), '')

    def test_notbad(self):
        actions.notbad(tests.utils.Phenny(), '')

    def test_dealwithit(self):
        actions.dealwithit(tests.utils.Phenny(), '')

    def test_glare(self):
        actions.glare(tests.utils.Phenny(), '')

    def test_facepalm(self):
        actions.facepalm(tests.utils.Phenny(), '')

    def test_tothemoon(self):
        actions.tothemoon(tests.utils.Phenny(), '')

    def test_postal(self):
        actions.postal(tests.utils.Phenny(), '')
