from io import BytesIO
import requests, json
import kle_render
from flask import Flask, send_file
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


def serve_pil_image(pil_img):
    img_io = BytesIO()
    pil_img.save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')


@app.route('/render', methods=['POST'])
@app.route('/render/<path:perm>', methods=['POST'])
def render(perm):
    content = request.get_json(silent=True)

    data = kle_render.deserialise(content)
    img = kle_render.render_keyboard(data)
    img.save("rendered/"+perm+".png", 'PNG')
    return serve_pil_image(img)

if __name__ == '__main__':
    app.run()