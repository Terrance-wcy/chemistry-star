from django.db import models

# Create your models here.

from mongoengine import *

connect('wym', host='127.0.0.1', port=27017)



class Users(Document):
    name = StringField(required=True, max_length=200)
    password = StringField(required=True, max_length=200)
    status = StringField(required=True, max_length=200,default='stu')

class GkQuestion(Document):
    question = StringField(required=True, max_length=200)
    answer_a = StringField(required=True, max_length=200)
    answer_b = StringField(required=True, max_length=200)
    answer_c = StringField(required=True, max_length=200)
    answer_d = StringField(required=True, max_length=200)
    r_answer = StringField(required=True, max_length=200)
    papermark = StringField(required=True, max_length=200)
    mark =IntField(required=True)
    jiexi = StringField(required=True, max_length=1000)

class Shoucangt(Document):
    papermark = StringField(required=True, max_length=200)
    questionmark =IntField(required=True)
    number = IntField(required=True)
    name= StringField(required=True, max_length=200)

class papers(Document):
    name= StringField(required=True, max_length=200)
    author = StringField(required=True, max_length=200)
    intro = StringField(required=False, max_length=1000)
    pubtime = DateTimeField(required=False)

class paperquestion(Document):
    papername= StringField(required=True, max_length=200)
    papermark = StringField(required=True, max_length=200)
    mark = IntField(required=True)

class Statistic(Document):
    name= StringField(required=True, max_length=200)
    total = IntField(required=True,default=0)
    right = IntField(required=True,default=0)

class quesrecord(Document):
    name= StringField(required=True, max_length=200)
    papermark = StringField(required=True, max_length=200)
    mark = IntField(required=True)
    pubtime = DateTimeField(required=False)
    tf = StringField(required=True, max_length=10)









