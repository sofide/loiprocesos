from django.shortcuts import render

from gallery.models import Photo, Section


def gallery_home(request):
    sections = Section.objects.all()


    return render(request, 'gallery/gallery_home.html', {'sections': sections,
                                                        })
