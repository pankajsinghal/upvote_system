# upvote\_system
Image upvote downvote system(like instagram :P)
(My first attempt on django framework)

Steps to Run:

1. install django 1.8
2. go to mysite dir.
3. run python manage.py runserver
4. copy all the photos to upvote\_system/mysite/static/photos
5. in upvote\_system/mysite run python manage.py shell
	a) from votes.models import Photo
	b) Photo.add_photos('../static/photos')
6. visit 127.0.0.1:8000/admin to create users. 
6. visit 127.0.0.1:8000/votes to see all the photos and votes


Sources:
https://docs.djangoproject.com/en/1.8/intro/tutorial01/
http://www.effectivedjango.com/tutorial/authzn.html
https://docs.djangoproject.com/en/1.8/topics/db/examples/many\_to\_many/
http://francoisgaudin.com/2013/08/22/decorators-in-django/
