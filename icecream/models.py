from django.db import models
from django.utils import timezone
# Create your models here.
CHO = 'CHOCOLATE'
VAN = 'VANILLA'

DAI = 'DAILY'
WEE = 'WEEKLY'
SEA = 'SEASONAL'


class IceCream(models.Model):
    flavor_text = models.CharField(max_length=30)
    base = [
        (CHO, 'Chocolate'),
        (VAN, 'Vanilla'),
    ]
    available = [
        (DAI, 'Daily'),
        (WEE, 'Weekly'),
        (SEA, 'Seasonal'),
    ]
    featured = models.BooleanField(default=False)
    date_churned = models.DateTimeField('date churned', default=timezone.now)

    def __str__(self):
        return self.flavor_text
#
# class Choice(models.Model):
#      flavor = models.ForeignKey(IceCream, on_delete=models.CASCADE)
#      choice_text = models.CharField(max_length=30)



#     CHOCOLATE = "Chocolate"
#     VANILLA = "Vanilla"
#     BASE_CHOICES = [
#         (CHOCOLATE, 'Chocolate'),
#         (VANILLA, 'Vanilla'),
#     ]
#     base = models.CharField(
#     max_length=30,
#     choices=BASE_CHOICES,
#     default=CHOCOLATE,
#     )
#
#     def is_flavor(self):
#         return  self.base in (self.CHOCOLATE, self.VANILLA)
    # base: CharField with choices (chocolate, vanilla)
    # available = CharField with choices (daily, weekly, seasonal)
    # featured = BoolField
    # date_churned = DateField
