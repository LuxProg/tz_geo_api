from django.contrib import admin
from .models import TblAzs, TblRoads

admin.site.register(TblAzs)
admin.site.register(TblRoads)

# доступ к админке admin:admin
