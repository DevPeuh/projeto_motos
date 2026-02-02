from django.db import models


class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150) # Nome que vai ser exibido na tela

    def __str__(self): # Retorna o nome da marca
        return self.name

class Bike(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=100) # Modelo do moto
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='bike_brands') # vai fazer a relação com a tabela Brand, ter proteção para não exluir a marca.
    factory_year = models.IntegerField(blank=True, null=True) # Ano de fabricação podendo ser nulo
    model_year = models.IntegerField(blank=True, null=True) # Ano do modelo podendo ser nulo
    plate = models.CharField(max_length=10, blank=True, null=True) # Placa da moto podendo ser nulo
    value = models.FloatField(blank=True, null=True) # Valor da moto podendo ser nulo
    photo = models.ImageField(upload_to='bikes/', blank=False, null=False) # Foto da moto salva no diretório bikes
    

    def __str__(self): # Retorna o modelo da moto
        return self.model 
    
