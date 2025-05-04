from flask import Flask, render_template_string, request
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def coin_flip():
    result = None
    if request.method == 'POST':
        result = random.choice(['орёл', 'решка'])
    return render_template_string('''
        <h1>Орёл или решка?</h1>
        {% if result %}
            <p>Выпало: <b>{{ result }}</b></p>
        {% endif %}
        <form method="POST">
            <button type="submit">Подбросить монетку</button>
        </form>
    ''', result=result)

if __name__ == '__main__':
    app.run()