import random

def load_words(file_path):
    words = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            word, meaning = line.strip().split(':')
            words[word] = meaning
    return words

def quiz(words):
    word, meaning = random.choice(list(words.items()))
    print(f"단어: {word}")
    answer = input("뜻을 입력하세요: ")
    if answer == meaning:
        print("정답입니다!")
    else:
        print(f"틀렸습니다. 정답은 {meaning}입니다.")

def main():
    words = load_words('words.txt')
    while True:
        quiz(words)
        cont = input("계속하시겠습니까? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
