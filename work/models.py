from django.db import models


class Order(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    telephone = models.CharField(max_length=11)
    pubDate = models.DateTimeField(auto_now=True)
    viewsCount = models.IntegerField(default=0)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def fill_by_post(POST):
        order = Order()

        for attr_name in order.__dict__:
            attr_val = POST.get(attr_name)

            if not attr_val is None:
                setattr(order, attr_name, attr_val)

        return order
