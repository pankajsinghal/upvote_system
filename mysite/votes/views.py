from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import RequestContext, loader
from .models import Photo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import functools
from django.core.exceptions import ObjectDoesNotExist
import exceptions,os


def validate_user_and_photo(method):
    @functools.wraps(method)
    def wrapper(self,*args, **kwargs):
        try:
	    user = User.objects.get(id=self.user.id)
        except ObjectDoesNotExist:
	    user = None
	if user is None:
            return JsonResponse(dict(status='error',reason='invalid user'))
        try:
	    photo = Photo.objects.get(id=kwargs['photo_id'])
        except ObjectDoesNotExist:
            photo = None
	if not photo:
            return JsonResponse(dict(status='error',reason='invalid photo'))
        return method(self, user, photo, *args, **kwargs)
    return wrapper

# Create your views here.
@login_required(login_url='/login')
def index(request):
    photos_list = Photo.objects.all()
    photo_result = {}
    for photo in photos_list:
	if not photo or not photo.image:
		continue
	upvotes_list = photo.upvotes.all()
	upvotes_list_names = []
	for user in upvotes_list:
		upvotes_list_names.append(user.get_full_name())
        downvotes_list = photo.downvotes.all()
        downvotes_list_names = []
        for user in downvotes_list:
                downvotes_list_names.append(user.get_full_name())
	photo_object = dict(photo_name = photo.image.name.split(os.path.sep)[-1], photo_url=photo.image.url, upvotes_names = upvotes_list_names, downvotes_names = downvotes_list_names)
	photo_result[photo.id] = photo_object
    user = User.objects.get(pk=request.user.id)
    user_result = dict()
    if user:
    	photos_upvoted = user.upvotes.all()
    	photos_upvotes_ids = []
    	for photo in photos_upvoted:
    		photos_upvotes_ids.append(photo.id)
    	photos_downvoted = user.downvotes.all()
    	photos_downvotes_ids = []
    	for photo in photos_downvoted:
    		photos_downvotes_ids.append(photo.id)
    	user_result = dict(upvotes = photos_upvotes_ids, downvotes = photos_downvotes_ids)
    template = loader.get_template('votes/index.html')
    print str(photo_result) + str(user_result)
    context = RequestContext(request, {
        'photo_result': photo_result,
	'user_result' : user_result,
    'username' : request.user.get_full_name()
    })
    return HttpResponse(template.render(context))

def returnJsonResponse(status,reason=None,http_status_code=200):
    return JsonResponse(dict(status=status, reason=reason),status=http_status_code)

@validate_user_and_photo
def upvote(request,user,photo,photo_id):
    if not photo.is_upvoted(user):
	photo.upvote(user)
    	photo.remove_downvote(user)
	return returnJsonResponse('ok')
    else:
	return returnJsonResponse('error','you have already upvoted this photo',400)

@validate_user_and_photo
def remove_upvote(request,user,photo,photo_id):
    if photo.is_upvoted(user):
        photo.remove_upvote(user)
	return returnJsonResponse('ok')
    else:
	return returnJsonResponse('error','you have not upvoted this photo',400)

@validate_user_and_photo
def downvote(request,user,photo,photo_id):
    if not photo.is_downvoted(user):
        photo.downvote(user)
	photo.remove_upvote(user)
    	return returnJsonResponse('ok')
    else:
        return returnJsonResponse('error','you have already downvoted this photo',400)

@validate_user_and_photo
def remove_downvote(request,user,photo,photo_id):
    if photo.is_downvoted(user):
        photo.remove_downvote(user)
    	return returnJsonResponse('ok')
    else:
        return returnJsonResponse('error','you have not downvoted this photo',400)
