from django import forms
from post.models import Topic
from django.core.exceptions import ValidationError


class TopicField(forms.Field):
    """
    自定义Field
    """
    default_error_messages = {
        "invalid": "Enter a whole number",
        "not_exist": "Model not exist",
    }

    def to_python(self, value):
        try:
            value = int(str(value).strip())
            return Topic.objects.get(pk=value)
        except (ValueError, TypeError):
            raise ValidationError(self.default_error_messages.get("invalid"), code="invalid")
        except Topic.DoesNotExist:
            raise ValidationError(self.default_error_messages.get("not_exist"), code="not_exist")