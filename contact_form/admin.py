from django.contrib import admin

# Register your models here.
from .forms import Contact_UsForm
from .models import Contact_Us



# class SignUpAdmin(admin.ModelAdmin):
#     list_display = ["__unicode__", "timestamp", "updated"]
#     form = SignUpForm
#     #class Meta:
#     #    model = SignUp
# # 
# # 
# # # admin.site.register(SignUp, SignUpAdmin)
# # 



class Contact_UsAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    form = Contact_UsForm
      

admin.site.register(Contact_Us, Contact_UsAdmin)
