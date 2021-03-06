# -*- coding: utf-8 -*-

"""Tests for simple views which render templates."""

from django.test import TestCase


PLAIN_RESPONSE = 'Hello, World!'
CONTEXT_RESPONSE = 'a = 1; b = 2'
REQ_CONTEXT_RESPONSE = 'user.is_anonymous() => True'
NOT_FOUND_RESPONSE = 'NOT FOUND: /this/does/not/exist/'
SERVER_ERROR_RESPONSE = 'ERROR OCCURRED.'


class SimpleTest(TestCase):
    
    def test_plain(self):
        response = self.client.get('/simple/plain/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, PLAIN_RESPONSE)
    
    def test_context(self):
        response = self.client.get('/simple/context/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, CONTEXT_RESPONSE)
    
    def test_req_context(self):
        response = self.client.get('/simple/req_context/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, REQ_CONTEXT_RESPONSE)
    
    def test_404(self):
        response = self.client.get('/this/does/not/exist/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.content, NOT_FOUND_RESPONSE)
