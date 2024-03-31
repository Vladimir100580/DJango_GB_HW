from random import choices
from django.core.management.base import BaseCommand
from myapp3.models import Author, Post

LOREM = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Maecenas porttitor congue massa." \
        " Fusce posuere, magna sed pulvinar ultricies, purus lectus malesuada libero, " \
        "sit amet commodo magna eros quis urna. Nunc viverra imperdiet enim. Fusce est." \
        " Vivamus a tellus. Pellentesque habitant morbi tristique senectus et netus et malesuada fames" \
        " ac turpis egestas. Proin pharetra nonummy pede. Mauris et orci. Aenean nec lorem. In porttitor." \
        " Donec laoreet nonummy augue. Suspendisse dui purus, scelerisque at, vulputate vitae, pretium mattis, nunc." \
        " Mauris eget neque at sem venenatis eleifend. Ut nonummy. Fusce aliquet pede non pede." \
        " Suspendisse dapibus lorem pellentesque magna. Integer nulla.Donec blandit feugiat ligula." \
        " Donec hendrerit, felis et imperdiet euismod, purus ipsum pretium metus, in lacinia nulla nisl eget sapien." \
        " Donec ut est in lectus consequat consequat. Etiam eget dui. Aliquam erat volutpat." \
        " Sed at lorem in nunc porta tristique. Proin nec augue. Quisque aliquam tempor magna." \
        " Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. " \
        "Nunc ac magna. Maecenas odio dolor, vulputate vel, auctor ac, accumsan id, felis." \
        " Pellentesque cursus sagittis felis."


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count ID')

    def handle(self, *args, **kwargs):
        text = LOREM.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            author = Author(name=f'Author_{i}', email=f'mail{i}@mail.ru')
            author.save()
            for j in range(1, count + 1):
                post = Post(title=f'Title-{j}', content=" ".join(choices(text, k=64)), author=author)
                post.save()
