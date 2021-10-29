from django.contrib import admin
from .models import User, Cruiser, History
from import_export.admin import ImportExportModelAdmin


@admin.register(User, Cruiser, History)
class ViewAdmin(ImportExportModelAdmin):
    pass

# admin.site.register(User)
# admin.site.register(Cruiser)
# admin.site.register(History)
