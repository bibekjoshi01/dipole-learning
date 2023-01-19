from django.core.exceptions import ValidationError
from django.conf import settings
from django.core.files.images import get_image_dimensions

def validate_subject_icon(icon):
    if icon:
        if icon.size > (1024*1024):
            raise ValidationError("Image should be smaller than 1MB")
        w, h = get_image_dimensions(icon)
        if w != 200 and h != 200: 
            raise ValidationError("Image size should be 200 x 200")
    else:
        raise ValidationError("Invalid Image")
    




