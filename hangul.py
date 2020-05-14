import random

def random_hangul(length):
    random_unicodes = [chr(random.randrange(0xAC00, 0xD7Af)) for _ in range(0, length)]
    return u"".join(random_unicodes)