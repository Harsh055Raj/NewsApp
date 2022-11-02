from django.contrib import admin

from news_api.forms import MailMessageForm
from . import models
# Register your models here.

admin.site.register(models.Subscribers)
admin.site.register(models.MailMessage)
admin.site.register(models.Contact)

