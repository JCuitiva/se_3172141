from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm

from .models import Usuarios

class UsuarioCreationForm(AdminUserCreationForm):
    class Meta:
        model = Usuarios
        fields = ("correo",)

    
class UsuarioChangeForm(UsuarioChangeForm):
    class Meta:
        model = Usuarios
        fields = ("correo",)