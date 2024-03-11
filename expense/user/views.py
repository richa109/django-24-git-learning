# Import necessary modules
from django.urls import reverse
from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.views.generic import ListView
from exp.models import Expense
from .models import User
from .forms import UserRegistrationForm
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Your existing views...

class UserRegisterView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user/user_register.html'
    success_url = '/user/login/'

    def get_context_data(self, **kwargs):
        email = self.request.POST.get('email')
        print(email)
        kwargs['user_type'] = 'is_user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        subject = "Welcome to Mysite"
        message = "Hello Guys! Now you can create and manage your expense. Thank you for joining us."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.request.POST.get("email"), ]
        print(recipient_list)
        send_mail(subject, message, email_from, recipient_list)
        return response


# views.py



class UserLoginView(LoginView):
    template_name = 'user/login.html'

    def get_redirect_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_user:
                return reverse('user_dashboard')  # Make sure this matches the name in your urls.py
            else:
                return reverse('user_register')   # Adjust this accordingly

def logout_view(request):
    logout(request)
    return redirect('/user/login/')
    

class UserDashboardView(ListView):

    template_name = 'user/user_dashboard.html'
    context_object_name = 'user_dashboard'

    def get(self, request, *args, **kwargs):
        user = request.user
        print(user)
        # expense = Expense.objects.all().values()
        expense1 = Expense.objects.filter(user=user).values()
        # expense = Expense.objects.all().values('id','amount','category','user','payee','transaction_type','description','expDateTime','status')
        expense = Expense.objects.filter(user=user).values('id','amount','transaction_type','description','expDateTime','status')
        

        print(".....",expense)

        sort_by = self.request.GET.get('sort_by', 'amount')
        direction = self.request.GET.get('direction', 'asc')
        print(".....",sort_by)
        print(".....",direction)
        if direction == 'asc':
            expense = expense.order_by(sort_by)
        elif direction == 'desc':
            expense = expense.order_by(f'-{sort_by}')

        # search_input = self.request.GET.get('search-area') or ''
        # if search_input:
        #     exp = Expense.objects.filter(category_categoryname_icontains=search_input).values()
        #     print('...................exp',exp)
        #     print('Search input:', search_input)
        

        
        
        return render(request, 'user/user_dashboard.html',{
            'expenses':expense,'expense1':expense1
        })
    template_name = 'user/user_dashboard.html'
    
    def get(self, request, *args, **kwargs):
        # def safe(request): 
        if request.user.is_authenticated:
            # expenses = Expense.objects.filter(payee__user=request.user).all()
            # expense = Expense.objects.all().values()
            expenses = Expense.objects.filter(user=request.user).all()
            try:
             user_income = sum(list(expenses.filter( transaction_type="income").values_list('amount', flat=True)))
            except: 
             user_income = 0
            
            try:
             user_expenses = sum(list(expenses.filter( transaction_type="expense").values_list('amount', flat=True)))
            except:
             user_expenses = 0
            
            try:
             safe_amount = user_income - (user_expenses*10/100)
            except: 
             safe_amount = 0
            
        
        #print("*"*80)
            print("user_income", user_income)
            print("user_expenses", user_expenses)
            return render(request, 'user/user_dashboard.html', 
                {
            "expenses": expenses,
            "user_income": user_income, 
            "user_expenses": user_expenses, 
            "safe_amount": user_income-user_expenses
            
            
               })
        else:
            return redirect('user_dashboard')
    

    # def safe(request): 
    #     if request.user.is_authenticated:
    #         # expenses = Expense.objects.filter(payee__user=request.user).all()
    #         # expense = Expense.objects.all().values()
    #         expenses = Expense.objects.filter(user=request.user).all()
    #         try:
    #          user_income = sum(list(expenses.filter( transaction_type="income").values_list('amount', flat=True)))
    #         except: 
    #          user_income = 0
            
    #         try:
    #          user_expenses = sum(list(expenses.filter( transaction_type="expense").values_list('amount', flat=True)))
    #         except:
    #          user_expenses = 0
            
    #         try:
    #          safe_amount = user_income - (user_expenses*10/100)
    #         except: 
    #          safe_amount = 0
            
        
    #     #print("*"*80)
    #         print("user_income", user_income)
    #         print("user_expenses", user_expenses)
    #         return render(request, 'user/safe.html', 
    #             {
    #         "expenses": expenses,
    #         "user_income": user_income, 
    #         "user_expenses": user_expenses, 
    #         "safe_amount": user_income-user_expenses
            
            
    #            })
    #     else:
    #         return redirect('user_dashboard')
    

def safe(request):
            if request.user.is_authenticated:
            # expenses = Expense.objects.filter(payee__user=request.user).all()
            # expense = Expense.objects.all().values()
             expenses = Expense.objects.filter(user=request.user).all()
            try:
             user_income = sum(list(expenses.filter( transaction_type="income").values_list('amount', flat=True)))
            except: 
             user_income = 0
            
            try:
             user_expenses = sum(list(expenses.filter( transaction_type="expense").values_list('amount', flat=True)))
            except:
             user_expenses = 0
            
            try:
             safe_amount = user_income - (user_expenses*10/100)
            except: 
             safe_amount = 0
        
            print("user_income", user_income)
            print("user_expenses", user_expenses)
            return render(request, 'user/safe.html', 
                {
            "expenses": expenses,
            "user_income": user_income, 
            "user_expenses": user_expenses, 
            "safe_amount": user_income-user_expenses
            
            
               })
    
def chart(request):
    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user=request.user).all()
        try:
            user_income = sum(list(expenses.filter(transaction_type="income").values_list('amount', flat=True)))
        except: 
            user_income = 0
            
        try:
            user_expenses = sum(list(expenses.filter( transaction_type="expense").values_list('amount', flat=True)))
        except:
            user_expenses = 0
            
        try:
            # safe_amount = user_income - (user_income * 10 / 100)
            safe_amount = user_income - (user_expenses*10/100)
            safe_amount = int(safe_amount)
        except: 
            safe_amount = 0
        
        chart_data = [user_income, safe_amount - user_expenses, user_expenses]
        return render(request,'user/chart.html', {"chart_data": chart_data,  "expenses": expenses, "user_income": user_income, "user_expenses": user_expenses, "safe_amount": user_income-user_expenses})
    return render(request,'user/chart.html', {"chart_data": [0, 0, 0],})

def chart1(request):
    if request.user.is_authenticated:
        expenses = Expense.objects.filter(user=request.user).all()
        try:
            user_income = sum(list(expenses.filter(transaction_type="income").values_list('amount', flat=True)))
        except: 
            user_income = 0
            
        try:
            user_expenses = sum(list(expenses.filter( transaction_type="expense").values_list('amount', flat=True)))
        except:
            user_expenses = 0
            
        try:
            # safe_amount = user_income - (user_income * 10 / 100)
            safe_amount = user_income - (user_expenses*10/100)
            safe_amount = int(safe_amount)
        except: 
            safe_amount = 0
        
        chart_data = [user_income, safe_amount - user_expenses, user_expenses]
        return render(request,'user/chart.html', {"chart_data": chart_data,  "expenses": expenses, "user_income": user_income, "user_expenses": user_expenses, "safe_amount": user_income-user_expenses})
    return render(request,'user/chart.html', {"chart_data": [0, 0, 0],})

def forgot(request):
       return render(request,'user/forgot.html')
   
