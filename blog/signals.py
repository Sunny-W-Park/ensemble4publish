from django.db.models.signals import post_save
from django.dispatch import receiver
from blog.models import Post, Order

@receiver(post_save, sender=Order)
def order_post_save(sender,  **kwargs):
    post = kwargs['instance'].post
    post.call += int(Order.quantity)
    post.save()

