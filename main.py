def get_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def find_100_words(text):   
    LETTER_MAP = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

    list_words = text.lower().replace("'","").split()
    all_100_words = []

    for word in list_words:
        sum = 0
        for i in range(0,len(word)):
            sum += LETTER_MAP[word[i]]
        if sum == 100:
            all_100_words.append(word)
    
    return "\n".join(all_100_words)

def main():
    raw_text = get_text("englishWords.txt")

    output = find_100_words(raw_text)

    print(output)

main()