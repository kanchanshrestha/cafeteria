from django.shortcuts import render
from customer.models import Customer
# Create your views here.
def customerlist(request):
   customers=Customer.objects.all()
   return render(request,'customertemp/customer_list.html')

# from django.shortcuts import redirect, render
# from django. http import HttpRequest, HttpResponse,HttpResponseRedirect
# from .models import StudentForm
# from .forms import StudentF
# # Create your views here.

# def studentform(request):
#     forms=StudentF()
#     if request.method=='POST':
#         forms=StudentF(request.POST)
#         print(forms)

#         if forms.is_valid():
#             forms.save()
#             return redirect('/studentform/getstudentlist/')
            
#         else:
#             return HttpResponse("Invalid Form")

#     context={
#         "forms":forms
#     }
  
#     return render (request,'studentform/index.html',context)