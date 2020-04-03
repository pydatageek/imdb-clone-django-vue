import random
import string

from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def video_code(url):
    """
    it returns video specific code from url to be used in apps easily
    e.g. for a youtube video it is: 695y8rdHsA4
    """
    if url is None or str(url).strip() == '':
        return 'no-video'
    elif str(url).find('watch?v='):  # for youtube videos
        splitted = url.split('watch?v=')[1]
        if splitted.find('&'):
            code = splitted.split('&')[0]
        else:
            code = splitted
        return code


def age(birth_date):
    today = timezone.now()
    age = today.year - birth_date.year - \
        ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def random_name(num):
    """e.g. print(random_name(num), file=sys.stderr)"""
    return ''.join(["{}".format(
        random.choice(string.ascii_lowercase + string.digits))
        for _ in range(num)])
