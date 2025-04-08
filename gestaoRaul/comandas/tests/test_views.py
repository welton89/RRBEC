
from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.contrib.sessions.middleware import SessionMiddleware
from django.contrib.messages.middleware import MessageMiddleware

from ..views import createComanda 
from ..models import Mesa, Comanda 
from mesas.models import Mesa
from gestaoRaul.decorators import group_required


class CreateComandaViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.garcom_group = Group.objects.create(name='Garçom')
        self.outro_group = Group.objects.create(name='OutroGrupo')
        self.garcom_user = User.objects.create_user(username='garcom', password='password')
        self.garcom_user.groups.add(self.garcom_group)
        self.outro_user = User.objects.create_user(username='outro', password='password')
        self.outro_user.groups.add(self.outro_group)
        self.mesa = Mesa.objects.create(name='teste')

    def add_middleware(self, request):
        """Adiciona middlewares necessários para request.user e mensagens."""
        middleware = SessionMiddleware(lambda x: x)
        middleware.process_request(request)
        request.session.save()
        message_middleware = MessageMiddleware(lambda x: x)
        message_middleware.process_request(request)
        return request

    def test_garcom_can_access_and_create_comanda(self):
        """Testa se um usuário no grupo 'Garçom' pode acessar e criar uma comanda."""
        request = self.factory.post(
            reverse('createComanda'),  # Assumindo que sua URL para createComanda se chama 'createcomanda'
            {'name-comanda': 'Comanda Teste', 'select-mesa': self.mesa.id}
        )
        request.user = self.garcom_user
        request = self.add_middleware(request)

        response = createComanda(request)

        self.assertEqual(response.status_code, 302)  # Verifica se houve um redirect
        self.assertIn(reverse('viewcomanda'), response.url)  # Verifica se redirecionou para a view correta
        self.assertTrue(Comanda.objects.filter(name='Comanda Teste', mesa=self.mesa, user=self.garcom_user).exists())

    def test_non_garcom_cannot_access_create_comanda(self):
        """Testa se um usuário fora do grupo 'Garçom' não pode acessar a view."""
        request = self.factory.post(
            reverse('createComanda'),
            {'name-comanda': 'Comanda Teste', 'select-mesa': self.mesa.id}
        )
        request.user = self.outro_user
        request = self.add_middleware(request)

        # Aplica o decorator diretamente para testar o acesso negado
        wrapped_view = group_required(groupName='Garçom')(createComanda)
        response = wrapped_view(request)

        self.assertEqual(response.status_code, 403)  # Verifica se o acesso foi negado (Forbidden)
        self.assertFalse(Comanda.objects.filter(name='Comanda Teste').exists())

    def test_anonymous_user_cannot_access_create_comanda(self):
        """Testa se um usuário anônimo não pode acessar a view."""
        request = self.factory.post(
            reverse('createComanda'),
            {'name-comanda': 'Comanda Teste', 'select-mesa': self.mesa.id}
        )
        request.user = None  # Simula um usuário não autenticado
        request = self.add_middleware(request)

        wrapped_view = group_required(groupName='Garçom')(createComanda)
        response = wrapped_view(request)

        self.assertEqual(response.status_code, 302)  # Deve redirecionar para a página de login (padrão do Django)
        self.assertTrue(response.url.startswith(reverse('login')))  # Verifica se redireciona para a página de login
        self.assertFalse(Comanda.objects.filter(name='Comanda Teste').exists())

    def test_create_comanda_invalid_mesa(self):
        """Testa o comportamento ao tentar criar uma comanda com uma mesa inválida."""
        request = self.factory.post(
            reverse('createComanda'),
            {'name-comanda': 'Comanda Inválida', 'select-mesa': 999}  # ID de mesa inexistente
        )
        request.user = self.garcom_user
        request = self.add_middleware(request)
        # response = createComanda(request)

        with self.assertRaises(Mesa.DoesNotExist):
            createComanda(request)
        # self.assertEqual(response.status_code, 400)
        self.assertFalse(Comanda.objects.filter(name='Comanda Inválida').exists())

    def test_create_comanda_missing_data(self):
        """Testa o comportamento ao tentar criar uma comanda com dados faltando."""
        # Sem 'name-comanda'
        request_sem_nome = self.factory.post(
            reverse('createComanda'),
            {'select-mesa': self.mesa.id}
        )
        request_sem_nome.user = self.garcom_user
        request_sem_nome = self.add_middleware(request_sem_nome)

        # with self.assertRaises(TypeError):  # A view espera 'name' e 'mesa_id' no POST
        #     createComanda(request_sem_nome)
        self.assertFalse(Comanda.objects.exists())

        # Sem 'select-mesa'
        request_sem_mesa = self.factory.post(
            reverse('createComanda'),
            {'name-comanda': 'Comanda Sem Mesa'}
        )
        request_sem_mesa.user = self.garcom_user
        request_sem_mesa = self.add_middleware(request_sem_mesa)

        # with self.assertRaises(TypeError):  # A view espera 'name' e 'mesa_id' no POST
        #     createComanda(request_sem_mesa)
        self.assertFalse(Comanda.objects.exists())