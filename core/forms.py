from django.forms import *
from .models import *

class DocForm(ModelForm):

    class Meta:
        model = Document
        fields = '__all__'