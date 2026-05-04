#!/usr/bin/env python3
import urllib.request
import os
import sys
import subprocess
import tempfile
import json

CONFIG_FILE = os.path.expanduser("~/.qdow_config")

RECITERS = [
    {"name": "Mahmoud Khalil Al-Husary (Muallim)", "path": "Husary_Muallim_128kbps"},
    {"name": "Mahmoud Khalil Al-Husary (Standard)", "path": "Husary_64kbps"},
    {"name": "Mishari Rashid al-`Afasy", "path": "Mishari_Rashid_Alafasy_128kbps"},
    {"name": "AbdulBaset AbdulSamad (Murattal)", "path": "Abdul_Basit_Murattal_128kbps"},
    {"name": "AbdulBaset AbdulSamad (Mujawwad)", "path": "Abdul_Basit_Mujawwad_128kbps"},
    {"name": "Mohamed Siddiq al-Minshawi (Murattal)", "path": "Minshawi_Murattal_128kbps"},
    {"name": "Mohamed Siddiq al-Minshawi (Mujawwad)", "path": "Minshawi_Mujawwad_128kbps"},
    {"name": "Abdur-Rahman as-Sudais", "path": "Sudais_128kbps"},
]

SURAH_DATA = [
    (1, "Al-Fatihah", "Аль-Фатиха"), (2, "Al-Baqarah", "Аль-Бакара"), (3, "Ali-Imran", "Али Имран"),
    (4, "An-Nisa", "Ан-Ниса"), (5, "Al-Maidah", "Аль-Маида"), (6, "Al-Anam", "Аль-Анам"),
    (7, "Al-Araf", "Аль-Араф"), (8, "Al-Anfal", "Аль-Анфаль"), (9, "At-Tawbah", "Ат-Тауба"),
    (10, "Yunus", "Юнус"), (11, "Hud", "Худ"), (12, "Yusuf", "Юсуф"),
    (13, "Ar-Rad", "Ар-Раад"), (14, "Ibrahim", "Ибрахим"), (15, "Al-Hijr", "Аль-Хиджр"),
    (16, "An-Nahl", "Ан-Нахль"), (17, "Al-Isra", "Аль-Исра"), (18, "Al-Kahf", "Аль-Кахф"),
    (19, "Maryam", "Марьям"), (20, "Ta-Ha", "Та Ха"), (21, "Al-Anbiya", "Аль-Анбия"),
    (22, "Al-Hajj", "Аль-Хадж"), (23, "Al-Mu-minun", "Аль-Муминун"), (24, "An-Nur", "Ан-Нур"),
    (25, "Al-Furqan", "Аль-Фуркан"), (26, "Ash-Shuara", "Аш-Шуара"), (27, "An-Naml", "Ан-Намль"),
    (28, "Al-Qasas", "Аль-Касас"), (29, "Al-Ankabut", "Аль-Анкабут"), (30, "Ar-Rum", "Ар-Рум"),
    (31, "Luqman", "Лукман"), (32, "As-Sajdah", "Ас-Саджда"), (33, "Al-Ahzab", "Аль-Ахзаб"),
    (34, "Saba", "Саба"), (35, "Fatir", "Фатыр"), (36, "Ya-Sin", "Йа Син"),
    (37, "As-Saffat", "Ас-Саффат"), (38, "Sad", "Сад"), (39, "Az-Zumar", "Аз-Зумар"),
    (40, "Ghafir", "Гафир"), (41, "Fussilat", "Фуссилат"), (42, "Ash-Shura", "Аш-Шура"),
    (43, "Az-Zukhruf", "Аз-Зухруф"), (44, "Ad-Dukhan", "Ад-Духан"), (45, "Al-Jathiyah", "Аль-Джасия"),
    (46, "Al-Ahqaf", "Аль-Ахкаф"), (47, "Muhammad", "Мухаммад"), (48, "Al-Fath", "Аль-Фатх"),
    (49, "Al-Hujurat", "Аль-Худжурат"), (50, "Qaf", "Каф"), (51, "Adh-Dhariyat", "Аз-Зарият"),
    (52, "At-Tur", "Ат-Тур"), (53, "An-Najm", "Ан-Наджм"), (54, "Al-Qamar", "Аль-Камар"),
    (55, "Ar-Rahman", "Ар-Рахман"), (56, "Al-Waqiah", "Аль-Вакыа"), (57, "Al-Hadid", "Аль-Хадид"),
    (58, "Al-Mujadilah", "Аль-Муджадиля"), (59, "Al-Hashr", "Аль-Хашр"), (60, "Al-Mumtahanah", "Аль-Мумтахана"),
    (61, "As-Saff", "Ас-Сафф"), (62, "Al-Jumuah", "Аль-Джумуа"), (63, "Al-Munafiqun", "Аль-Мунафикун"),
    (64, "At-Taghabun", "Ат-Тагабун"), (65, "At-Talaq", "Ат-Таляк"), (66, "At-Tahrim", "Ат-Тахрим"),
    (67, "Al-Mulk", "Аль-Мульк"), (68, "Al-Qalam", "Аль-Калям"), (69, "Al-Haqqah", "Аль-Хакка"),
    (70, "Al-Maarij", "Аль-Мааридж"), (71, "Nuh", "Нух"), (72, "Al-Jinn", "Аль-Джинн"),
    (73, "Al-Muzzammil", "Аль-Муззаммиль"), (74, "Al-Muddaththir", "Аль-Муддассир"), (75, "Al-Qiyamah", "Аль-Кыяма"),
    (76, "Al-Insan", "Аль-Инсан"), (77, "Al-Mursalat", "Аль-Мурсалят"), (78, "An-Naba", "Ан-Наба"),
    (79, "An-Nazi-at", "Ан-Назиат"), (80, "Abasa", "Абаса"), (81, "At-Takwir", "Ат-Таквир"),
    (82, "Al-Infitar", "Аль-Инфитар"), (83, "Al-Mutaffifin", "Аль-Мутаффифин"), (84, "Al-Inshiqaq", "Аль-Иншикак"),
    (85, "Al-Buruj", "Аль-Бурудж"), (86, "At-Tariq", "Ат-Тарик"), (87, "Al-A-la", "Аль-Аля"),
    (88, "Al-Ghashiyah", "Аль-Гашия"), (89, "Al-Fajr", "Аль-Фаджр"), (90, "Al-Balad", "Аль-Баляд"),
    (91, "Ash-Shams", "Аш-Шамс"), (92, "Al-Layl", "Аль-Ляйль"), (93, "Ad-Duha", "Ад-Духа"),
    (94, "Ash-Sharh", "Аш-Шарх"), (95, "At-Tin", "Ат-Тин"), (96, "Al-Alaq", "Аль-Аляк"),
    (97, "Al-Qadr", "Аль-Кадр"), (98, "Al-Bayyinah", "Аль-Баййина"), (99, "Az-Zalzalah", "Аз-Зальзаля"),
    (100, "Al-Adiyat", "Аль-Адият"), (101, "Al-Qari-ah", "Аль-Кариа"), (102, "At-Takathur", "Ат-Такасур"),
    (103, "Al-Asr", "Аль-Аср"), (104, "Al-Humazah", "Аль-Хумаза"), (105, "Al-Fil", "Аль-Филь"),
    (106, "Quraysh", "Курайш"), (107, "Al-Ma-un", "Аль-Маун"), (108, "Al-Kawthar", "Аль-Каусар"),
    (109, "Al-Kafirun", "Аль-Кяфирун"), (110, "An-Nasr", "Ан-Наср"), (111, "Al-Masad", "Аль-Масад"),
    (112, "Al-Ikhlas", "Аль-Ихлас"), (113, "Al-Falaq", "Аль-Фаляк"), (114, "An-Nas", "Ан-Нас")
]

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {"reciter_idx": 0}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def print_surah_list():
    print("\n--- Список Сур ---")
    for i in range(0, len(SURAH_DATA), 3):
        line = ""
        for j in range(3):
            if i + j < len(SURAH_DATA):
                idx, eng, rus = SURAH_DATA[i+j]
                line += f"{str(idx).ljust(3)} {rus.ljust(15)} | "
        print(line)

