from flask import Flask, render_template,request,Response
from PIL import Image
import io

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/jpgtopng', methods=['GET'])
def jpgtopng():
    return render_template('jpgtopng.html')


@app.route('/pngtojpg', methods=['GET'])
def pngtojpg():
    return render_template('pngtojpg.html')

@app.route('/webtopng', methods=['GET'])
def webtopng():
    return render_template('webtopng.html')

@app.route('/bmptopng', methods=['GET'])
def bmptopng():
    return render_template('bmptopng.html')

@app.route('/pngtopdf', methods=['GET'])
def pngtopdf():
    return render_template('pngtopdf.html')




@app.route('/api/jpgtopng', methods=['POST'])
def jpg_to_png():
    image = request.files['image']
    image = Image.open(image)
    image = image.convert("RGB")
    png_image = image.save("converted.png")
    with open("converted.png", "rb") as f:
        response = Response(f.read(), content_type="image/png")
        response.headers["Content-Disposition"] = "attachment; filename=converted.png"
        return response

if __name__ == '__main__':
    app.run(debug=True)
