words_content = """apple:사과
banana:바나나
cat:고양이
dog:개
"""

with open('words.txt', 'w', encoding='utf-8') as file:
    file.write(words_content)

print("words.txt 파일이 생성되었습니다.")
