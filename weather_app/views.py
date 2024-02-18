from django.shortcuts import render,redirect
from .form import CityForm
from .models import city
import requests
from django.contrib import messages 

# Create your views here.
def home(request):
    url='https://api.openweathermap.org/data/2.5/weather?q={},&appid=88b94ea9d7c92229796b72f131ff0c28&units=metric' 

    if request.method=='POST':
        form=CityForm(request.POST)
        if form.is_valid():
            NCity=form.cleaned_data['name']  # this is input cityname
            ccity=city.objects.filter(name=NCity).count()  # database class name city if any city name in database it will count 
            if ccity==0:                               # after check put the city name that not stored repeated
                res=requests.get(url.format(NCity)).json()
                print(res)
                if res['cod']==200:
                    form.save()
                    messages.success(request,' '+NCity+' Added Successfully...!!!')
                else:
                    messages.error(request,'City Does Not Excists...!!!')
            else:
                messages.error(request,'City Already Exists...!!!')
 
    form=CityForm()

    cities=city.objects.all()
    data = []
    for area in cities:
        res = requests.get(url.format(area)).json()
        city_weather={
            'city': area,
            'temperature': res['main']['temp'],
            'description': res['weather'][0]['description'],
            'country': res['sys']['country'],
            'icon': res['weather'][0]['icon'],
        }
        data.append(city_weather)
        
    context = {'data' : data,'form' : form}
    return render(request,'weatherapp.html',context)

def delete_city(request,CName):
    city.objects.get(name=CName).delete()
    messages.success(request," "+CName+" Removed Successfully...!!!")
    return redirect('Home')