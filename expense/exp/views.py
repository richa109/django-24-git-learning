from django.shortcuts import render
# from django.http import JsonResponse
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
        list_exp = Expense.objects.filter(user=user).values("id",'user', 'category','subCategory','amount','expDateTime','transaction_type','status','description','goal__goalname')
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
       expense = Expense.objects.get(id=self.kwargs['pk'])
       expense_data = {
        "id": expense.id,
        "user": expense.user,
        "category": expense.category,
        "subCategory": expense.subCategory,
        "amount": expense.amount,
        "expDateTime": expense.expDateTime,
        "transaction_type": expense.transaction_type,
        "status": expense.status,
        "description": expense.description,
        "goal__goalname": expense.goal.goalname if expense.goal else None
    }
       print(expense)
       
    #    return render(request, self.template_name, {'exp_detail': self.get_object(),'expense':expense,'labels':self.labels,'data':self.data})
       return render(request, self.template_name, {'exp_detail': expense_data,'expense':expense,'labels':labels,'data':data})
      
     
    

    
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
    
    # Import your Expense model here


def bar_chart(request):
    # Initialize empty lists for labels and data
    labels = []
    data = []

    # Query for expenses
    queryset = Expense.objects.filter(user=request.user).order_by('-amount')[:10]

    # Populate labels and data from queryset
    for expense in queryset:
        labels.append(expense.category)
        data.append(expense.amount)

    # Create context dictionary
    context = {
        'labels': labels,
        'data': data,
    }

    # Render both chart.html and user_dashboard.html with the same context
    render(request, 'user/user_dashboard.html', context)
    return render(request, 'exp/chart.html', context)

    

# def get_context_data(self, **kwargs):
#         bar_chart = self.request.POST.get('bar_chart')
#         print(bar_chart)
#         kwargs['user_type'] = 'is_user'
#         return render().get_context_data(**kwargs)


# def user_specific_chart(request):
#     # Assuming you have a model called Expense with a field called amount
#     # Fetch data for the chart specific to the logged-in user
#     user_expenses = Expense.objects.filter(user=request.user)
#     labels = []
#     data = []
#     for expense in user_expenses:
#         labels.append(expense.category)  # Example: Use category as labels
#         data.append(expense.amount)      # Example: Use amount as data points

#     return render(request, 'exp/user_chart.html', {'labels': labels, 'data': data})

   
    
    

