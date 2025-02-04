name = str(input('Enter File Name: ').strip() or 'subtitles')
srtstr = str(input('Enter SRT Text: ').strip() or 'Sample text for subtitles!!!! This is the test string.... The second part of the example”?” ')
speechspeed = float(input("Enter Speech Speed (default = 0.065): ").strip() or "0.065") # 0.065 = 65мс
words_per_line = int(input("Words in line (default = 5): ").strip() or "5") 
line_break_on_dot = (input_line == 'true') if (input_line := input('Use line break on dot? (True/False, default=True): ').strip().lower()) else True

count = 1
firsttime = 0
secondtime = 0
strfirsttime = "00:00:00,000"
strsecondtime = ""
srtstr = srtstr.split()

def timecalculation(total_seconds):
    total_milliseconds = int(total_seconds * 1000)
    hours, remainder = divmod(total_milliseconds, 3600000)
    minutes, seconds = divmod(remainder, 60000)
    seconds, milliseconds = divmod(seconds, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"

completesrt = ""
current_words = 0
line_words = ""

for words in srtstr:
    wordslen = len(words)
    secondtime += wordslen * speechspeed

    if (secondtime - firsttime) * 1000 < 150:
        secondtime = firsttime + 0.15

    strsecondtime = timecalculation(secondtime)

    line_words += f"{words} "
    current_words += 1

    # Проверка условий для переноса строки
    if current_words >= words_per_line or (line_break_on_dot and words.endswith('.')):
        completesrt += f"{count}\n{strfirsttime} --> {strsecondtime}\n{line_words.strip()}\n\n"
        count += 1
        strfirsttime = strsecondtime
        firsttime = secondtime
        current_words = 0
        line_words = ""

if current_words > 0:
    completesrt += f"{count}\n{strfirsttime} --> {strsecondtime}\n{line_words.strip()}\n\n"

with open(f"{name}.srt", "w", encoding="utf-8") as file:
    file.write(completesrt)

print(f"Subtitles saved to {name}.srt")