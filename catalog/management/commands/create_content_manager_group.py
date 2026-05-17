from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Создаёт группу контент-менеджеров'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Контент-менеджер')

        permissions = Permission.objects.filter(codename__in=[
            'add_blogpost',
            'change_blogpost',
            'delete_blogpost',
            'view_blogpost',
        ])

        group.permissions.set(permissions)
        self.stdout.write(self.style.SUCCESS('Группа "Контент-менеджер" создана!'))