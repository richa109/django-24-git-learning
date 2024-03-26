from django.contrib import admin
from django.urls import path,include
from.views import *
from.import views

urlpatterns = [
    path('navbar/',views.navbar,name='navbar'),
    path('index/',views.index,name='index'),
    path('home/',views.home,name='home'),
    
    # path('transaction/',views.transaction,name='transaction'),
    path('create_expense/',ExpenseCreationView.as_view(),name='create_exp'),
    path('list_exp/',ExpenseListView.as_view(),name='exp_list'),
    path('exp_detail/<int:pk>/',ExpenseDetailView.as_view(),name='exp_detail'),
    path('update_exp/<int:pk>/',ExpenseUpdateView.as_view(),name='update_exp'),
    #  path('exp/update_exp/<int:pk>/', ExpenseUpdateView.as_view(), name='update_exp'),
    path('exp_delete/<int:pk>/',ExpenseDeleteView.as_view(),name='delete_exp'),
    path('manage_exp/',AccountCreationView.as_view(),name='manage_exp'),
    path('list1_exp/',AccountListView.as_view(),name='list1_exp'),
    path('update_acc/<int:pk>/',AccountUpdateView.as_view(),name='update_acc'),
    path('detail_acc/<int:pk>/',AccountDetailView.as_view(),name='detail_acc'),
    path('delete_acc/<int:pk>/',AccountDeleteView.as_view(),name='delete_acc'),
    path("chart/", views.bar_chart_expense, name="chart"),
    path("receipt/",ReceiptListView.as_view(), name="receipt")
  # URL for general chart
    # path("user_chart/", views.user_specific_chart, name="user_chart"),


    
    
]