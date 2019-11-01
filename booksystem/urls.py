from django.urls import path
from . import views

app_name = 'booksystem'

urlpatterns = [
    path('<int:pk>/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/withoutStock/', views.WithoutStockView.as_view(), name='without_stock'),
    path('<int:pk>/backend/', views.BackendView.as_view(), name='backend'),

    path('createAuthor/', views.CreateAuthorView.as_view(), name='create_author'),
    path('createPublisher/', views.CreatePublisherView.as_view(), name='create_publisher'),
    path('createBookType/', views.CreateBookTypeView.as_view(), name='create_book_type'),
    path('createCashier/', views.createCashierView.as_view(), name='create_cashier'),
    path('createBook/', views.createBookView.as_view(), name='create_book'), 

    path('<int:pk>/receipts/', views.receiptsView.as_view(), name='receipts'),
    path('<int:pk>/receipts/settings/', views.ReceiptsSettingsView.as_view(), name='receipts_settings'),
    path('<int:pk>/receipts/last/', views.lastReceiptsView.as_view(), name='last_receipts'),

    path('<int:pk>/shortcuts/', views.ShortCutView.as_view(), name='shortcut_view'),

    path('<int:pk>/endDay/', views.EndDayView.as_view(), name='end_day'),

    path('<int:pk>/reports/', views.ReportsView.as_view(), name='reports_view'),
    path('<int:pk>/reports/addCash/', views.ReportsAddCashView.as_view(), name='reports_add_cash_view'),
    path('<int:pk>/reports/drawCash/', views.ReportsDrawCashView.as_view(), name='reports_draw_cash_view'),
]