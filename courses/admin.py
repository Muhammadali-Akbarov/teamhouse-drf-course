from django.contrib import admin
from .models import (
    Cource,
    Review
)

admin.site.register([Cource,Review])