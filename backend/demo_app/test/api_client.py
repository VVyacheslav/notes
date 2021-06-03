import json
import random
import string
from collections.abc import Iterable

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from users.tests.factories import UserFactory


class DRFClient(APIClient):
    def __init__(self, user=None, god_mode=True, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.god_mode = god_mode
        self.user = user or self._create_user()
        self.auth()

    def auth(self):
        if self.user.is_anonymous:
            return

        token = Token.objects.create(user=self.user)
        self.credentials(
            HTTP_AUTHORIZATION=f'Token {token}',
            HTTP_X_CLIENT='testing',
        )

    def _create_user(self):
        user_opts = {'username': 'chuck'}
        if self.god_mode:
            user_opts.update({
                'is_staff': True,
                'is_superuser': True,
            })
        user = UserFactory(**user_opts)
        self.password = ''.join([random.choice(string.hexdigits) for _ in range(0, 6)])
        user.set_password(self.password)
        user.save()
        return user

    def logout(self):
        self.credentials()
        super().logout()

    def get(self, *args, **kwargs):
        return self._api_call('get', kwargs.get('expected_status_code', 200), *args, **kwargs)

    def post(self, *args, **kwargs):
        return self._api_call('post', kwargs.get('expected_status_code', 201), *args, **kwargs)

    def put(self, *args, **kwargs):
        return self._api_call('put', kwargs.get('expected_status_code', 200), *args, **kwargs)

    def patch(self, *args, **kwargs):
        return self._api_call('patch', kwargs.get('expected_status_code', 200), *args, **kwargs)

    def delete(self, *args, **kwargs):
        return self._api_call('delete', kwargs.get('expected_status_code', 204), *args, **kwargs)

    def _api_call(self, method, expected, *args, **kwargs):
        kwargs['format'] = kwargs.get('format', 'json')  # by default submit all data in JSON
        as_response = kwargs.pop('as_response', False)

        method = getattr(super(), method)
        response = method(*args, **kwargs)

        if as_response:
            return response

        content = self._decode(response)
        actual_status_code = response.status_code

        if not isinstance(expected, Iterable):
            expected = [expected]

        assert actual_status_code in expected, (
            f'Status code should be one of {expected}, but received {actual_status_code}.\n'
            f'Content:\n{content}'
        )

        return content

    def _decode(self, response):
        if not response.content:
            return

        content = response.content.decode('utf-8', errors='ignore')
        if 'application/json' in response.headers['content-type']:
            return json.loads(content)
        else:
            return content
