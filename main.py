from flask_restful.utils import cors
from logic.ars_corpia_logic.artist_logic import ArtistSingleton
from logic.ars_corpia_logic.corpia_logic import CorpiaSingleton
from logic.projects_logic import ProjectsSingleton
from logic.stories_logic import StoriesSingleton
from flask import Flask, request, render_template, abort, jsonify
from flask_restful import Resource, Api, reqparse
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'SimpleCache'})
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


class Paypal(Resource):
    @cors.crossdomain(origin='*')
    def post(self):
        # check if file exists
        file = open('templates/paypal_details.html', 'w')
        data = request.get_data()
        string_data = data.decode('utf-8')
        if string_data.__contains__('\r\n\r\n'):
            string_result = (string_data.split('\r\n\r\n')[1].split('\r\n')[0]).rstrip('\"')
            print(string_result)
            a = string_result
            file.write(' <!DOCTYPE html>\n<html lang="en">\n<head>\n<meta name="viewport" content="width=device-width, initial-scale=1" />\n<meta http-equiv="X-UA-Compatible" content="IE=edge" />\n<title>PayPal Standard Payments Integration | Client Demo</title>\n</head>\n\n<body>\n<div id="paypal-button-container"></div>\n<!-- Sample PayPal credentials (client-id) are included -->\n<script src="https://www.paypal.com/sdk/js?client-id=test&currency=CAD&intent=capture&enable-funding=venmo" data-sdk-integration-source="integrationbuilder"></script>\n<script>\nconst paypalButtonsComponent = paypal.Buttons({\n// optional styling for buttons\n// https://developer.paypal.com/docs/checkout/standard/customize/buttons-style-guide/\nstyle: {\ncolor: "gold",\nshape: "rect",\nlayout: "vertical"\n},\n\n// set up the transaction\ncreateOrder: (data, actions) => {\n// pass in any options from the v2 orders create call:\n// https://developer.paypal.com/api/orders/v2/#orders-create-request-body\nconst createOrderPayload = {\npurchase_units: [\n{\namount: {\nvalue: %a\n}\n}\n]\n};\n\nreturn actions.order.create(createOrderPayload);\n},\n\n// finalize the transaction\nonApprove: (data, actions) => {\nconst captureOrderHandler = (details) => {\nconst payerName = details.payer.name.given_name;\nconsole.log("Transaction completed");\n};\n\nreturn actions.order.capture().then(captureOrderHandler);\n},\n\n// handle unrecoverable errors\nonError: (err) => {\nconsole.error("An error prevented the buyer from checking out with PayPal");\n}\n});\n\npaypalButtonsComponent\n.render("#paypal-button-container")\n.catch((err) => {\nconsole.error("PayPal Buttons failed to render");\n});\n</script>\n</body>\n</html> '%(a))
        file.close()
        return 'OK , 200'


@app.route('/')
def index_page():
    return render_template("index.html")


@app.route("/paypal")
def paypal_page():
    return render_template("paypal_details.html")

@app.route("/projects")
def artist_page():
    return render_template("projects.html")


@app.route("/stories")
def corpia_page():
    return render_template("stories.html")


@app.route('/index')
def index_page_corpia():
    return render_template("templates/ars_corpia_templates/index.html")


api.add_resource(Stories, "/api/stories")
api.add_resource(Projects, "/api/projects")
api.add_resource(Paypal, '/api/paypal')

api.add_resource(Corpia, "/ars-corpia/api/corpia")
api.add_resource(Artist, "/ars-corpia/api/artists")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True)
