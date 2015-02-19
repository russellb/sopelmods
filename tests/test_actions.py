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

    def _test_action(self, action):
        func = getattr(actions, action)
        func(tests.utils.Phenny(), '')
        if not hasattr(func, 'commands'):
            raise Exception('Missing commands attribute on function %s' %
                            action)
        self.assertTrue(action in func.commands)

    def test_table(self):
        self._test_action('table')

    def test_untable(self):
        self._test_action('untable')

    def test_raaage(self):
        self._test_action('raaage')

    def test_dapper(self):
        self._test_action('dapper')

    def test_smile(self):
        self._test_action('smile')

    def test_finger(self):
        self._test_action('finger')

    def test_umadbro(self):
        self._test_action('umadbro')

    def test_troll(self):
        self._test_action('troll')

    def test_trololo(self):
        self._test_action('trololo')

    def test_notbad(self):
        self._test_action('notbad')

    def test_dealwithit(self):
        self._test_action('dealwithit')

    def test_pirate(self):
        self._test_action('pirate')

    def test_glare(self):
        self._test_action('glare')

    def test_facepalm(self):
        self._test_action('facepalm')

    def test_tothemoon(self):
        self._test_action('tothemoon')

    def test_postal(self):
        self._test_action('postal')

    def test_ping(self):
        self._test_action('ping')

    def test_pong(self):
        self._test_action('pong')

    def test_hi(self):
        self._test_action('hi')

    def test_fail(self):
        self._test_action('fail')

    def test_boggle(self):
        self._test_action('boggle')

    def test_makeitrain(self):
        self._test_action('makeitrain')

    def test_failboat(self):
        self._test_action('failboat')

    def test_beerme(self):
        self._test_action('beerme')

    def test_halibut(self):
        self._test_action('halibut')
