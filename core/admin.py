from django.contrib import admin

from core.models import Position, Group, UserDocs, User

admin.autodiscover()
admin.site.register(User)
admin.site.register(UserDocs)
admin.site.register(Group)
admin.site.register(Position)