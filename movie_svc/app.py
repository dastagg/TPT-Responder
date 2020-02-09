from api_instance import api
from data import db
from views.api_views import *
from views.home import *


def main():
    db.global_init()

    api.run()


if __name__ == "__main__":
    main()
