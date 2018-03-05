from django.contrib import admin
from  django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from django_auth.authuser.models import AuthUser


class AuthUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Passwordconfirmation', widget=forms.PasswordInput)

    class Meta:
        model = AuthUser
        fields = ('email', 'name')

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Password dont match")

        return password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

        return user

class AuthUserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = AuthUser
        fields = ('email', 'name', 'is_admin', 'is_active')

    def clean_password(self):
        return self.initial["password"]

class AuthUserAdmin(BaseUserAdmin):
    form = AuthUserChangeForm
    add_form = AuthUserCreationForm

    list_display = ('email', 'name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields' : ('email', 'password')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'password_confirm')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(AuthUser, AuthUserAdmin)
admin.site.unregister(Group)