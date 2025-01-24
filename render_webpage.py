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
        
        <!-- Hidden input to track Halal preset -->
        <form action="/" method="post">
            <div class="form-group">
                <label for="text">Enter Chinese text here:</label>
                <textarea id="text" name="text" rows="4" class="form-control" placeholder="Enter Chinese text here...">{{ request.form['text'] if request.form['text'] else '' }}</textarea>
            </div>
            <!-- Preset Buttons -->
                <label for="text">Presets: </label>
                <button type="button" class="btn btn-secondary" onclick="setPreset('你好')">Hello</button>
                <button type="button" class="btn btn-secondary" onclick="setPreset('再见')">Goodbye</button>
                <button type="button" class="btn btn-secondary" onclick="setPreset('谢谢')">Thank you</button>
                <button type="button" class="btn btn-secondary" onclick="setPreset('清真')">Halal ¹</button>
                <button type="button" class="btn btn-secondary" onclick="setPreset('《天方性理》题记言心性，无异于儒家。言四元及天有九重，合于欧罗巴之法。盖精研于程朱之理，又纬以泰西之学，遂能卓然成一家之言，为天方教中巨作。明未文体多诡，言理者尤多支碎。此书文笔昌明博大。盖康熙间，景运方隆，文明焕发，而载笔之士，皆知圣道所归，想见一时儒学之盛焉。时同治丙寅岁仲春月。兵部侍郎兼都察院右副都御史、安徽巡抚部院兼提督军门乔松年阅毕题记。 ')">Liu Zhi's Tianfang xingli ²</button>

            <button type="submit" class="btn btn-primary btn-block" id="submitButton" style="margin-top: 10px;">Convert</button>
        </form>
        
        <!-- JavaScript to Set Preset Text -->
        <script>
            function setPreset(text) {
                document.getElementById('text').value = text;
                document.getElementById('submitButton').click();
            }
        </script>

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
    
    <div class= "container">
    
    <h2>Footnotes:</h2>
    <p class="footnote-content">¹ The Chinese word for halal 清真 translates literally to pure and true. Originally used by Daoists, this word was adopted by Chinese Islamic scholars to describe Islamic doctrine.</p>
    <p class="footnote2">² Liu Zhi is a Chinese Islamic Scholar and Tianfang Xingli was his magnum opus. The book's title translates to "Nature and Principle in Islam". The book is heavily influenced by Sufi texts, but is presented using Neo-Confucian terminology and ideas. 
    The paragraph that is preset into this tool is <a href="https://zh.wikisource.org/wiki/%E5%A4%A9%E6%96%B9%E6%80%A7%E7%90%86#%E3%80%8A%E5%A4%A9%E6%96%B9%E6%80%A7%E7%90%86%E3%80%8B%E9%A2%98%E8%AE%B0" target="_blank"> here</a>.</p>
    
    </div>
    
    </body>
    </html>
    '''