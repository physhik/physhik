from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms

from .models import Post


class ContactForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.form_method = "post"
        self.helper.form_action = "/contact/"
        self.helper.form_class = "form-group"
        self.helper.form_id = "contact-form"

        self.helper.add_input(Submit("submit", "Submit"))

    name = forms.CharField(
        max_length=100,
        label="Your name",
        widget=forms.TextInput(attrs={"class": "col", "placeholder": "Namshik Kim"}),
    )
    email = forms.CharField(
        label="Your email",
        widget=forms.EmailInput(
            attrs={"class": "col", "placeholder": "physhik@gmail.com"},
        ),
    )
    message = forms.CharField(
        max_length=500,
        label="Your inquiry",
        widget=forms.Textarea(attrs={"placeholder": "I need to..."}),
    )


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "slug",
            "overview",
            "body",
            "image",
            "created_on",
            "updated_on",
            "categories",
            "status",
        ]
        widgets = {
            "created_on": forms.DateInput(attrs={"type": "date"}),
            "updated_on": forms.DateInput(attrs={"type": "date"}),
        }
