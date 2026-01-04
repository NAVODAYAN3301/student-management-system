from django.core.management.base import BaseCommand
from student_management_app.models import CustomUser, Staffs

class Command(BaseCommand):
    help = 'Fix missing staff records'

    def handle(self, *args, **options):
        # Find all staff users without Staff records
        staff_users = CustomUser.objects.filter(user_type=2)
        
        for user in staff_users:
            try:
                staff = Staffs.objects.get(admin=user)
                self.stdout.write(f"Staff record exists for {user.email}")
            except Staffs.DoesNotExist:
                # Create missing staff record
                Staffs.objects.create(admin=user, address="")
                self.stdout.write(f"Created staff record for {user.email}")
        
        self.stdout.write(self.style.SUCCESS('Staff records check completed'))