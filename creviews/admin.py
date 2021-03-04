from django.contrib import admin
# Register your models here.
from creviews.models import App
from creviews.models import Review
from creviews.models import Reply
from creviews.models import Report
admin.site.register(App)
admin.site.register(Review)
admin.site.register(Reply)
admin.site.register(Report)
