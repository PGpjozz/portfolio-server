from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ScreenshotUploadView,ContactMessageView,CVUploadView,ProfilePictureAPIView

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/profile-picture/', ProfilePictureAPIView.as_view(), name='profile-picture'),
    path("contact/", ContactMessageView.as_view(), name="contact-message"),
    path("cv/", CVUploadView.as_view(), name="cv-upload"),
    path('projects/<int:project_id>/upload-screenshot/', ScreenshotUploadView.as_view(), name='upload-screenshot'),
]
