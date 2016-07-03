from django.conf import settings

from django.core.mail import send_mail

from django.shortcuts import render

from .forms import ContactForm, SignUpForm

#Create your views here.
def home(request):
    #if request.user.is_authenticated():
    #    title = "My Title %s" %(request.user)
    title = "Welcome"
    form = SignUpForm(request.POST or None) 
    context = {
        "title": title,
        "form": form,
    }
  
    if form.is_valid():
        #form.save()
        instance = form.save(commit=False)
        Full_Name = form.cleaned_data.get("Full_Name")
        if not Full_Name:
            Full_Name = "New Full Name"
        instance.Full_Name = Full_Name
        instance.save()
        context = {
            "title": "Thank You!",
        }
  
    return render(request,"home1.html", context)


def contact(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        #for key, value in form.cleaned_data.iteritem():
            #print key, value
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_Full_Name = form.cleaned_data.get("Full_Name")
        #print email, message, Full_Name
        subject = 'Site Contact Form'
        contact_message = "%s: %s via %s" %(
            form_Full_Name, 
            form_message, 
            form_email)

        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, 'yourotheremail@email.com']
        some_email_message = """<h1>Hello!</h1>"""

        send_mail(subject, 
            contact_message, 
            from_email, 
            to_email,
            html_message=some_email_message,
            fail_silently=True)

    context = {
        "form": form,
        "title": title,
    }
    return render(request, "forms.html", context)


    #if request.user.is_authenticated() and request.user.is_staff:
    #    context = {
    #        "queryset": [123, 456]
    #    }

