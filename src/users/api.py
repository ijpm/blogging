# -*- coding: utf-8 -*-
import json

from django.contrib.auth.models import User


from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import get_object_or_404, GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer, UserListSerializer


class UsersAPI(GenericAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

    def get(self, request):
        """
        Devuelve el listado de usuarios de la plataforma
        :param request:
        :return:
        """
        users = User.objects.all().values("id","username")
        page = self.paginate_queryset(users)
        serializer = UserListSerializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def post(self, request):
        """
        Crea un usuario
        :param request:
        :return:
        """
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetailAPI(APIView):
    """
    user detail
    """
    def get(self, request, pk):
        """
        devuelve el usuario solicitado
        :param request:
        :param pk:
        :return:
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        :param request:
        :param pk:
        :return:
        """
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, instance, pk):
        """
        borra un usuario
        :param instance:
        :return:
        """
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)