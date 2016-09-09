from flask import Flask, request
import json
import logging
import os

logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
port = int(os.getenv("PORT", 5000))

# Can check header X-Broker-Api-Version for match.
# Send "412 Precondition Failed" if rejecting for incompat version.
# request.headers.get('your-header-name')

# Authentication
# Cloud Controller authenticates with the Broker using HTTP basic authentication (the Authorization: header) on every request and will reject any broker registrations that do not contain a username and password. The broker is responsible for checking the username and password and returning a 401 Unauthorized message if credentials are invalid. Cloud Controller supports connecting to a broker using SSL if additional security is desired.
# For now, since I don't have user/pass backend set up, let's just skip it.
# Maybe print out the stuff.

def read_catalog():
    with open("catalog.json") as catalog_file:
        return catalog_file.read()

CATALOG = read_catalog()

@app.route("/v2/catalog")
def catalog():
    return CATALOG

@app.route("/v2/service_instances/<string:instance_id>", methods=["PUT"])
def create_service_instances(instance_id):
    body = request.get_json()
    # FIXME should check body['service_id'] and body['plan_id'] for valid catalog entries.
    return json.dumps({}), 201

@app.route("/v2/service_instances/<string:instance_id>", methods=["PATCH"])
def update_service_instances(instance_id):
    body = request.get_json()
    # FIXME should check body['service_id'] and body['plan_id'] for valid catalog entries.
    return json.dumps({}), 200

@app.route("/v2/service_instances/<string:instance_id>/service_bindings/<string:binding_id>", methods=["PUT"])
def bind(instance_id, binding_id):
    # FIXME return 409 if binding exists.
    return json.dumps(
        {
            # FIXME should read this from environment...or perhaps parameters to cf create-service.
            'credentials':
            {
                'uri': 'http://echo-app-1.bosh-lite.com/echo'
            }
        }
    ), 201

@app.route("/v2/service_instances/<string:instance_id>/service_bindings/<string:binding_id>", methods=["DELETE"])
def unbind(instance_id, binding_id):
    # FIXME return 410 if binding does not exist.
    return json.dumps({}), 200

@app.route("/v2/service_instances/<string:instance_id>", methods=["DELETE"])
def deprovision(instance_id):
    # FIXME return 410 if service instance does not exist.
    return json.dumps({}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
