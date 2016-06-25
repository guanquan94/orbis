from urllib import quote_plus
from django import template

register = template.Library()

@register.filter
def urlify(value):
	return quote_plus(value)

def about(request):
	return render(request,"about1.html",{})