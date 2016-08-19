from django.db import models
from django.utils import timezone



class Person(models.Model):
	firstname = models.CharField(max_length=50)
	lastname = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	vk = models.CharField(max_length=50)
	login = models.CharField(max_length=50)
	password = models.CharField(max_length=50)

	
class SysJournal(models.Model):
	datein = models.DateTimeField()
	dateout = models.DateTimeField()	
	person = models.ForeignKey(Person)

class Quest(models.Model):
	title = models.CharField(max_length=50)
	text = models.TextField()	
	date = models.DateTimeField()
	status = models.IntegerField(default=0)

	models.ManyToManyField(Person, through='RunQuest')

class RunQuest(models.Model):
	person = models.ForeignKey(Person, null='true')
	quest = models.ForeignKey(Quest, null='true')
	comment = models.TextField()
	firstdate = models.DateTimeField()
	lastdate = models.DateTimeField()


class Meeting(models.Model):
	title = models.CharField(max_length=50)
	target = models.CharField(max_length=50)
	text = models.TextField()
	date = models.DateTimeField()
	place = models.CharField(max_length=50)

	plans = models.ManyToManyField(Quest, through='Plan')
	persons = models.ManyToManyField(Person, through='Journal')

class Journal(models.Model):
	meeting = models.ForeignKey(Meeting, null='true')
	person = models.ForeignKey(Person, null='true')
	status = models.IntegerField(default=0)

class Plan(models.Model):
	meeting = models.ForeignKey(Meeting, null='true')
	quest = models.ForeignKey(Quest, null='true')
	result = models.TextField()
