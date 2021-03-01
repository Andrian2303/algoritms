def primary_hash(pattern_length, pattern, text, pattern_hash, text_hash_window, h, digits_amount, prime_number):
    for _ in range(pattern_length - 1):
        h = (h * digits_amount) % prime_number

    for window_index in range(pattern_length):
        text_hash_window = (digits_amount * text_hash_window + ord(text[window_index])) % prime_number
        pattern_hash = (digits_amount * pattern_hash + ord(pattern[window_index])) % prime_number

    return h, text_hash_window, pattern_hash


def next_characters_hash(window_index, text_length, pattern_length, digits_amount, text_hash_window,
                         text, h, prime_number):
    if window_index < text_length - pattern_length:
        text_hash_window = (digits_amount * (text_hash_window - ord(text[window_index]) * h) +
                            ord(text[window_index + pattern_length])) % prime_number

        if text_hash_window < 0:
            text_hash_window = text_hash_window + prime_number

    return text_hash_window


def search_pattern(pattern, text, prime_number, digits_amount):
    pattern_length = len(pattern)
    text_length = len(text)

    text_hash_window = 0
    pattern_hash = 0
    symbol_index = 0
    h = 1

    result = []

    # data validation
    if pattern == "" or text == "":
        return []

    h, text_hash_window, pattern_hash = primary_hash(pattern_length, pattern, text, pattern_hash, text_hash_window, h,
                                                     digits_amount, prime_number)

    for window_index in range(text_length - pattern_length + 1):

        if pattern_hash == text_hash_window:

            for symbol_index in range(pattern_length):
                if text[window_index + symbol_index] != pattern[symbol_index]:
                    break
                else:
                    symbol_index += 1

            if symbol_index == pattern_length:
                result.append((str(window_index), str(window_index + symbol_index - 1)))

        text_hash_window = next_characters_hash(window_index, text_length, pattern_length, digits_amount,
                                                text_hash_window, text, h, prime_number)
    print(result)
    return result
