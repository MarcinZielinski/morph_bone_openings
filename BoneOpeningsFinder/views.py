# Create your views here.
import os
import zipfile

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse, FileResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from BoneOpeningsFinder import morph
from BoneOpeningsFinder.forms import XRayForm
from morph_bone_openings.settings import MEDIA_URL


class LastFileLocation:
    def __init__(self):
        self.predict = ""
        self.mask = ""


lastFileLocation = LastFileLocation()


@csrf_exempt
def index(request):
    title = 'Bone morphological openings finder'
    author = 'Marcin Zieliński'
    form = XRayForm()
    html = render(request, 'index.html', {'title': title, 'author': author, 'form': form})
    return HttpResponse(html)


@csrf_exempt
def upload(request):
    form = XRayForm(request.POST, request.FILES)

    if form.is_valid():
        saved_picture = form.save()
        predict, mask = morph.predict(saved_picture.xRayImg.url[1:])
        lastFileLocation.predict = predict
        lastFileLocation.mask = mask
        return JsonResponse({
            'predict': predict,
            'mask': mask
        })
    else:
        return HttpResponseBadRequest()


@csrf_exempt
def download(request):
    zip_path = os.path.join(MEDIA_URL, 'zips',
                            lastFileLocation.predict.split("/")[-1].split('_')[0] + '_morphology.zip')[1:]
    with zipfile.ZipFile(zip_path, 'w') as zip:
        zip.write(lastFileLocation.predict)
        zip.write(lastFileLocation.mask)
    return FileResponse(
        open(zip_path, 'rb')
    )
