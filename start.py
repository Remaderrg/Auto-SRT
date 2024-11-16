name = str(input('Enter File Name: '))
srtstr = str(input('Enter SRT Text: '))
srtstr = srtstr.split()
speechspeed = float(input("Enter Speech Speed (default = 0.05): "))  # 0.05 = 50мс

# Новая переменная для количества слов в строке
words_per_line = int(input("Words in line: ")) 

count = 1
firsttime = 0
secondtime = 0
strfirsttime = "00:00:00,000"
strsecondtime = ""

def timecalculation(total_seconds):
    # Преобразование секунд в миллисекунды
    total_milliseconds = int(total_seconds * 1000)

    # Вычисление часов, минут и секунд
    hours, remainder = divmod(total_milliseconds, 3600000)
    minutes, seconds = divmod(remainder, 60000)
    seconds, milliseconds = divmod(seconds, 1000)

    # Форматирование результата
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

completesrt = ""
current_words = 0
line_words = ""

for words in srtstr:
    wordslen = len(words)
    secondtime += wordslen * speechspeed
    strsecondtime = timecalculation(secondtime)

    line_words += f"{words} "
    current_words += 1

    # Проверяем, достигли ли мы лимита слов в строке или если слово заканчивается на точку
    if current_words >= words_per_line or words.endswith('.'):
        completesrt += f"{count}\n{strfirsttime} --> {strsecondtime}\n{line_words.strip()}\n\n"
        count += 1
        strfirsttime = strsecondtime
        current_words = 0
        line_words = ""

# Добавляем последнюю строку, если остались слова
if current_words > 0:
    completesrt += f"{count}\n{strfirsttime} --> {strsecondtime}\n{line_words.strip()}\n\n"

# Записываем результат в файл
with open(f"{name}.srt", "w", encoding="utf-8") as file:
    file.write(completesrt)

print(f"Subtitles saved to {name}.srt")
