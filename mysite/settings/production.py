from .base import *

# load database from the DATABASE_URL environment variable
#DATABASES = {}
DATABASES = {
	'default':{
    	'ENGINE': 'django.db.backends.postgresql_psycopg2',
    	'NAME': 'ruru'
    	'USER': ''
    	'PASSWORD': ''
    	'HOST': 
    	'PORT':
    }
} 

AWS_ACCESS_KEY_ID = 'AKIAJ24XDOQND6UTLKGA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'hellomuseum'
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False

# AWS cache settings, don't change unless you know what you're doing:
AWS_EXPIRY = 60 * 60 * 24 * 7

# See: https://github.com/jschneier/django-storages/issues/47
# Revert the following and use str after the above-mentioned bug is fixed in
# either django-storage-redux or boto

# URL that handles the media served from MEDIA_ROOT, used for managing
# stored files.
#  See:http://stackoverflow.com/questions/10390244/

AWS_S3_REGION_NAME = 'ap-northeast-2'
AWS_S3_SIGNATURE_VERSION = 's3v4'
AWS_S3_SECURE_URLS = True
AWS_S3_USE_SSL = True
AWS_IS_GZIPPED = True
from storages.backends.s3boto3 import S3Boto3Storage  # noqa
StaticRootS3BotoStorage = lambda: S3Boto3Storage(
    location='static',
    object_parameters={'CacheControl': 'max-age=%d' % AWS_EXPIRY}
)  # noqa
MediaRootS3BotoStorage = lambda: S3Boto3Storage(
    location='media',
    object_parameters={'CacheControl': 'max-age=%d' % AWS_EXPIRY}
)  # noqa

# Media
MEDIA_URL = 'https://{0}.s3.amazonaws.com/media/'.format(AWS_STORAGE_BUCKET_NAME)
DEFAULT_FILE_STORAGE = 'hellomuseum.settings.production.MediaRootS3BotoStorage'

# Static
STATIC_URL = 'https://{0}.s3.amazonaws.com/static/'.format(AWS_STORAGE_BUCKET_NAME)
STATICFILES_STORAGE = 'hellomuseum.settings.production.StaticRootS3BotoStorage'