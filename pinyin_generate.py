from flask import Flask, request, render_template_string
from pypinyin import pinyin, Style

from word_mapping import phonetic_dict


# Initialize Flask application
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    pinyin_result = ""
    if request.method == 'POST':
        # Get the Chinese text from the form
        chinese_text = request.form["text"]

        # Convert the Chinese text to Pinyin with tone markings (Style.TONE)
        pinyin_result = " ".join([item[0] for item in pinyin(chinese_text, style=Style.TONE, strict= False)])

    # Render the HTML template with the result
    return render_template_string('''
        <h1>Chinese to Pinyin Converter</h1>
        <form action="/" method="post">
            <textarea name="text" rows="4" cols="50" placeholder="Enter Chinese text here...">{{ request.form['text'] if request.form['text'] else '' }}</textarea><br><br>
            <button type="submit">Convert to Pinyin</button>
        </form>
        <br>
        <h2>Pinyin Result:</h2>
        <p>{{ pinyin_result }}</p>
    ''', pinyin_result=pinyin_result)


if __name__ == "__main__":
    # Run the app on the default Flask port (5000)
    app.run(debug=True)
