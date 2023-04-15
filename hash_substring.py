def read_input():
    file_or_input = input().strip().lower()
    
    if file_or_input == "i":
        pattern = input().rstrip()
        text = input().rstrip()
    elif file_or_input == "f":
        file_path = ("tests/06")
        with open(file_path, encoding="utf8") as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    else:
        quit()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    base = 256
    prime = 101
    pattern_length = len(pattern)
    text_length = len(text)
    h = pow(base, pattern_length - 1) % prime
    pattern_hash = 0
    text_hash = 0
    occurrences = []
    for i in range(pattern_length):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime
    for i in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash:
            for j in range(pattern_length):
                if text[i + j] != pattern[j]:
                    break
            else:
                occurrences.append(i)
        if i < text_length - pattern_length:
            text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + pattern_length])) % prime
            if text_hash < 0:
                text_hash += prime   
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
