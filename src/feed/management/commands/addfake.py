from django.core.management.base import BaseCommand
from src.profiler.models import UserNet
from src.followers.models import Follower
from src.wall.models import Post
import random


class Command(BaseCommand):
    """command to create db elements for test workability
    """
    def handle(self, *args, **options):
        self.create_user()
        self.create_follower()
        self.create_posts()
        self.stdout.write("Success")

    def create_user(self):
        for i in range(10):
            user = UserNet(
                username=f"testuser{i}",
                middle_name=f"test {i}",
                email=f"test{i}mail@rtf.oo",
                is_active=True,
                phone=f"1234567891{i}",
                gender=1
            )
            user.set_password('4321qwer')
            user.save()

    def make_subs(self, list_users, owner):
        """we know list_user != 0 ,  list.len  > 1
        """

    def create_follower(self):
        user_list = UserNet.objects.order_by()
        for user in user_list:
            for el in user_list:
                if random.randint(0, 1) == 1:
                    if not el == user:
                        Follower.objects.create(user=el, follower_id=user.id)

    def create_posts(self):
        user_list = UserNet.objects.order_by()[2:]
        for user in user_list:
            for i in range(10):
                Post.objects.create(text=f"testpost {i} from user {user}", user=user)

