from django.core import validators
from django import forms

class FormArticle(forms.Form):
    title=forms.CharField(
        label='Titulo',
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Ingresa el titulo',
                'class':'title_from_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñáéóíú ]*$', 'El titulo no puede tener caracteres especiales', 'invalid_title')

        ]
    )

    content=forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(150, 'Mucho texto')
        ]
    )

    content.widget.attrs.update({
        'placeholder': 'Ingresa el contenido',
        'class':'content_from_article',
    })

    public_opcion=[
        (1, 'Todos'),
        (0, 'Nadie')
    ]

    public=forms.TypedChoiceField(
        label = "¿quién puede ver el articulo?",
        choices = public_opcion
    )