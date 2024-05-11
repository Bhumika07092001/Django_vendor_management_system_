from django.contrib import admin
from django.urls import path
from .views import VendorList,VendorDetail,PurchaseOrderList,PurchaseOrderDetail,VendorPOAcknowledgmentView,VendorPerformanceView

urlpatterns = [
    path('vendors/',VendorList.as_view(),name='vendorList'),
    path('vendors/<int:pk>/', VendorDetail.as_view(),name='vendorDetail'),
    path('vendors/<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor_performance'),
    path('vendors/<int:vendor_id>/acknowledge_po/<int:po_id>/', VendorPOAcknowledgmentView.as_view(), name='acknowledge_po'),
    path('purchase_orders/',PurchaseOrderList.as_view(),name='purchaseOrderList'),
    path('purchase_orders/<int:pk>/', PurchaseOrderDetail.as_view(),name='purchaseOrderDetail'),
]
