from django.shortcuts import render
from django.views.generic import CreateView
from django.core.mail import send_mail
from django.conf import settings
from .forms import *
from .models import *
from django.views.generic import ListView,DetailView
from django.views.generic import DeleteView,UpdateView

# from django.conf import settings
# from django.core.mail import send_mail
# from django.http import HttpResponse


# Create your views here.
# 1.navbar
def navbar(request):
    return render(request,'exp/navbar.html')

def index(request):
    return render(request,'exp/index.html')

def home(request):
    return render(request,'exp/home.html')


class ExpenseCreationView(CreateView):
    form_class =ExpCreationForm
    model = Expense
    template_name = 'exp/create_expense.html'
    success_url = '/exp/list_exp/'

    def get_context_data(self,**kwargs):
        email = self.request.POST.get('email')
        print(email)
        kwargs['user_type'] = 'is_user'
        
        return super().get_context_data(**kwargs)
    
    


    def form_valid(self, form):
        
        
        form.instance.user = self.request.user
        response = super().form_valid(form)
        print("email id ----",self.request.user.email)
        subject = "Welcome to Mysite"
        message = "We are pleased to inform you that your recent income/expense has been added successfully to your Expense Manager App. Your records are now available for you to access and review at any time.With our Expense Manager App, you can easily keep track of your income and expenses, set budgets, and monitor your spending habits. By doing so, you can better manage your finances, avoid overspending, and achieve your financial goals."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [self.request.user.email]        
        send_mail(subject, message, email_from, recipient_list)
        print(recipient_list)   
        return response
   
    
   


class ExpenseListView(ListView):
    model = Expense
    template_name = 'exp/list_exp.html'
    context_object_name = 'list_exp'
    
    # def get_queryset(self):
    #     return super().get_queryset()  

    def get(self, request, *args, **kwargs):
        user = request.user
        print(user)
        # list_exp1=Expense.objects.filter(user=user).values()
        list_exp = Expense.objects.filter(user=user).values("id",'user', 'category','subCategory','amount','expDateTime','transaction_type','status','description')
        print(list_exp)
        return render(request,'exp/list_exp.html',{'list_exp':list_exp})
    




class ExpenseUpdateView(UpdateView):
    model = Expense
    form_class = ExpCreationForm
    template_name = 'exp/create_expense.html'
    success_url = '/exp/list_exp/'

   

    
class ExpenseDetailView(DetailView):
    model = Expense
    template_name = 'exp/exp_detail.html'
    context_object_name = 'exp_detail'
    success_url = '/exp/exp_detail/'
    
             
    
    def get(self, request ,*args, **kwargs):
       user = request.user
       print(user)
       labels=[]
       data =[]
       category = Expense.objects.all().values_list('category',flat=True)
    # category = Expense.objects.filter(user=user).values_list('category__categoryname',flat=True)
    
       amount = Expense.objects.all().values_list('amount',flat=True)
    # amount = Expense.objects.filter(user=user).values_list('amount',flat=True)
       for i in category:
            labels.append(i)
       for i in amount:
            data.append(i)
       expense = Expense.objects.filter(id=self.kwargs['pk'],).values()
       
    #    return render(request, self.template_name, {'exp_detail': self.get_object(),'expense':expense,'labels':self.labels,'data':self.data})
       return render(request, self.template_name, {'exp_detail': self.get_object(),'expense':expense,'labels':labels,'data':data})
      
     
    

    
class ExpenseDeleteView(DeleteView):
    model = Expense
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    success_url = '/exp/list_exp/'
    
    
class AccountCreationView(CreateView):
    model = Account
    form_class = AccountCreationForm
    template_name = 'exp/manage_exp.html'
    success_url = '/exp/list1_exp/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class AccountListView(ListView):
    model = Account
    template_name = 'exp/list1_exp.html'
    context_object_name = 'list1_exp'
    
    def get_queryset(self):
        return super().get_queryset()
    

class AccountUpdateView(UpdateView):
    model = Account
    form_class = AccountCreationForm
    template_name = 'exp/manage_exp.html'
    success_url = '/exp/list1_exp/'


class AccountDetailView(DetailView):
    model = Account
    template_name = 'exp/detail_acc.html'
    context_object_name = 'detail_acc'
    success_url = '/exp/detail_acc/'
    
class AccountDeleteView(DeleteView):
    model = Account
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    success_url = '/exp/list1_exp/'
    
    
    
   
    
    

