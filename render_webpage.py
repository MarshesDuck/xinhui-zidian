content = '''
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
    '''