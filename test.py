import kle_render
import json
import codecs


data = kle_render.deserialise(json.loads(codecs.open('test.json', 'r', 'utf-8').read()))
img = kle_render.render_keyboard(data)

img.save("render_output.png", 'PNG')
