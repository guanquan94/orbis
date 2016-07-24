from django import forms

from .models import Contact_Us

class Contact_UsForm(forms.ModelForm):
    class Meta:
        model = Contact_Us
        fields = ['Full_Name', 'email', 'message']
        
    def clean_email(self): #if you need to use for school purpose
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@") #america@gmail.com ---> email_base = america, provider = gmail.com
        domain, extension = provider.split('.') #gmail.com ---> domain = gmail, extension = com
        #if not domain == 'USC':
        #    raise forms.ValidationError("Please make sure you use your USC email.")
        #if not extension == "edu":
        #    return forms.ValidationError("Please use a valid .edu email address")
        return email

    def clean_full_name(self):
        Full_Name = self.cleaned_data.get("Full_Name")
        #write validation code
        return Full_Name
#     Full_Name = forms.CharField(required=False)
#     email = forms.EmailField()
#     message = forms.CharField()

        


# class SignUpForm(forms.ModelForm):
#     class Meta:
#         model = SignUp
#         fields = ['Full_Name', 'email']
#         #exclude = ['full_name'] <----------To Remove
# 
# 
#     def clean_email(self): #if you need to use for school purpose
#         email = self.cleaned_data.get('email')
#         email_base, provider = email.split("@") #america@gmail.com ---> email_base = america, provider = gmail.com
#         domain, extension = provider.split('.') #gmail.com ---> domain = gmail, extension = com
#         #if not domain == 'USC':
#         #    raise forms.ValidationError("Please make sure you use your USC email.")
#         #if not extension == "edu":
#         #    return forms.ValidationError("Please use a valid .edu email address")
#         return email
# 
#     def clean_full_name(self):
#         Full_Name = self.cleaned_data.get("Full_Name")
#         #write validation code
#         return Full_Name