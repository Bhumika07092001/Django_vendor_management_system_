from rest_framework import serializers
from .models import Vendor, PurchaseOrder, HistoricalPerformance

class vendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields='name','contact_details','address'

class purchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=PurchaseOrder
        fields="__all__"

class historicalPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=HistoricalPerformance
        fields="__all__"
