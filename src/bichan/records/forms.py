from django import forms
from django.contrib.auth.models import User

from bichan.records.models import Record

class RecordForm(forms.ModelForm):
	class Meta:
		model = Record
		fields = ('name', 'value')
