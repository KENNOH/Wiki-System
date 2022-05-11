from django.test import Client
from django.urls import reverse
from django.contrib.auth.models import Group, User
import pytest



@pytest.mark.django_db
def test_my_user():
    me = User.objects.get(username='admin@gmail.com')
    assert me.is_superuser