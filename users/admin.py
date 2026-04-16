from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Role,UserRole


# * 

# * INTERFAZ DE ADMINISTACION PARA GESTIONAR LOS USUARIOS Y LOS ROLES
# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'first_name', 'last_name')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'customers', 'suppliers', 'materials', 'purchases', 'sales')
    list_filter = ('customers', 'suppliers', 'materials', 'purchases', 'sales')
    search_fields = ('role_name',)

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('get_username', 'get_role_name')
    list_filter = ('role',)
    search_fields = ('user_id__username', 'role__role_name')

    def get_username(self, obj):
        return obj.user_id.username
    get_username.short_description = 'Username'

    def get_role_name(self, obj):
        return obj.role.role_name
    get_role_name.short_description = 'Role Name'


"""  CREAR USUARIO Y ROL DESDE LA SHELL DE DJANGO
>>> from users.models import Role
>>> admin_role = Role.objects.create(role_name='Administrator',customers=2,suppliers=2,materials=2,purchases=2,sales=2,inventory=2,accounting=2,reporting=2)
>>> sales_role = Role.objects.create(role_name='Sales Representative',customers=2,sales=2,inventory=1,reporting=1)


 """