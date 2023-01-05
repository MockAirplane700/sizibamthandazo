import json
from flask_restful.utils import cors

from logic.ars_corpia_logic.artist_logic import ArtistSingleton
from logic.ars_corpia_logic.corpia_logic import CorpiaSingleton
from logic.projects_logic import ProjectsSingleton
from logic.stories_logic import StoriesSingleton
from flask import Flask, request, render_template, abort, jsonify
from flask_restful import Resource, Api, reqparse
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config= {'CACHE_TYPE':'SimpleCache'})
api = Api(app)

parser = reqparse.RequestParser()


class Stories(Resource):

    @cors.crossdomain(origin='*')
    @cache.memoize(50)
    def get(self):
        db = StoriesSingleton()
        result = db.get_all_stories()
        return result


class Projects(Resource):
    @cors.crossdomain(origin='*')
    @cache.memoize(50)
    def get(self):
        db = ProjectsSingleton()
        result = db.get_all_projects()
        return result


class Corpia(Resource):
    @cors.crossdomain(origin='*')
    @cache.memoize(50)
    def get(self):
        db = CorpiaSingleton()
        result = db.get_all_corpia()
        return result


class Artist(Resource):
    @cors.crossdomain(origin='*')
    @cache.memoize(50)
    def get(self):
        db = ArtistSingleton()
        result = db.get_all_artists()
        return result


@app.route('/')
def index_page():
    return render_template("index.html")


@app.route("/projects")
def artist_page():
    return render_template("projects.html")


@app.route("/stories")
def corpia_page():
    return render_template("stories.html")


@app.route('/index')
def index_page_corpia():
    return render_template("templates/ars_corpia_templates/index.html")


@app.route("/artist")
def artist_page():
    return render_template("templates/ars_corpia_templates/artist.html")


@app.route("/coripa")
def corpia_page():
    return render_template("templates/corpia.html")


api.add_resource(Stories, "/api/stories")
api.add_resource(Projects, "/api/projects")

api.add_resource(Corpia, "/ars-corpia/api/corpia")
api.add_resource(Artist, "/ars-corpia/api/artists")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, threaded=True)
