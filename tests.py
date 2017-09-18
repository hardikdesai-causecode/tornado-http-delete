import handlers
from tornado.testing import AsyncHTTPTestCase
import json
import unittest

# Your TestHandler class
# They are runnable via nosetests as well.
class TestHandler(AsyncHTTPTestCase):
    def get_app(self):
        return handlers.make_app()

    def test_post_request(self):
        # Example on how to hit a particular handler as POST request.
        # In this example, we want to test the response code,
        post_args = {'name': 'Hardik', 'age': '22'}
        response = self.fetch(
            '/',
            method='POST',
            body=json.dumps(post_args).encode('utf-8'),
            follow_redirects=True)

        self.assertEqual(response.code, 200)

    def test_put_request(self):
        # Example on how to hit a particular handler as PUT request.
        # In this example, we want to test the response code,
        post_args = {'name': 'Hardik', 'age': '22'}
        response = self.fetch(
            '/',
            method='PUT',
            body=json.dumps(post_args).encode('utf-8'),
            follow_redirects=True)

        self.assertEqual(response.code, 200)

    def test_delete_request(self):
        # Example on how to hit a particular handler as DELETE request.
        # In this example, we want to test the redirect,
        post_args = {'name': 'Hardik', 'age': '22'}
        response = self.fetch(
            '/',
            method='DELETE',
            body=json.dumps(post_args).encode('utf-8'),
            follow_redirects=True)

        self.assertEqual(response.code, 200)

class TestOrg(AsyncHTTPTestCase):
    def get_app(self):
        return handlers.make_app()

    def test_get_request(self):
        response = self.fetch(
            '/uid/{}/org/'.format('12345'),
            method='GET',
            follow_redirects=True)

        self.assertEqual(response.code, 200)

    def test_delete_request(self):
        response = self.fetch(
            '/uid/{}/org/{}'.format('12345','54321'),
            method='DELETE',
            follow_redirects=True)

        self.assertEqual(response.code, 200)


if __name__ == "__main__":
    unittest.main()