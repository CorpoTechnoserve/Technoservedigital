from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Contact)
admin.site.register(HrCorner)
admin.site.register(AskQuery)
admin.site.register(SoftwareDevelopment)
# @admin.register(StudentCorner)
# class StudentCorner(ImportExportModelAdmin):
#     pass

# @admin.register(HrCorner)
# class HrCorner(ImportExportModelAdmin):
#     pass

# @admin.register(Contact)
# class Contact(ImportExportModelAdmin):
#     pass

# @admin.register(AskQuery)
# class AskQuery(ImportExportModelAdmin):
#     pass

# @admin.register(SoftwareDevelopment)
# class SoftwareDevelopment(ImportExportModelAdmin):
#     pass




