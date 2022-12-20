import sys

from io import BytesIO
from PIL import Image

from django.core.files.uploadedfile import InMemoryUploadedFile


def create_tmp_img(field_name: str, name: str = 'test.png', content_type: str = 'PNG') -> InMemoryUploadedFile:
    file = BytesIO()
    image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
    image.save(file, 'png')
    file.name = name
    file.seek(0)
    return InMemoryUploadedFile(file, field_name, name, content_type, sys.getsizeof(file), None)
