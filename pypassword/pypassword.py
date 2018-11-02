import string
import random
import argparse


def password_generator(size=6,
                       chars=string.ascii_letters + string.digits):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))


if __name__ == "__main__":
    size = 14
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", help="Random string size", type=int)

    args = parser.parse_args()
    if args.size:
        size = args.size

    print(password_generator(size=size))
