from rest_framework import serializers
from .models import Project, Screenshot,ContactMessage,CV,ProfilePicture

class ScreenshotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screenshot
        fields = ['id', 'image','description']

class ProjectSerializer(serializers.ModelSerializer):
    screenshots = ScreenshotSerializer(many=True, read_only=True)
    image = serializers.ImageField(required=False)
    video = serializers.FileField(required=False)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'description', 'full_description',
            'tags', 'image', 'video', 'url', 'screenshots'
        ]

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['id', 'name', 'email', 'message', 'created_at']
        
class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = ['id', 'file', 'uploaded_at']
        
class ProfilePictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = ['image']