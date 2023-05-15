from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy

from petstgram_workshop.common.models import Like
from petstgram_workshop.photos.models import Photo


def apply_count_likes(photo):
    photo.likes_count = photo.like_set.count()
    return photo


# Create your views here.
def apply_user_liked_photo(photo):
    photo.is_liked_by_user = photo.like_set.all()
    return photo


def home_page(request):
    all_photos = [apply_count_likes(photo) for photo in Photo.objects.all()]
    all_photos = [apply_user_liked_photo(photo) for photo in all_photos]

    context = {
        "all_photos": all_photos
    }

    return render(request=request, template_name='common/home-page.html', context=context)


def like_functionality(request, photo_id):
    photo = Photo.objects.get(id=photo_id)
    liked_object = Like.objects.filter(to_photo_id=photo_id).first()

    if liked_object:
        liked_object.delete()
    else:
        like = Like(to_photo=photo)
        like.save()

    return redirect(request.META['HTTP_REFERER'] + f'#photo-{photo_id}')


def copy_link_to_clipboard(request, photo_id):
    copy(request.META['HTTP_HOST']+ resolve_url('photo-details', photo_id))
    return redirect(request.META['HTTP_REFERER'] + f'#{photo_id}')