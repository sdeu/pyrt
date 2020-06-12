from flask import Flask, abort, send_from_directory
from flask_restful import Resource, Api, reqparse
import werkzeug
import os

UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')
ACCEPTED_FILE_TYPE = 'png'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('file',type=werkzeug.datastructures.FileStorage, location='files')

class Image(Resource):
    def get(self, image_id):
        images = [os.path.splitext(os.path.basename(f))[0] for f in os.listdir(UPLOAD_FOLDER)]
        if image_id not in images:
            abort(404)
        path = f'{image_id}.{ACCEPTED_FILE_TYPE}'
        return send_from_directory(UPLOAD_FOLDER, path, as_attachment=True)

    def post(self, image_id):
        data = parser.parse_args()
        if data['file'] is None:
            abort(500)
        img = data['file']

        if img:
            filename = f'{image_id}.{ACCEPTED_FILE_TYPE}'
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            img.save(filepath)
            return {
                    'data':'',
                    'message':'Image uploaded',
                    'status':'success'
                    }
        abort(500)

class ImageList(Resource):
    def get(self):
        return list([os.path.basename(f) for f in os.listdir(UPLOAD_FOLDER)])

api.add_resource(ImageList, '/')
api.add_resource(Image, '/<string:image_id>')

if __name__ == '__main__':
    app.run()