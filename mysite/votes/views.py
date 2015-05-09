from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Photo
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def index(request):
    photos_list = Photo.objects.all()
    photo_result = []
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
	photo_object = dict(name = photo.image.name , url=photo.image.url, upvotes = upvotes_list_names, downvotes = downvotes_list_names)
	photo_result.append(photo_object)
    user = User.objects.get(pk=request.user.id)
    user_result = dict()
    photos_upvoted = user.upvotes.all()
    photos_upvotes_names = []
    for photo in photos_upvoted:
    	photos_upvotes_names.append(photo.image.name)
    photos_downvoted = user.downvotes.all()
    photos_downvotes_names = []
    for photo in photos_downvoted:
    	photos_downvotes_names.append(photo.image.name)
    user_result = dict(upvotes = photos_upvotes_names, downvotes = photos_downvotes_names)
    template = loader.get_template('votes/index.html')
    print str(photo_result) + str(user_result)
    context = RequestContext(request, {
        'photo_result': photo_result,
	'user_result' : user_result
    })
    return HttpResponse(template.render(context))

def upvote(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def downvote(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
