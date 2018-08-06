from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from music.models import Album
#from django.template import loader

all_albums = Album.objects.all()


def index(request):

    #all_albums = Album.objects.all()
    #template = loader.get_template('music/index.html')
    #context = {'all_albums':all_albums}
    #return HttpResponse(template.render(context,request))
    return render(request,'music/index.html', {'all_albums':all_albums})


def details(request,album_id):
    
    album = get_object_or_404(Album,pk=album_id)
    
    #try :
      #  album = Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
     #   raise Http404("Album Does not Exists")
    
    
    return render(request,'music/details.html',{'album':album})

   # return HttpResponse("<h2>Details for Album id: "+str(album_id)+"</h2>")

def favourite(request,album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_songs = album.song_set.get(pk=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request,'music/details.html',{ 'album' : album, 'error_message': "you did not select a valid song",})
    else:
        selected_songs.is_favourite = True
        selected_songs.save()
        return render(request, 'music/details.html', {'album': album})



