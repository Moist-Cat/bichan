from django.contrib import admin
from bichan.records.models import Record

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass
