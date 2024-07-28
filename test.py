from utils.permissionHandler import PermissionManager

pm = PermissionManager()

print(pm.has_permission("anadmin123", "builtin.users.profiles.update"))

