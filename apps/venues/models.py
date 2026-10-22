#Импортирует инструменты Django ORM , с помощью которых ты описываешь поля таблиц. 
from django.db import models
#Валидатор который проверяет , что число не меньше указанного значение. 

from django.core.validators import MinValueValidator
# Create your models here.

#Venue описывает место проведения мероприятия. 
class Venue(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)

    capacity=models.PositiveIntegerField(validators=[MinValueValidator(1)])
    
    is_active = models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)

    #Additional settings
    class Meta:
        #сортирует по city затем , если несколько то затем name.
        ordering=["city", "name"]
        verbose_name="Venue" #название модели в единственным число
        verbose_name_plural="Venues" #название модели в множественном числе

        #Помогает проверять комбинации несколько полей.
        constraints = [
            models.UniqueConstraint(
                fields=["name", "address", "city"],
                name="unique_venue_location",
            ),
        ]
  
    def __str__(self):
        return f"{self.name}, {self.city}"
# удобный представление объекта. 