def select_reciter():
    print("\n--- Выбор чтеца ---")
    for i, r in enumerate(RECITERS):
        print(f"{i}: {r['name']}")
    try:
        choice = int(input("\nВыберите номер чтеца: "))
        if 0 <= choice < len(RECITERS):
            save_config({"reciter_idx": choice})
            print(f"✅ Выбран чтец: {RECITERS[choice]['name']}")
        else: print("❌ Неверный номер.")
    except ValueError: print("❌ Введите число.")

def download_file(url, path):
    try:
        urllib.request.urlretrieve(url, path)
        return True
    except: return False

def merge_and_tag(files, output_path, reciter_name, album_name):
    print(f"🔄 Склеиваю и добавляю теги...")
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        for file in files: f.write(f"file '{os.path.abspath(file)}'\n")
        list_path = f.name
    try:
        subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', list_path, '-metadata', f'artist={reciter_name}', '-metadata', f'album={album_name}', '-c', 'copy', output_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Сохранено: {os.path.abspath(output_path)}")
    finally: os.unlink(list_path)

def tag_single_file(input_path, output_path, reciter_name, album_name):
    try:
        subprocess.run(['ffmpeg', '-y', '-i', input_path, '-metadata', f'artist={reciter_name}', '-metadata', f'album={album_name}', '-c', 'copy', output_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Сохранено: {os.path.abspath(output_path)}")
    except: pass

def process_request(request, reciter):
    try:
        if ":" not in request: return
        surah_part, ayah_part = request.split(":")
        s_idx = int(surah_part)
        if not (1 <= s_idx <= 114): return
        
        _, eng_name, rus_name = SURAH_DATA[s_idx - 1]
        s_num = surah_part.zfill(3)

        if "-" in ayah_part:
            start_a, end_a = map(int, ayah_part.split("-"))
            ayahs = range(start_a, end_a + 1)
            output_name = f"{eng_name}_{start_a}-{end_a}.mp3"
        else:
            ayahs = [int(ayah_part)]
            output_name = f"{eng_name}_{ayah_part}.mp3"

        temp_files = []
        with tempfile.TemporaryDirectory() as tmpdir:
            for a in ayahs:
                a_str = str(a).zfill(3)
                url = f"https://mirrors.quranicaudio.com/everyayah/{reciter['path']}/{s_num}{a_str}.mp3"
                tmp_path = os.path.join(tmpdir, f"{a_str}.mp3")
                print(f"⬇️  Загрузка: {rus_name} ({surah_part}:{a})...")
                if download_file(url, tmp_path): temp_files.append(tmp_path)
                else: print(f"⚠️ Аят {a} не найден")

            if len(temp_files) > 1: merge_and_tag(temp_files, output_name, reciter['name'], f"Сура {rus_name}")
            elif len(temp_files) == 1: tag_single_file(temp_files[0], output_name, reciter['name'], f"Сура {rus_name}")
    except Exception as e: print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    config = load_config()
    reciter = RECITERS[config['reciter_idx']]

    if len(sys.argv) > 1:
        if sys.argv[1] == "--reciter": select_reciter()
        elif sys.argv[1] == "list": print_surah_list()
        else:
            for arg in sys.argv[1:]: process_request(arg, reciter)
    else:
        print(f"🎙 Чтец: {reciter['name']}")
        print("Команды: 2:255, 2:285-286, list (список сур), --reciter, exit")
        while True:
            val = input("\nqdow > ").strip()
            if val.lower() == 'exit': break
            if val == '--reciter': select_reciter(); config = load_config(); reciter = RECITERS[config['reciter_idx']]
            elif val == 'list': print_surah_list()
            else: process_request(val, reciter)
