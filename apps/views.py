from django.shortcuts import render

# from apps.models import Friend
from apps.models import TimeLine


# def index_view(request):
#     context = {
#         'friends': Friend.objects.all()
#     }
#     return render(request, 'apps/index.html', context)


def index_view(request):
    context = {
        'times': TimeLine.objects.all()
    }
    return render(request, 'apps/index1.html', context)
