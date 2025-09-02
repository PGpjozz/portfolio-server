# views.py

from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import Project, Screenshot,ContactMessage,CV,ProfilePicture
from .serializers import ScreenshotSerializer,ProjectSerializer,ContactMessageSerializer,CVSerializer,ProfilePictureSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from django.conf import settings

class ScreenshotUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, project_id):
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

        image = request.FILES.get('image')
        if not image:
            return Response({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)

        screenshot = Screenshot.objects.create(project=project, image=image)
        serializer = ScreenshotSerializer(screenshot)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
class ContactMessageView(APIView):
    def post(self, request):
        serializer = ContactMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Message saved successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CVUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = CVSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        cv = CV.objects.last()
        serializer = CVSerializer(cv)
        return Response(serializer.data)
    
class ProfilePictureAPIView(APIView):
    def get(self, request):
        pic = ProfilePicture.objects.last()  # always fetch the latest
        serializer = ProfilePictureSerializer(pic)
        return Response(serializer.data)