#!/usr/bin/python
import flask  #web frame work to build web app( HTTP requests and rendering templates.)
from flask import request, jsonify

app = flask.Flask(__name__)  ##Create a flask application object
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Hi Python!</h1>"

	
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>` resource could not be found.</p>", 404

if __name__ == '__main__':  # Script executed directly?
    print("Hello World! Built with a Docker file.")
    app.run(host="0.0.0.0", port=5000, debug=True,use_reloader=True) 

	##maintaining host as 0.0.0.0 ensures that this application when deployed into a pod,cna be invoked using the load balancer route of openshift









