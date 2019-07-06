# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Positions(models.Model):
    cate_name = models.CharField(max_length=255)
    job_name = models.CharField(max_length=255)
    salary_range = models.CharField(max_length=255)
    working_city = models.CharField(max_length=255)
    experience_required = models.CharField(max_length=255, blank=True, null=True)
    education_required = models.CharField(max_length=255, blank=True, null=True)
    job_type = models.CharField(max_length=255)
    position_label = models.CharField(max_length=255, blank=True, null=True)
    publish_time = models.CharField(max_length=255)
    job_advantage = models.TextField(blank=True, null=True)
    job_detail = models.TextField()
    working_address = models.CharField(max_length=255)
    company_lagou_url = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_field = models.CharField(max_length=255)
    financing_status = models.CharField(max_length=255, blank=True, null=True)
    company_size = models.CharField(max_length=255, blank=True, null=True)
    company_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'positions'
        ordering = ["id"]