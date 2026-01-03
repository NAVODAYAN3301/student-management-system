import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser if none exists'

    def handle(self, *args, **options):
        User = get_user_model()
        
        if User.objects.filter(is_superuser=True).exists():
            self.stdout.write(
                self.style.SUCCESS('Superuser already exists.')
            )
            return
        
        # Get credentials from environment variables or use defaults
        email = os.environ.get('SUPERUSER_EMAIL', 'admin@gmail.com')
        password = os.environ.get('SUPERUSER_PASSWORD', 'admin')
        first_name = os.environ.get('SUPERUSER_FIRST_NAME', 'Admin')
        last_name = os.environ.get('SUPERUSER_LAST_NAME', 'User')
        
        try:
            superuser = User.objects.create_user(
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                user_type=1,  # Admin user type
                is_staff=True,
                is_superuser=True,
                is_active=True
            )
            
            self.stdout.write(
                self.style.SUCCESS(f'Superuser created successfully: {email}')
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error creating superuser: {str(e)}')
            )