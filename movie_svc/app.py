import responder

api = responder.API()


@api.route("/")
def index(req, resp):
    resp.content = api.template("home/index.html")


# Search movies
# GET /api/search/{keyword}
@api.route("/api/search/{keyword}")
def search_by_keyword(req, resp: responder.Response, keyword: str):
    resp.media = {"searching": keyword}


# Movies by director
# GET /api/director/{director_name}
@api.route("/api/director/{director_name}")
def search_by_director(req, resp: responder.Response, director_name: str):
    resp.media = {"searching": director_name}


# Movie by IMDB code
# GET /api/movie/{imdb_number}
@api.route("/api/movie/{imdb_number}")
def movie_by_imdb(req, resp: responder.Response, imdb_number: str):
    resp.media = {"searching": imdb_number}


api.run()
