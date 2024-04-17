m = int(input())

def reflection(value):
    words = []
    word = ''
    for char in value:
        if char != ',':
            word += char
        else:
            words.append(word)
            word = ''
    words.append(word)
    for i in range(len(words)-1, -1, -1):
        print(words[i])

input_str = input()
reflection(input_str)