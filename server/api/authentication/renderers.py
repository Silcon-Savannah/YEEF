import json

from rest_framework.renderers import JSONRenderer


class UserJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        """
        If the view throws an error (such as the user can't be authenticated
        or something similar), `data` will contain an `errors` key. We want
        the default JSONRenderer to handle rendering errors, so we need to
        check for this case.
        """
        return json.dumps({
            'user': data
        })


class ProfileJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        """
        If the view throws an error (such as the user can't be authenticated
        or something similar), `data` will contain an `errors` key. We want
        the default JSONRenderer to handle rendering errors, so we need to
        check for this case.
        """
        return json.dumps({
            'profile': data
        })
