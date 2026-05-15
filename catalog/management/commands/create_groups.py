from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product

class Command(BaseCommand):
    help = 'Создание групп с правами'

    def handle(self, *args, **options):
        moderators, created = Group.objects.get_or_create(name='Модератор продуктов')
        if created:
            permissions = Permission.objects.filter(codename__in=['can_unpublish_product', 'delete_product'])
            moderators.permissions.set(permissions)
            self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" создана и права назначены'))
        else:
            self.stdout.write(self.style.WARNING('Группа "Модератор продуктов" уже существует'))
