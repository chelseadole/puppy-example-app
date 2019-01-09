"""Testing for Landing Page of bpmninja."""

import unittest
from run import app


class StatusTests(unittest.TestCase):
    """Index test."""

    def setUp(self):
        """Setting up client and response for subsequent tests."""
        self.client = app.test_client()
        self.client.testing = True

    def test_index_200_okay(self):
        """Response code for '/'' landing page."""
        resp = self.client.get('/')
        assert resp.status_code == 200

    def test_pup_200_okay(self):
        """Response code for '/pup' random dog page."""
        resp = self.client.get('/pup')
        assert resp.status_code == 200
