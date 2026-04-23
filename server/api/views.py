from rest_framework import generics, viewsets, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response


class RootView(APIView):
    authentication_classes = [authentication.SessionAuthentication, authentication.BasicAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return Response({"message": "Welcome to the API root!"})
