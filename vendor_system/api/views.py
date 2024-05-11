from rest_framework.views import APIView
from rest_framework import generics 
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.utils import timezone
from .serializers import vendorSerializer, purchaseOrderSerializer, historicalPerformanceSerializer
from .models import Vendor, PurchaseOrder, HistoricalPerformance

class VendorList(APIView):
    def get(self, format=None):
        vendors = Vendor.objects.all()
        serializer = vendorSerializer(vendors, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serialize=vendorSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
        
class VendorDetail(APIView):
    def get_object(self,pk):
        try:
            return Vendor.objects.get(pk=pk)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk,format=None):
        vendor=self.get_object(pk)
        serialize=vendorSerializer(vendor)
        return Response(serialize.data)
    
    def put(self,request,pk,format=None):
        vendor=self.get_object(pk)
        serialize=vendorSerializer(vendor,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk, format=None):
        vendor=self.get_object(pk)
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PurchaseOrderList(generics.ListCreateAPIView):
    serializer_class= purchaseOrderSerializer
    queryset=PurchaseOrder.objects.all()

    def get(self, request, format=None):
        purchaseOrders = PurchaseOrder.objects.all()
        serialize = purchaseOrderSerializer(purchaseOrders, many=True)
        return Response(serialize.data)
    
    def post(self, request, format=None):
        serialize= purchaseOrderSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
        
class PurchaseOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = purchaseOrderSerializer
    queryset = PurchaseOrder.objects.all()

    def get_object(self, pk):
        try:
            return PurchaseOrder.objects.get(pk=pk)
        except PurchaseOrder.DoesNotExist:
            return None

    def retrieve(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if instance:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if instance:
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk, *args, **kwargs):
        instance = self.get_object(pk)
        if instance:
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class VendorPOAcknowledgmentView(APIView):
    def post(self, request, vendor_id, po_id, format=None):
        try:
            po = PurchaseOrder.objects.get(id=po_id, vendor_id=vendor_id)
        except PurchaseOrder.DoesNotExist:
            return Response({'error': 'Purchase order not found'}, status=status.HTTP_404_NOT_FOUND)
        po.acknowledgment_date = timezone.now()
        po.save()
        
        return Response({'success': 'Purchase order acknowledged successfully'}, status=status.HTTP_200_OK)
    

class VendorPerformanceView(APIView):
    def get(self, request, vendor_id, format=None):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            historical_performance = HistoricalPerformance.objects.get(vendor=vendor)
            serializer = historicalPerformanceSerializer(historical_performance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Vendor.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
        except HistoricalPerformance.DoesNotExist:
            return Response({'error': 'Historical performance data not found'}, status=status.HTTP_404_NOT_FOUND)
        
 



