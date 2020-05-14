import random

def random_error(length):
    random_unicodes = [chr(random.randrange(0x1041, 0x10aa)) for _ in range(0, length)]
    return u"".join(random_unicodes)
