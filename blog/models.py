from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from django.conf import settings
import re

def photo_path(instance, filename):
	from time import gmtime, strftime
	from random import choice
	import string
	arr = [choice(string.ascii_letters) for _ in range(8)]
	pid = ''.join(arr)
	extension = filename.split('.')[-1]
	return '{}/{}/{}.{}'.format(strftime('post/%Y/%m/%d/'), instance.author.username, pid, extension)

class Post(models.Model):
	owner = models.ForeignKey(User, null=True)
	#owner = models.ForeignKey(settings.AUTH_USER_MODEL)
	country = CountryField(blank_label='(select country)')

	SPOT ="SPOT"
	ACCOMODATION = "ACCOMODATION"
	RESTAURANT = "RESTAURANT"
	RECREATION = "RECREATION"

	POSTCATEGORY = (
		(SPOT, 'SPOT'),
		(ACCOMODATION, 'ACCOMODATION'),
		(RESTAURANT, 'RESTAURANT'),
		(RECREATION, 'RECREATION')
	)


	postcategory = models.CharField(max_length=20, choices=POSTCATEGORY, default = SPOT)

	XBOX = "XBOX"
	CARDBOARD = "CARDBOARD"

	CLASSIFICATION = (
		(XBOX, 'XBOX'),
		(CARDBOARD, 'CARDBOARD')
	)

	classification = models.CharField(max_length = 20, choices=CLASSIFICATION, default = 360)

	title = models.CharField(max_length=200)
	name = models.TextField(max_length=40, default='정확한 명칭을 입력해주세요.')
	address = models.TextField(max_length=50, default='정확한 주소를 입력해주세요.')
	contents = models.TextField(max_length=500, default='좋은 장소를 다른 사람들에게 소개해주세요!')
	hashtag = models.TextField('HASHTAG')


	#hash = models.TextField(max_length=100, default=True)

	photo = models.ImageField(upload_to = 'blog/post', default = 'blog/post/None/no-img.jpg')
	video = EmbedVideoField(default="https://www.youtube.com/watch?v=STE2uqh-xqg")
	created_date = models.DateTimeField('Create Date', auto_now_add=True)
	modify_date = models.DateTimeField('Modify Date', auto_now=True)
	#하나의 post를 좋아하는 user가 여러명일 수도 있고, 한명의 user는 여러개의 post를 좋아할 수 있다. 따라서 user와 post는 다대다 관계가 되어야 하고
	#like_user_set은 이 post를 좋아하는 user의 집합(?)이다. 
	like_user_set = models.ManyToManyField(settings.AUTH_USER_MODEL,
										   blank=True,
										   related_name='like_user_set',
										   through='Like')  # post.like_set 으로 접근 가능

	tag_set = models.ManyToManyField('Tag', blank=True, max_length=40)

	def __str__(self):
		return self.hashtag

	def publish(self):
		self.created_date = timezone.now()
		self.save()

	def get_previous_post(self):
		return self.get_previous_by_modify_date()

	def get_next_post(self):
		return self.get_next_by_modify_date()

	@property
	def like_count(self):
		return self.like_user_set.count()


	def tag_save(self):
		tags = re.findall(r"#(\w+)", self.hashtag) # '#'로 시작하는 문자열 분리됨

		if not tags:
			return

		for t in tags:
			tag, tag_created = Tag.objects.get_or_create(name=t)
			self.tag_set.add(tag)  # NOTE: ManyToManyField 에 인스턴스 추가


class Like(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	post = models.ForeignKey(Post)
	created_date = models.DateTimeField(auto_now_add=True)
	modify_date = models.DateTimeField(auto_now=True)


	class Meta:
		unique_together = (
			('user', 'post')
		)


class Tag(models.Model):
	name = models.CharField(max_length=140, unique=True)

	def __str__(self):
		return self.name

