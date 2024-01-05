from django.shortcuts import render 
from django.http import HttpResponse
from .models import Service,Mashgulot


def  service_read(request):
    services = Service.objects.all()
    print(services)
    return HttpResponse("service ishladi")


def create_service(request):
    servise = Service.objects.create(
        # service_icon='image.jpg',
        service_name='suzish',
        about_service='yaxshi'     )
    return HttpResponse('Data yaratilindi')


def update_service(request):
    service = Service.objects.get(service_name='yugurish')
    service.service_name='yugurish'
    service.about_service="zo'r"
    service.save()
    return HttpResponse("Ma'lumot yangilandi")

def delete_service(request):
    service = Service.objects.get(service_name='yugurish')
    service.delete()
    
    return HttpResponse("Ma'lumot o'chirildi")
    


def  mashgulot_read(request):
    mashgulot = Mashgulot.objects.all()
    print(mashgulot)
    return HttpResponse("tizim ishladi")

def create_mashgulot(request):
    mashgulot = Mashgulot.objects.create(
        mashgulot_nomi="suzish",
        davomiyligi="30 daqiqa",
        boshlanish_vaqti="08:00",
        tugash_vaqti="08:30",
        # mashgulot_icon="img.png",
        kuni="Dushanba"
    )
    return HttpResponse('tizim ishladi')

def update_mashgulot(request):
    mashgulot=Mashgulot.objects.get(mashgulot_nomi='suzish')
    mashgulot.mashgulot_nomi='yugurish',
    mashgulot.davomiyligi='45 daqiqa',
    mashgulot.boshlanish_vaqti='08:00',
    mashgulot.tugash_vaqti='08:45',
    mashgulot.kuni='Seshanba'
    mashgulot.save()
    return HttpResponse("tizim ishladi")

def delete_mashgulot(request):
    mashgulot = Mashgulot.objects.get(mashgulot_name='suzish')
    mashgulot.delete()
    
    return HttpResponse("Tizim ishladi")







