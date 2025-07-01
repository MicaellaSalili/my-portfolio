from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/uppercase_convert', methods=['GET', 'POST'])
def convert():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/areaOfcircle', methods=['GET', 'POST'])
def area_of_circle():
    area_circle = None
    radius = None
    if request.method == 'POST':
        radius = (request.form.get('radius', 0))
        area_circle = 3.14159 * float(radius) ** 2
        area_circle = round(area_circle, 2)
    return render_template('circle_area.html', area_circle=area_circle , radius=radius)

@app.route('/areaOftriangle', methods=['GET', 'POST'])
def area_of_triangle():
    area_triangle = None
    base = None
    height = None
    if request.method == 'POST':
        base = float(request.form.get('base', 0))
        height = float(request.form.get('height', 0))
        area_triangle = 0.5 * base * height
        area_triangle = round(area_triangle, 2)
    return render_template('triangle_area.html', area_triangle=area_triangle, base=base, height = height)

if __name__ == "__main__":
    app.run(debug=True)
