from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'
    verbose_name = 'Blog Configuration for Order'
    #def ready(self):
    #    import blog.signals
