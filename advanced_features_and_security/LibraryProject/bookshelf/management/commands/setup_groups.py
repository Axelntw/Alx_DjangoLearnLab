from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Creates default groups and permissions'

    def handle(self, *args, **options):
        # Create groups
        editor_group, _ = Group.objects.get_or_create(name='Editors')
        viewer_group, _ = Group.objects.get_or_create(name='Viewers')
        admin_group, _ = Group.objects.get_or_create(name='Admins')

        # Get content type for Book model
        book_content_type = ContentType.objects.get_for_model(Book)

        # Assign permissions to groups
        editor_permissions = Permission.objects.filter(
            content_type=book_content_type,
            codename__in=['can_edit', 'can_create', 'can_view']
        )
        editor_group.permissions.set(editor_permissions)

        viewer_permissions = Permission.objects.filter(
            content_type=book_content_type,
            codename='can_view'
        )
        viewer_group.permissions.set(viewer_permissions)

        # Admins get all permissions
        admin_permissions = Permission.objects.filter(content_type=book_content_type)
        admin_group.permissions.set(admin_permissions)

        self.stdout.write(self.style.SUCCESS('Successfully set up groups and permissions'))
