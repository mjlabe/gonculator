import os
import argparse
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gonculator.settings")
import django

from django.contrib.auth import get_user_model

django.setup()

# Define the parser
parser = argparse.ArgumentParser(description='get env path')
# Declare an argument (`--algo`), telling that the corresponding value should be stored in the `algo` field
parser.add_argument('--env', action="store", dest='env', default='.')
# Now, parse the command line arguments and store the values in the `args` variable
args = parser.parse_args()


def read_env():
    su = {}
    env = open(args.env)
    for line in env:
        k = line.split('=')[0]
        k = k[:len(k)-1]
        v = line.split('=')[1]
        su[k] = v
    return su


def create_su():
    su = args.env.split('=')[1]
    user = get_user_model()
    if not user.objects.filter(username=su['username']).exists():
        user.objects.create_superuser(su['username'], su['email'], su['password'])


def main():
    """
    Entry to War Card Game simulation.

    :return: None
    """
    create_su()


if __name__ == "__main__":
    main()
