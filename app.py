
from flask import Flask
from flask_restx import Api
from flask_cors import CORS, cross_origin

# ROUTES

from routes.ipfs import api as ipfs_api

app = Flask(__name__)

cors = CORS(app, supports_credentials=True)

api = Api()
api = Api(version = '0.9.1', 
          title = 'hesychasm', 
          description= 'A serverless API for managing IPFS Content Identifiers (CIDs)',
          contact='hicetnunc2000@protonmail.com')

# NAMESPACES

api.add_namespace(ipfs_api)

api.init_app(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)