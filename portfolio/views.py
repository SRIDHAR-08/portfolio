from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt



def portfolio_home(request):
    data = profile_page.objects.all()
    skill_data = skill.objects.all()
    project_data = project.objects.all()
 
    return render(request, 'portfolio\portfolio_home.html',{'data':data,'project_data':project_data,'skill':skill_data})

def allproject(request):
    project_data = project.objects.all()
    return render(request,'portfolio/allproject.html',{'project_data':project_data})

def project_details(request,id):
    project_data = project.objects.filter(id=id)
    return render(request,'portfolio/project_details.html',{'project_data':project_data})

def resume_data(request):
    resume_data = resume.objects.all()
    return render(request,'portfolio/resume.html',{'resume_data':resume_data})

def portfolio_about(request):
    data = profile_page.objects.all()
    skill_data = skill.objects.all()
    project_data = project.objects.all()
 
    return render(request, 'portfolio/aboutpage.html',{'data':data,'project_data':project_data,'skill':skill_data})

from django.utils import timezone
from datetime import datetime
current_datetime = datetime.now()  # Replace this with your datetime object



@csrf_exempt
def Contect(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        message_send_date = current_datetime.strftime("%d %B %Y")
        message_send_time = timezone.localtime().strftime("%H:%M:%S")

   
        contect.objects.create(name=name, gmail=email, message=message,message_send_date=message_send_date,message_send_time=message_send_time)
        
        import smtplib
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("sridhar200288@gmail.com", "mhcd uzlb zgsa uiwq")
        message = f"thank u for your message\n \n Hai {name} message successfully sent message \n \n Your message : {message} \n \n Time :{message_send_date} {message_send_time} "
        s.sendmail("sridhar200288@gmail.com", email, message)
        s.sendmail("sridhar200288@gmail.com","sridhar200288@gmail.com", message)
        s.quit()
        print( 'Email sent!')
        contect_data = list(contect.objects.filter(gmail=email).values())
        
        request.session['contect_data'] = contect_data
        return redirect('mes_succ')

    else:
        return render(request,'portfolio/contect.html')
@csrf_exempt
def mes_succ(request):
    contect_data = request.session.pop('contect_data', [])
    print(len(contect_data))
    if len(contect_data)==0:
        return redirect('contect')
    else:
        contect_data = reversed(contect_data)
        return render(request, 'portfolio/mes_succ.html', {'contect_data': contect_data})
    

    