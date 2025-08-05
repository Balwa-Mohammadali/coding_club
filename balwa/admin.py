from django.contrib import admin

# Register your models here.

from .models import Apply,Contact

admin.site.register(Apply)

class ContactAdmin(admin.ModelAdmin):
    list_display=('name','email','msg')

admin.site.register(Contact,ContactAdmin)