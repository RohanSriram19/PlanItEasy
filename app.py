from flask import Flask, render_template, request, redirect, url_for
import os
from PIL import Image

app = Flask(__name__)

# Initialize schedule as an empty list
schedule = []

# Ensure the static/images folder exists
if not os.path.exists('static/images'):
    os.makedirs('static/images')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        task = request.form['task']
        image = request.files['image']

        if image:
            # Save image to static/images folder
            image_path = os.path.join('static/images', image.filename)
            image.save(image_path)

            # Append the task and image path to the schedule
            schedule.append({'task': task, 'image_path': image_path})

            # Redirect back to the homepage to display updated schedule
            return redirect(url_for('home'))

    # Render the schedule on the homepage
    return render_template('index.html', schedule=schedule)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

