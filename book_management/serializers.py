from rest_framework import serializers
from book_management.models import AppUser


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = AppUser
        fields = ['email', 'password', 'first_name']
        extr_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = AppUser(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            username=self.validated_data['email']
        )
        password = self.validated_data['password']
        user.set_password(password)
        user.save()
        return user


class LoginSerializer(serializers.ModelSerializer):
    """
    Class Name: LoginSerializer

    Description: Checking Username and Password.
    """

    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(required=True, allow_blank=False, write_only=True)

    class Meta:
        model = AppUser
        fields = ('email', 'password')
