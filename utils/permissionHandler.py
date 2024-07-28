from .jsonHandler import get_jason_filepath, JSONHandler

class PermissionManager:
    def __init__(self):
        self.users_handler = JSONHandler(get_jason_filepath("users.json"), custom_name="PM_Users")
        self.roles_handler = JSONHandler(get_jason_filepath("roles.json"), custom_name="PM_Roles")
    
    def has_permission(self, username, permission_path):
        # Load users and roles data
        users = self.users_handler.data
        roles = self.roles_handler.data
        
        # Check if user exists
        if username not in users:
            return False
        
        # Get user's role
        user_role = users[username]['role']
        
        # Check if role exists in roles
        if user_role not in roles:
            print("Role does not exist")
            return False
                
        # Split the permission path by dot
        permission_keys = permission_path.split('.')
        
        # Traverse the permission path to find the permission
        permissions = roles[user_role]
        for key in permission_keys:
            if key in permissions:
                permissions = permissions[key]
            else:
                return False
        
        return permissions == True
    
    def update_permission(self, role, permission_path, value):
        # Load roles data
        roles = self.roles_handler.data
        
        # Check if role exists
        if role not in roles:
            return f"Role '{role}' not found."
        
        # Split the permission path by dot
        permission_keys = permission_path.split('.')
        
        # Traverse the permission path to set the new value
        permissions = roles[role]
        for key in permission_keys[:-1]:
            if key not in permissions:
                permissions[key] = {}
            permissions = permissions[key]
        
        # Set the final key to the new value
        permissions[permission_keys[-1]] = value
        
        # Write the updated roles back to the JSON file
        result = self.roles_handler.write_json(roles)
        if "Error" in result:
            return result
        return f"Permission '{permission_path}' for role '{role}' updated to {value}."