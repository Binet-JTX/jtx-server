from django.contrib import admin

from jtx_core.models.user import User
from jtx_core.models.tag import Tag, TagKey


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(TagKey)
