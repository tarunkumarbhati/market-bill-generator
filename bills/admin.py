from django.contrib import admin
from bills import models

# Register your models here.
myModels = [
            models.Item,
            models.Discountrule
]

admin.site.register(myModels)