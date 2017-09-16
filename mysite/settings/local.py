from .base import *

MEDIA_URL = '/media/' #각 media 파일에 대한 URL Prefix
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') #업로드된 파일을 저장할 디렉토리 경로