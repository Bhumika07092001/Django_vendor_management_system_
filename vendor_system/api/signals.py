from django.db.models.signals import post_save
from django.utils import timezone
from django.dispatch import receiver
from .models import PurchaseOrder, HistoricalPerformance, Vendor

@receiver(post_save, sender=PurchaseOrder)
def calculate_on_time_delivery_rate(sender, instance, created, **kwargs):
    if instance.status == 'completed':
        current = timezone.now()
        completed_orders = PurchaseOrder.objects.filter(
            vendor=instance.vendor,
            delivery_date__lte = current
        ).count()
        total_completed_orders = PurchaseOrder.objects.filter(
            vendor=instance.vendor,
            status='completed'
        ).count()
        if total_completed_orders > 0:
            on_time_delivery_rate = (completed_orders / total_completed_orders) * 100
            instance.vendor.on_time_delivery_rate = on_time_delivery_rate
            instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def calculate_quality_rating_average(sender, instance, created, **kwargs):
    if instance.status == 'completed' and instance.quality_rating is not None:
        completed_orders = PurchaseOrder.objects.filter(
            vendor=instance.vendor,
            status='completed',
            quality_rating__isnull=False 
        )
        total_quality_ratings = sum(order.quality_rating for order in completed_orders)
        total_completed_orders = completed_orders.count()
        if total_completed_orders > 0:
            average_quality_rating = total_quality_ratings / total_completed_orders
            instance.vendor.quality_rating_avg = average_quality_rating
            instance.vendor.save()

@receiver(post_save, sender=PurchaseOrder)
def calculate_average_response_time(sender, instance, created, **kwargs):
    if instance.acknowledgment_date is not None:  
        acknowledged_orders = PurchaseOrder.objects.filter(
            vendor=instance.vendor,
            acknowledgment_date__isnull=False 
        )
        
        total_response_time = sum(
            (order.acknowledgment_date - order.issue_date).total_seconds() 
            for order in acknowledged_orders
        )
        
        total_acknowledged_orders = acknowledged_orders.count()
        if total_acknowledged_orders > 0:
            average_response_time = total_response_time / total_acknowledged_orders
            instance.vendor.response_time_rate = average_response_time
            instance.vendor.save()


@receiver(post_save, sender=PurchaseOrder)
def calculate_fulfillment_rate(sender, instance, created, **kwargs):
    all_orders = PurchaseOrder.objects.filter(vendor=instance.vendor)
    total_orders = all_orders.count()
    fulfilled_orders = all_orders.filter(status='completed').count()
    if total_orders > 0:
        fulfillment_rate = (fulfilled_orders / total_orders) * 100
        instance.vendor.fulfillment_rate = fulfillment_rate
        instance.vendor.save()

@receiver(post_save, sender=Vendor)
def update_historical_performance(sender, instance, created, **kwargs):
    if not created:
        if HistoricalPerformance.objects.filter(vendor=instance).exists():
            historical_performance = HistoricalPerformance.objects.get(vendor=instance)
            historical_performance.date = timezone.now()
            historical_performance.on_time_delivery_rate = instance.on_time_delivery_rate
            historical_performance.quality_rating_avg = instance.quality_rating_avg
            historical_performance.average_response_time = instance.response_time_rate
            historical_performance.fulfillment_rate = instance.fulfillment_rate
            historical_performance.save()
        else:
            HistoricalPerformance.objects.create(
                vendor=instance,
                date=timezone.now(),
                on_time_delivery_rate=instance.on_time_delivery_rate,
                quality_rating_avg=instance.quality_rating_avg,
                average_response_time=instance.response_time_rate,
                fulfillment_rate=instance.fulfillment_rate
            )

        

