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
    d = 256
    q = 101
    M = len(pattern)
    N = len(text)
    h = pow(d, M-1) % q
    p = 0
    t = 0
    occurrences = []
    for i in range(M):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(N-M + 1):
        if p == t:
            for j in range(M):
                if text[i + j] != pattern[j]:
                    break
            else:
                occurrences.append(i)
        if i < N-M:
            t = (d*(t-ord(text[i])*h) + ord(text[i + M])) % q
            if t < 0:
                t = t + q   
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
