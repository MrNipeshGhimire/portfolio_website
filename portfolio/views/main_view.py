from django.shortcuts import render,get_object_or_404, redirect
from ..models import Profile,Skills,Education,Experience,Projects,Contact
from django.contrib import messages

def index(request):
    profile = get_object_or_404(Profile,pk=1)
    skill = Skills.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    projects = Projects.objects.all()

    return render(request,'index.html',{'profile':profile,'skills':skill, 'education':education,'experience':experience,'projects':projects})


def contactForm(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact.objects.create(
            name=name,
            email = email,
            subject = subject,
            message = message
        )
        contact.save()
        messages.success(request,"Your message sent successfully")
        return redirect("index")