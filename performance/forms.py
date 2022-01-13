from django.forms import ModelForm, NumberInput, TextInput, Textarea, TimeInput, DateTimeInput, Select

from performance.models import Performance, Rating, Genre, Poster


class PerformanceForm(ModelForm):
    class Meta:
        model = Performance
        fields = ['name', 'rating_id', 'description', 'author', 'duration', 'genre_id', 'price']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            'rating_id': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            'author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Author'
            }),
            'duration': TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duration'
            }),
            'genre_id': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price'
            })
        }


class PerformanceOnGoingForm(ModelForm):
    class Meta:
        model = Poster
        fields = ['performance_id', 'date', 'hall_id']
        widgets = {
            'performance_id': Select(attrs={
                'class': 'form-control'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date and time yyyy-mm-dd hh:mm'
            }),
            'hall_id': Select(attrs={
                'class': 'form-control'
            })
        }
