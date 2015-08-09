from django.contrib import admin

from jtx_video.models.video import Video
from jtx_video.models.file import Folder, VideoFile, SubtitleFile

# Register your models here.
admin.site.register(Video)
admin.site.register(Folder)
admin.site.register(VideoFile)
admin.site.register(SubtitleFile)