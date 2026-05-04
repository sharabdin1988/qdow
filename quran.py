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

SURAH_NAMES = [
    "Al-Fatihah", "Al-Baqarah", "Ali-Imran", "An-Nisa", "Al-Maidah",
    "Al-Anam", "Al-Araf", "Al-Anfal", "At-Tawbah", "Yunus",
    "Hud", "Yusuf", "Ar-Rad", "Ibrahim", "Al-Hijr",
    "An-Nahl", "Al-Isra", "Al-Kahf", "Maryam", "Ta-Ha",
    "Al-Anbiya", "Al-Hajj", "Al-Mu-minun", "An-Nur", "Al-Furqan",
    "Ash-Shuara", "An-Naml", "Al-Qasas", "Al-Ankabut", "Ar-Rum",
    "Luqman", "As-Sajdah", "Al-Ahzab", "Saba", "Fatir",
    "Ya-Sin", "As-Saffat", "Sad", "Az-Zumar", "Ghafir",
    "Fussilat", "Ash-Shura", "Az-Zukhruf", "Ad-Dukhan", "Al-Jathiyah",
    "Al-Ahqaf", "Muhammad", "Al-Fath", "Al-Hujurat", "Qaf",
    "Adh-Dhariyat", "At-Tur", "An-Najm", "Al-Qamar", "Ar-Rahman",
    "Al-Waqiah", "Al-Hadid", "Al-Mujadilah", "Al-Hashr", "Al-Mumtahanah",
    "As-Saff", "Al-Jumuah", "Al-Munafiqun", "At-Taghabun", "At-Talaq",
    "At-Tahrim", "Al-Mulk", "Al-Qalam", "Al-Haqqah", "Al-Maarij",
    "Nuh", "Al-Jinn", "Al-Muzzammil", "Al-Muddaththir", "Al-Qiyamah",
    "Al-Insan", "Al-Mursalat", "An-Naba", "An-Nazi-at", "Abasa",
    "At-Takwir", "Al-Infitar", "Al-Mutaffifin", "Al-Inshiqaq", "Al-Buruj",
    "At-Tariq", "Al-A-la", "Al-Ghashiyah", "Al-Fajr", "Al-Balad",
    "Ash-Shams", "Al-Layl", "Ad-Duha", "Ash-Sharh", "At-Tin",
    "Al-Alaq", "Al-Qadr", "Al-Bayyinah", "Az-Zalzalah", "Al-Adiyat",
    "Al-Qari-ah", "At-Takathur", "Al-Asr", "Al-Humazah", "Al-Fil",
    "Quraysh", "Al-Ma-un", "Al-Kawthar", "Al-Kafirun", "An-Nasr",
    "Al-Masad", "Al-Ikhlas", "Al-Falaq", "An-Nas"
]

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {"reciter_idx": 0}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def select_reciter():
    print("\n--- Выбор чтеца ---")
    for i, r in enumerate(RECITERS):
        print(f"{i}: {r['name']}")
    
    try:
        choice = int(input("\nВыберите номер чтеца: "))
        if 0 <= choice < len(RECITERS):
            save_config({"reciter_idx": choice})
            print(f"✅ Выбран чтец: {RECITERS[choice]['name']}")
        else:
            print("❌ Неверный номер.")
    except ValueError:
        print("❌ Введите число.")

def download_file(url, path):
    try:
        urllib.request.urlretrieve(url, path)
        return True
    except Exception as e:
        print(f"❌ Ошибка при загрузке {url}: {e}")
        return False

def merge_files(files, output_path):
    if not files:
        return
    print(f"🔄 Склеиваю {len(files)} аятов...")
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        for file in files:
            f.write(f"file '{os.path.abspath(file)}'\n")
        list_path = f.name
    try:
        subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', list_path, '-c', 'copy', output_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Сохранено: {os.path.abspath(output_path)}")
    finally:
        os.unlink(list_path)

def process_request(request, reciter_path):
    try:
        if ":" not in request: return
        surah_part, ayah_part = request.split(":")
        s_idx = int(surah_part)
        s_num = surah_part.zfill(3)
        surah_name = SURAH_NAMES[s_idx - 1] if 1 <= s_idx <= 114 else "Unknown"

        if "-" in ayah_part:
            start_a, end_a = map(int, ayah_part.split("-"))
            ayahs = range(start_a, end_a + 1)
            output_name = f"{surah_name}_{start_a}-{end_a}.mp3"
        else:
            ayahs = [int(ayah_part)]
            output_name = f"{surah_name}_{ayah_part}.mp3"

        temp_files = []
        with tempfile.TemporaryDirectory() as tmpdir:
            for a in ayahs:
                a_str = str(a).zfill(3)
                url = f"https://mirrors.quranicaudio.com/everyayah/{reciter_path}/{s_num}{a_str}.mp3"
                tmp_path = os.path.join(tmpdir, f"{a_str}.mp3")
                print(f"⬇️  Загрузка {surah_name} {surah_part}:{a}...")
                if download_file(url, tmp_path): temp_files.append(tmp_path)

            if len(temp_files) > 1: merge_files(temp_files, output_name)
            elif len(temp_files) == 1:
                import shutil
                shutil.copy(temp_files[0], output_name)
                print(f"✅ Сохранено: {os.path.abspath(output_name)}")
    except Exception as e: print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    config = load_config()
    reciter = RECITERS[config['reciter_idx']]

    if len(sys.argv) > 1:
        if sys.argv[1] == "--reciter":
            select_reciter()
        else:
            print(f"🎙 Чтец: {reciter['name']}")
            for arg in sys.argv[1:]:
                process_request(arg, reciter['path'])
    else:
        print(f"--- Загрузчик Quran (Текущий чтец: {reciter['name']}) ---")
        print("Команды: 2:255, 2:285-286, --reciter (сменить чтеца), exit")
        while True:
            val = input("\nВведите запрос: ").strip()
            if val.lower() == 'exit': break
            if val == '--reciter': select_reciter(); config = load_config(); reciter = RECITERS[config['reciter_idx']]
            else: process_request(val, reciter['path'])
