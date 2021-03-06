"""
Configure Amazon s3 for storage in production
"""

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


# static files
class StaticStorage(S3Boto3Storage):
    """Set static file location"""
    location = settings.STATICFILES_LOCATION


# media files (option)
class MediaStorage(S3Boto3Storage):
    """Set media files location"""
    location = settings.MEDIAFILES_LOCATION
