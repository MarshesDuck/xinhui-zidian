punctuation_mapping = {
    # English punctuation
    ',': '،',  # Arabic comma
    '.': '.',  # Arabic full stop
    '!': '!',  # Exclamation mark remains the same (if needed to be modified, map it here)
    '"': '«',  # Arabic quotation mark (left)
    "'": '’',  # Arabic apostrophe (for single quotes)
    '(': '(',  # Parentheses remain the same
    ')': ')',  # Parentheses remain the same
    '?': '؟',  # Arabic question mark

    # Chinese punctuation
    '、': '،',  # Chinese comma to Arabic comma
    '，': '،',
    '。': '.',  # Chinese period to Arabic period
    '！': '!',  # Chinese exclamation mark remains the same
    '“': '«',  # Chinese left quotation mark to Arabic left quote
    '”': '»',  # Chinese right quotation mark to Arabic right quote
    '‘': '‘',  # Chinese single quotation mark remains the same
    '’': '’',  # Chinese single quotation mark remains the same
    '（': '(',  # Chinese left parenthesis to Arabic left parenthesis
    '）': ')',  # Chinese right parenthesis to Arabic right parenthesis
    '？': '؟',  # Chinese question mark to Arabic question mark
    '【': '【',  # Chinese left square bracket remains the same
    '】': '】',  # Chinese right square bracket remains the same
    '《': '«',  # Chinese left angle bracket to Arabic left quote
    '》': '»',  # Chinese right angle bracket to Arabic right quote
}