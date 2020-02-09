from api_instance import api


@api.route("/")
def index(_, resp):
    resp.content = api.template("home/index.html")
