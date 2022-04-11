from flask import request
from flask_restx import fields, Resource, Namespace
from werkzeug import FileStorage
from libs.validate import Validate

import ipfshttpclient
import json
import os

api = Namespace('ipfs')
upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

conn = ipfshttpclient.connect('/dns4/ipfs.infura.io/tcp/5001/https')

v = Validate()


@api.route('/post_file')
class post_file(Resource):
    def post(self):

        payload = v.read_requests(request)
        cid = conn.add_bytes(payload['buffer'])

        return { 'result' : cid['Hash'] }


@api.route('/post_json')
class post_json(Resource):
    def post(self):
        try:
            payload = v.read_requests(request)
            cid = conn.add_json(payload)
            return { 'result' : cid }
        except:
            return 500


@api.route('/read_cid')
@api.doc(params={
    'cid': 'IPFS CID hash'
})
class read_cid(Resource):
    def post(self):
        try:
            payload = v.read_requests(request)
            j = conn.get_json(payload['cid'])
            return { 'result' : j }
        except:
            return 500
