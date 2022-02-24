from decouple import config
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create admin user if it does not exist"

    def handle(self, *args, **options):
        ADMIN_USERNAME = config("ADMIN_USERNAME", default=None)
        ADMIN_PASSWORD = config("ADMIN_PASSWORD", default=None)

        if not ADMIN_USERNAME or not ADMIN_PASSWORD:
            return

        if User.objects.filter(is_staff=True).count() == 0:
            user = User.objects.create_superuser(
                username=ADMIN_USERNAME,
                password=ADMIN_PASSWORD,
                email="",
            )

            self.stdout.write(f"Admin user created")
