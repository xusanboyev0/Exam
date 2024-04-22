# from django.core import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from apps.models import Post, Tag


def post_list_view(request):
    posts = Post.objects.all()
    contex = {
        'posts': posts,
        'tags': Tag.objects.all(),
        'latest_post': Post.objects.order_by('-created_at')[:3],
    }
    return render(request, 'apps/list.html', contex)


def post_detail_view(request, pk):
    post = Post.objects.get(uuid=pk)
    contex = {
        'post': post,
        'tags': Tag.objects.all(),
        'latest_post': Post.objects.order_by('-created_at')[:3],
    }
    return render(request, 'apps/detail.html', contex)




# def profile_detail_view(request, pk):
#     profile = Profile.objects.get(pk=pk)
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('phone_number')
#         mobile = request.POST.get('mobile')
#         address = request.POST.get('address')
#         profile.fullname = full_name
#         profile.email = email
#         profile.phone_number = phone_number
#         profile.mobile = mobile
#         profile.address = address
#         profile.save()
#         Profile.objects.create(name=full_name, price=email, description=phone_number, mobile=mobile, address=address)
#
#     context = {
#         'profile': Profile.objects.get(id=pk)
#     }
#     return render(request, 'apps/profile.html', context)


# def send_email_view(request):
#     subject = 'Welcome'
#     message = 'Thank you for sending your email.'
#     recipient_list = ['xusanboyevbilol@gmail.com']
#     send_mail(subject, message, EMAIL_HOST_USER, recipient_list)
#     return HttpResponse('Email sent successfully')


# def forms_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         description = request.POST.get('description')
#         Product.objects.create(name=name, price=price, description=description)
#         return render(request, 'apps/list.html')


# from root.settings import EMAIL_HOST_USER


# def profile_view(request, pk):
#     profile = Profile.objects.get(pk=pk)
#     if request.method == 'POST':
#         full_name = request.POST.get('full_name')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('phone_number')
#         mobile = request.POST.get('mobile')
#         address = request.POST.get('address')
#         Profile.objects.create(name=full_name, price=email, description=phone_number, mobile=mobile, address=address)
#
#     return render(request, 'apps/profile.html')
