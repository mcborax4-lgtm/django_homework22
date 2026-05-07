from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Заполняет базу тестовыми данными'

    def handle(self, *args, **options):
        # Удаляем старые данные
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write('Старые данные удалены')

        # Создаём категории
        cat1 = Category.objects.create(name='Электроника', description='Электронные устройства')
        cat2 = Category.objects.create(name='Одежда', description='Одежда и аксессуары')

        # Создаём продукты
        Product.objects.create(name='Телефон', description='Смартфон', category=cat1, price=50000)
        Product.objects.create(name='Ноутбук', description='Игровой ноутбук', category=cat1, price=100000)
        Product.objects.create(name='Футболка', description='Хлопковая футболка', category=cat2, price=1500)

        self.stdout.write(self.style.SUCCESS('База успешно заполнена!'))