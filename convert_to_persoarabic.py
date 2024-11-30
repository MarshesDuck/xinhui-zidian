from flask import Flask, request, render_template_string
from pypinyin import pinyin, lazy_pinyin, Style
from word_mapping import phonetic_dict
from punctuation_mapping import punctuation_mapping
from eastern_arabic_numbers import western_to_eastern_numerals

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
        pinyin_result = " ".join([item[0] for item in pinyin(chinese_text, style=Style.TONE)])

        # Convert the Chinese text to lazy Pinyin (without tone markings)
        lazy_pinyin_result = lazy_pinyin(chinese_text)

        # Map the lazy Pinyin result to the phonetic dictionary
        phonetic_result = map_lazy_pinyin_to_phonetic(lazy_pinyin_result)

    # Render the HTML template with the results
    return render_template_string('''
        <h1>Write Chinese in Perso-Arabic (Xiaoerjing) script</h1>
        <form action="/" method="post">
            <textarea name="text" rows="4" cols="50" placeholder="Enter Chinese text here...">{{ request.form['text'] if request.form['text'] else '' }}</textarea><br><br>
            <button type="submit">Convert to Pinyin</button>
        </form>
        <br>
        <h2>Pinyin Result:</h2>
        <p>{{ pinyin_result }}</p>
        <br>
        <h2>Xiaoerjing Result:</h2>
        <p style="direction: rtl; text-align: left;">{{ phonetic_result }}</p>
    ''', pinyin_result=pinyin_result, phonetic_result=phonetic_result)


if __name__ == "__main__":
    # Run the app on the default Flask port (5000)
    app.run(debug=True)
