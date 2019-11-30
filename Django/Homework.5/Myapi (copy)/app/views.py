from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.core.files import File


class Student(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        f = open('document', 'r')
        return Response(File(f))
    def post(self,request):
        d = open('document', 'w')
        return Response(File(d))


