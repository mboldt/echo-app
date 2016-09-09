from flask import Flask, request
import json
import os
import requests

app = Flask(__name__)
port = int(os.getenv("PORT", 5001))

# For testing:
# User-provided service:
# VCAP_SERVICES='{"user-provided":[{"name":"echo_service","label":"user-provided","tags":[],"credentials":{"uri":"http://echo-app-1.bosh-lite.com/echo"},"syslog_drain_url":""}]}'
# Brokered service:
# VCAP_SERVICES='{"echo-service": [{"credentials": {"uri": "http://echo-app-1.bosh-lite.com/echo"}, "label": "echo-service", "name": "echo-service-1", "plan": "basic", "provider": null, "syslog_drain_url": null, "tags": [], "volume_mounts": []}]}'


print os.getenv('VCAP_SERVICES')

def get_echo_service_uri():
    vcs = json.loads(os.getenv('VCAP_SERVICES'))
    if 'user-provided' in vcs:
        for service in vcs['user-provided']:
            if service['name'] == 'echo_service':
                return service['credentials']['uri']
    if vcs.get('echo-service', False):
        return vcs['echo-service'][0]['credentials']['uri']

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/reverse")
def reverse():
    return ''.join(reversed(request.args.get('data', '')))

@app.route("/echo")
def echo():
    uri = get_echo_service_uri()
    r = requests.get(uri, request.args)
    return r.text

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=port)
