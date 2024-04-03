from django.contrib import admin

# from apps.models import Friend
from apps.models import TimeLine


#
# @admin.register(Friend)
# class FriendAdmin(admin.ModelAdmin):
#     pass

@admin.register(TimeLine)
class TimeLineAdmin(admin.ModelAdmin):
    pass
