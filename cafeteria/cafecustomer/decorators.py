from django.http import HttpResponse
from django.shortcuts import redirect

# def allowed_users(allowed_roles=[]):
#     def check_user(view_func):
#         def wrapper_function(request,*args,**kwargs):
#             group = None
#             if request.user.groups.exists():
#                 group=request.user.groups.all()[0].name

#             if group=='admin':
#                 return view_func(request,*args,**kwargs)

#             if group=='customer':
#                 return redirect('dashboard')
        
        
#         return wrapper_function
def admin_only(view_func):
        def wrapper_function(request,*args,**kwargs):
            group = None
            if request.user.groups.exists():
                group=request.user.groups.all()[0].name

            if group=='admin':
                return view_func(request,*args,**kwargs)
        return wrapper_function

def customer_only(view_func):
    def wrapper_functiona(request,*args,**kwargs):
        group=None
        if request.user.groups.exists():
            group=request.user.groups.all()[0].name

        if group=='customer':
            return redirect('/cafecustomer/dashboard')


