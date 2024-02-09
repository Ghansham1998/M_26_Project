from django import forms
from .models import YourModel
# forms.py



class YourModelForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = '__all__'

    def validate_file_extension(value):
        """
        Custom validator to check if the uploaded file has an allowed extension.
        """
        allowed_extensions = ['csv', 'xls', 'xlsx']
        ext = value.name.split('.')[-1]
        if ext not in allowed_extensions:
            raise forms.ValidationError(f'File type not supported. Allowed file types: {", ".join(allowed_extensions)}')

    file = forms.FileField(
        label='Select a CSV or Excel file',
        validators=[validate_file_extension]
    )
