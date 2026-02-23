from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Adicione campos personalizados ao token (payload) se desejar
        token['username'] = user.username
        token['groups'] = list(user.groups.values_list('name', flat=True))

        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        # Adicione informações do usuário na resposta do JSON
        data['user'] = {
            'id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'groups': list(self.user.groups.values_list('name', flat=True))
        }

        return data
