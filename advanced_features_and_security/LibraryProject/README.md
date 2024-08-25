# Permissions System

This application uses a custom permissions system for the Book model.

## Permissions
- can_view: Allows viewing book details
- can_create: Allows creating new books
- can_edit: Allows editing existing books
- can_delete: Allows deleting books

## Groups
- Editors: Can view, create, and edit books
- Viewers: Can only view books
- Admins: Have all permissions

To set up groups and permissions, run:
python manage.py setup_groups

Views are protected with the @permission_required decorator to enforce these permissions.
