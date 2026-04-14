 # * DEFINIR LOS PERMISOS DE USUARIO SEGUN LOS ROLES

from users.models import UserRole

def get_permissions(request):

    permissions = { # ? asume por defecto que el valor de cada modulo es 0
        'customers': 0,
        'suppliers': 0,
        'materials': 0,
        'purchases': 0,
        'sales': 0,
        'inventory': 0,
        'accounting': 0,
        'reporting': 0,
    }

    roles = []

# ? luego verifica si el usuario esta autenticado
    if request.user.is_authenticated:
        
        user_roles = UserRole.objects.filter(user_id=request.user.pk)

        roles = [ur-role.role_name for ur in user_roles]
        for user_role in user_roles: # ? va recorriendo 1 a 1 cada modulo
            role = user_role.role
            for module in permissions.keys():
                current_permission = getattr(role,module,0)
                if current_permission > permissions[module]:
                    permissions[module] = current_permission
    
     # ? nos retorna el permiso para cada modulo
    return {'permissions': permissions, 'roles': roles}


