from django.db import models
from multipageform.models import MultipageModel

# Create your models here.

class JA(MultipageModel):
    # stage 1 fields
    first_name = models.CharField(max_length=20, blank=True)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    # stage 2 fields
    education_level = models.CharField(max_length=20, blank=True)
    year_graduated = models.CharField(max_length=4, blank=True)
    # stage 3 fields
    prior_company = models.CharField(max_length=20, blank=True)
    prior_experience = models.TextField(blank=True)
    anything_more = models.BooleanField(default=False)
    # stage 3b fields
    personal_statement = models.TextField(blank=True)
    # stage 4 fields
    all_is_accurate = models.BooleanField(default=False)
