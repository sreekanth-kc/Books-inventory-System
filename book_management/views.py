from book_management.serializers import RegistrationSerializer, LoginSerializer
from rest_framework.views import APIView
from utils.mixins import HttpResponseMixin
from book_management.models import AppUser, Book
from utils.user_utils import get_token
from rest_framework.permissions import IsAuthenticated


class Registration_view(APIView, HttpResponseMixin):
    """

    """

    def post(self, request):
        """

        :param request:
        :return:
        """

        if request.method == 'POST':
            try:
                serializer = RegistrationSerializer(data=request.data)
                data = {}
                if serializer.is_valid():
                    account = serializer.save()
                    data['email'] = account.email
                    data['name'] = account.first_name
                else:
                    data = serializer.errors
                    return self.error_response(code='HTTP_400_BAD_REQUEST', message=data)
                return self.success_response(data=data, code='HTTP_200_OK', message="Success")
            except Exception as e:
                return self.error_response(code='HTTP_400_BAD_REQUEST', message=str(e))


class Login_View(APIView, HttpResponseMixin):
    permission_classes = (IsAuthenticated,)
    """

    """

    def post(self, request):
        """

        :param request:
        :return:
        """
        if request.method == 'POST':
            try:
                email = request.data['email'].lower()
                password = request.data['password']
                serializer = LoginSerializer(data=request.data)
                if serializer.is_valid():
                    user = AppUser.objects.get(email=email)

                    print("Token", get_token(user).key)
                    if user:
                        valid = user.check_password(password)
                        if valid:
                            return self.success_response(data={"token": get_token(user).key}, code='HTTP_200_OK', message="Success")
                        else:
                            return self.error_response(code='HTTP_400_BAD_REQUEST', message="Invalid password")
                    else:
                        return self.error_response(code='HTTP_400_BAD_REQUEST', message="Unknown user")

            except Exception as e:
                return self.error_response(code='HTTP_400_BAD_REQUEST', message=str(e))


class BorrowBook(APIView, HttpResponseMixin):
    permission_classes = (IsAuthenticated,)
    """

    """

    def post(self, request):
        """

        :param request:
        :return:
        """
        if request.method == 'POST':
            print(request.user)
            try:
                book_id = request.data['book_id']
                email = request.data['email'].lower()
                password = request.data['password']
                serializer = LoginSerializer(data=request.data)
                if serializer.is_valid():
                    user = AppUser.objects.get(email=email)
                    if user:
                        valid = user.check_password(password)
                        if valid:
                            return self.success_response(data="data", code='HTTP_200_OK', message="Success")
                        else:
                            return self.error_response(code='HTTP_400_BAD_REQUEST', message="Invalid password")
                    else:
                        return self.error_response(code='HTTP_400_BAD_REQUEST', message="Unknown user")

            except Exception as e:
                return self.error_response(code='HTTP_400_BAD_REQUEST', message=str(e))
