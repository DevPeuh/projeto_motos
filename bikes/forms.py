from django import forms
from .models import Bike

    
class BikeModelForm(forms.ModelForm):

    class Meta:
        model = Bike
        fields = '__all__'
        
    def clean_value(self):
        value = self.cleaned_data.get('value') #cleaned_data traz os dados limpos do formulário

        if value is not None and value < 0:
            self.add_error('value', 'O valor não pode ser negativo.')  # Adiciona um erro no campo 'value'
        
        elif value < 10000:
            self.add_error('value', 'O valor da moto deve ser maior ou igual a R$10.000.')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')

        if factory_year is not None and factory_year < 1980:
            self.add_error('factory_year', 'O ano de fabricação não pode ser anterior a 1980.')
        return factory_year

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')

        if photo is None:
            self.add_error('photo', 'A foto é obrigatória.')
        return photo
    
    def clean_plate(self):
        plate = self.cleaned_data.get(self)

        if plate is not None and len(plate) < 7:
            self.add_error('plate', 'A placa deve ter pelo menos 7 caracteres.')
        return plate
    
    