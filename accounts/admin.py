from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UsuarioPersonalizado

# Register your models here.
class CustomUserAdmin(UserAdmin):
    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UsuarioPersonalizado
    
    list_display = ['name', 'middle_name', 'last_name', 'email', 'username', 'is_staff',]
    
    # fieldsets (for fields to be used in editing users)
    fieldsets = UserAdmin.fieldsets + ( # new
    (
        None, {'fields': ('name',)}),
    )

    # add_fieldsets (for fields to be used when creating a user)
    add_fieldsets = UserAdmin.add_fieldsets + ( # new
    (
        None, {'fields': ('name',)}),
    )

admin.site.register(UsuarioPersonalizado, CustomUserAdmin)
