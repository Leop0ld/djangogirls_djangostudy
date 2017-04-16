from django.shortcuts import render, redirect

from .models import Video


def video_list(request):
    video_list = Video.objects.all()
    return render(request, 'video/video_list.html', {'video_list': video_list})


def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)

    if request.method == 'POST':
        title = request.POST.get('title', '')
        key = request.POST.get('key', '')

        video.title = title
        video.key = key

        video.save()

        return redirect('/video/' + str(video.id))
    return render(request, 'video/video_detail.html', {'video': video})


def video_new(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        key = request.POST.get('key', '')

        video = Video(
            title=title,
            key=key,
        )

        video.save()

        return redirect('/video/' + str(video.id))

    return render(request, 'video/video_new.html')


def video_delete(request, video_id):
    Video.objects.get(id=video_id).delete()
    return redirect('/video/')
