from django.contrib import admin
from jtx_core.models.tag import Tag, TagKey
from jtx_core.models.user import User

admin.site.register(Tag)
admin.site.register(TagKey)
admin.site.register(User)