import random

def random_dingbats(length):
    random_unicodes = [chr(random.randrange(0x2702, 0x27B0)) for _ in range(0, length)]
    return u"".join(random_unicodes)