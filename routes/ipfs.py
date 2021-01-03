from flask import request
from flask_restx import fields, Resource, Namespace
from werkzeug import FileStorage
from libs.validate import Validate

import ipfshttpclient

api = Namespace('ipfs')
upload_parser = api.parser()
upload_parser.add_argument('file', location='files',
                           type=FileStorage, required=True)

conn = ipfshttpclient.connect('/dns4/ipfs.infura.io/tcp/5001/https')

v = Validate()

@api.route('/post_file')
@api.expect(upload_parser)
class post_file(Resource):
    @api.expect(type)
    def post(self):
        try:
            args = upload_parser.parse_args()
            cid = conn.add_bytes(args['file'].read())
            return {'result': cid}
        except:
            return 500

@api.route('/post_json')
class post_json(Resource):
    def post(self):
        try:
            payload = v.read_requests(request)
            cid = conn.add_json(payload)
            return {'result': cid}
        except:
            return 500

@api.route('/get_json')
@api.doc(params={
    'cid': 'CID hash'
})
class get_json(Resource):
    def post(self):
        try:
            payload = v.read_requests(request)
            json = conn.get_json(payload['cid'])
            return {'result': json}
        except:
            return 500
