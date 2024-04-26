from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.models import*
def insert_Topic(request):
    topic_name=input("Enter topic_name: ")
    
    
    TO=Topic.objects.get_or_create(Topic_name=topic_name)[0]
    TO.save()
    
    return HttpResponse("Topic is created successfully!!")

def insert_WebPage(request):
    tn=input("Enter Topic name: ")
    n=input('Enter name: ')
    e=input('Enter email: ')
    u=input('Enter url: ')
    
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    TO.save()
    
    
    WO=WebPage.objects.get_or_create(Topic_name=TO,name=n,email=e,url=u)[0]
    WO.save()
    
    return HttpResponse("WebPage is created successfully!!")
    
def insert_AccessRecord(request):
    tn=input("Enter Topic name: ")
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    TO.save()
    
    n=input('Enter name: ')
    e=input('Enter email: ')
    u=input('Enter url: ')
    
    WO=WebPage.objects.get_or_create(Topic_name=TO,name=n,email=e,url=u)[0]
    WO.save()
    
    d=input("Enter date: ")
    a=input("Enter author name: ")
    
    AO=AccessRecord.objects.get_or_create(date=d,author=a,name=WO)[0]
    AO.save()

    return HttpResponse("AccessRecord is Created successfully!!")
    
    