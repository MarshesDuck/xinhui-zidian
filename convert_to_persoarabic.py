from flask import Flask, request, render_template_string
from pypinyin import pinyin, lazy_pinyin, Style, load_single_dict
from word_mapping import phonetic_dict
from punctuation_mapping import punctuation_mapping
from eastern_arabic_numbers import western_to_eastern_numerals

# Custom dictionary because the pinyin library is inaccurate.
load_single_dict({ord('嗯'): 'èn'})

# Initialize Flask application
app = Flask(__name__)

# Function to convert Western Arabic numerals to Eastern Arabic numerals
def convert_number_to_eastern(number_str):
    return ''.join(western_to_eastern_numerals[digit] for digit in number_str if digit in western_to_eastern_numerals)

# Function to map Lazy Pinyin (without tone markings) to phonetic dictionary
def map_lazy_pinyin_to_phonetic(lazy_pinyin_result):
    phonetic_result = []

    # Iterate through the lazy Pinyin syllables and map them
    for syllable in lazy_pinyin_result:
        # Get the first letter (the initial part) and the full syllable
        letter = syllable[0].upper()

        # Try to find the phonetic result in the phonetic_dict first
        if letter in phonetic_dict:
            phonetic = phonetic_dict.get(letter, {}).get(syllable.lower())
            if phonetic:
                phonetic_result.append(phonetic)
            else:
                phonetic_result.append(syllable)
        # If not found in phonetic_dict, check punctuation mapping
        elif letter in punctuation_mapping:
            phonetic_result.append(punctuation_mapping[letter])
        else:
            phonetic_result.append(syllable)

        # Now replace any Western Arabic numerals in the phonetic_result with Eastern Arabic numerals
    phonetic_result = [convert_number_to_eastern(syllable) if any(
        digit in western_to_eastern_numerals for digit in syllable) else syllable for syllable in phonetic_result]

    # Return the mapped phonetic result as a string
    return " ".join(phonetic_result)

@app.route('/', methods=['GET', 'POST'])
def index():
    pinyin_result = ""
    phonetic_result = ""

    if request.method == 'POST':
        # Get the Chinese text from the form
        chinese_text = request.form["text"]

        # Convert the Chinese text to Pinyin with tone markings (Style.TONE)
        pinyin_result = " ".join([item[0] for item in pinyin(chinese_text, style=Style.TONE, strict=False)])

        # Convert the Chinese text to lazy Pinyin (without tone markings)
        lazy_pinyin_result = lazy_pinyin(chinese_text)

        # Map the lazy Pinyin result to the phonetic dictionary
        phonetic_result = map_lazy_pinyin_to_phonetic(lazy_pinyin_result)

    # Render the HTML template with the results
    # return render_template_string('''
    #     <h1>Write Chinese in Perso-Arabic (Xiaoerjing) script</h1>
    #     <form action="/" method="post">
    #         <textarea name="text" rows="4" cols="50" placeholder="Enter Chinese text here...">{{ request.form['text'] if request.form['text'] else '' }}</textarea><br><br>
    #         <button type="submit">Convert to Pinyin</button>
    #     </form>
    #     <br>
    #     <h2>Pinyin Result:</h2>
    #     <p>{{ pinyin_result }}</p>
    #     <br>
    #     <h2>Xiaoerjing Result:</h2>
    #     <p style="direction: rtl; text-align: left;">{{ phonetic_result }}</p>
    # ''', pinyin_result=pinyin_result, phonetic_result=phonetic_result)

    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Write Chinese in Perso-Arabic (Xiaoerjing) script</title>
        <!-- Link to Bootstrap for mobile-friendly design -->
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                font-family: 'Georgia', 'Times New Roman', serif;
                padding: 20px;
                background-color: #f4f4f4;  /* Light background for an old web look */
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
            }
            h1 {
                font-size: 2rem;  /* Smaller title size */
                text-align: center;
            }
            h2 {
                font-size: 1.5rem;  /* Smaller heading size */
                margin-top: 20px;
            }
            textarea {
                width: 100%;
                font-family: 'Georgia', 'Times New Roman', serif;
            }
            button {
                font-family: 'Georgia', 'Times New Roman', serif;
            }
            .result-section {
                margin-top: 20px;
            }
            .pinyin-result, .phonetic-result {
                word-wrap: break-word;
            }
            .phonetic-result {
                direction: rtl;
                text-align: left;
            }
        </style>
    </head>
    <body>

    <div class="container">
        <h1>Write Chinese in Perso-Arabic (Xiaoerjing) script</h1>

        <form action="/" method="post">
            <div class="form-group">
                <label for="text">Enter Chinese text here:</label>
                <textarea id="text" name="text" rows="4" class="form-control" placeholder="Enter Chinese text here...">{{ request.form['text'] if request.form['text'] else '' }}</textarea>
            </div>
            <button type="submit" class="btn btn-primary btn-block">Convert</button>
        </form>

        <div class="result-section">
            <h2>Pinyin Result:</h2>
            <p class="pinyin-result">{{ pinyin_result }}</p>

            <h2>Xiaoerjing Result:</h2>
            <p class="phonetic-result">{{ phonetic_result }}</p>
        </div>
    </div>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.2/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    
    <!-- Link to the website at the bottom -->
    <div class="text-center mt-4">
    <a href="https://github.com/MarshesDuck/xinhui-zidian" target="_blank">Learn more about this project</a>
    </div>
    
    </body>
    </html>
    ''', pinyin_result=pinyin_result, phonetic_result=phonetic_result)


if __name__ == "__main__":
    # Run the app on the default Flask port (5000)
    app.run(debug=True)
