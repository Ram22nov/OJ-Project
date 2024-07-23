from django.db import models
from django.contrib.auth.models import User

class Problem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    difficulty = models.CharField(max_length=50)
    input_data = models.TextField()  # Store the input data for the problem
    expected_output = models.TextField()  # Store the expected output for the problem
    
    def __str__(self):
        return self.title

