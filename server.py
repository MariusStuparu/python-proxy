#!/usr/bin/python3
"""
Proxy server to bypass CORS restrictions and access
TeamCity and Jira API endpoints
"""
from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
import xmltodict
from xml.parsers import expat
import os

application = Flask(__name__)
CORS(application)
api = Api(application)

otherServerUrl = 'http://something'

class Endpoint(Resource):
    """Get the projects list from TeamCity using cURL"""

    @cross_origin()
    def get(self, parameterName = None):
        if not parameterName:
            cUrlPath = '{0}/some-url'.format(otherServerUrl)
        else:
            cUrlPath = '{0}/some-url/{1}'.format(otherServerUrl, str(parameterName))

        try:
            xmlResponse = os.popen('curl -H "Authorization: Bearer {0}" {1}'.format('', cUrlPath)).read()
            jsonResponse = xmltodict.parse(xmlResponse)
        except expat.ExpatError as parseError:
            print('XML Parse Error: {0}'.format(parseError))
        else:
            return jsonify(xmlResponse)

"""Add the routes"""
api.add_resource(Endpoint, '/api/endpoint/', '/api/endpoint/<string:parameterName>')

"""Run the server"""
if __name__ == '__main__':
    application.run(host='0.0.0.0', port='5002')
