from django.http import HttpResponse
from django.core.mail import send_mail


def sendmail(request):

    send_mail(subject='jo`natilganVaqt',
              message='weather bot', 
              from_email='sarvinozsaidova2404@gmail.com',
              recipient_list=['mamajonovibrokhimjon@gmail.com'],
              fail_silently=False)
    return HttpResponse('email has been sent ')