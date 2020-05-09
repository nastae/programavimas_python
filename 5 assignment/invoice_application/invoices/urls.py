from django.urls import path
from invoices.views import (InvoiceCreateView, FormCreateView, FormListView,
                            FormDetailsView, GeneratePDF, FormUpdateView, InvoiceUpdateView)

urlpatterns = [
    path("form/create", FormCreateView.as_view(), name='form-create'),
    path("form/<int:pk>/update", FormUpdateView.as_view(), name='form-update'),
    path("form/pdf/<int:pk>/", GeneratePDF.as_view(), name='form-in-pdf'),
    path("form/list", FormListView.as_view(), name='form-list'),
    path("form/<int:pk>/", FormDetailsView.as_view(), name='form-details'),
    path("form/<int:pk>/invoice/create", InvoiceCreateView.as_view(), name='invoice-create'),
    path("form/invoice/<int:pk>/update", InvoiceUpdateView.as_view(), name='invoice-update')
]