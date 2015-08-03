from rest_framework_jwt.views import ObtainJSONWebToken

from jtx_core.models.user import User


class ObtainJSONWebTokenWrapper(ObtainJSONWebToken):
    def post(self, request):
        """
        Get token
        ---
        parameters:
            - name: email
              required: true
              type: string
            - name: password
              required: true
              type: password
        """
        return super(ObtainJSONWebTokenWrapper, self).post(request)


obtain_jwt_token = ObtainJSONWebTokenWrapper.as_view()