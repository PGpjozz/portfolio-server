from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()  # short description
    full_description = models.TextField(blank=True)
    tags = models.CharField(max_length=200, blank=True)

    image = models.ImageField(upload_to='project_images/', blank=True)  # Main image upload
    video = models.FileField(upload_to='project_videos/', blank=True)  # Short video upload
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Screenshot(models.Model):
    project = models.ForeignKey(Project, related_name='screenshots', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_screenshots/')
    description = models.TextField()
    def __str__(self):
        return f"Screenshot for {self.project.title}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
    
class CV(models.Model):
    file = models.FileField(upload_to='cv/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class ProfilePicture(models.Model):
    image = models.ImageField(upload_to='profile_pictures/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Profile Picture {self.id}"