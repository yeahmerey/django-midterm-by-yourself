from django.db import models
from django.utils.text import slugify
#slugify используется чтобы простой строка перевести на URL формат то есть если Django Applicaton , django-application
# Create your models here.

#null=True , разрешить хранить NULL в базы данных 
#blank=True , разрешает оставлять поле пустым при проверке Django-form
#default=True , задает значение по умолчанию
#unique=True, запрещает дублирование в таблице
#models.Model - базовый класс Django , который предоставляет функциональность для работы с базы данных

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    #slug это текстовый идентификатор, удобный для использование в URL
    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True)
    description = models.TextField(
        blank=True
    )
#дополнительный настройки модели
    class Meta:
        ordering=["name"]
        #-name - sort desc
        verbose_name="Category"
        verbose_name_plural="Categories"

#*args - позволяет функции принимать любое кол:во дополнительных аргументов
#args - тип данных tuple будет принимать
#и также тут используется kwargs
#*args и *kwargs - без них работает тоже , но если вдруг метод save()поддерживает доп параметры. 
#Если их не будет не будет принимать доп параметры.
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)

        super().save(*args, **kwargs)

    #Как объект будет отображаться в виде строки. Если не исользовать может быть <Category: Category object (1)>    
    def __str__(self):
        return self.name
#Если мы создаем объект от этого класса , и сделаем просто print(имя_объекта) то выходить : Category object(1)
#А если использовать в нашем случае дает name