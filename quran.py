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

# Surah data with English names and Ayah counts
SURAH_DATA = [
    (1, "Al-Fatihah", 7), (2, "Al-Baqarah", 286), (3, "Ali-Imran", 200),
    (4, "An-Nisa", 176), (5, "Al-Maidah", 120), (6, "Al-Anam", 165),
    (7, "Al-Araf", 206), (8, "Al-Anfal", 75), (9, "At-Tawbah", 129),
    (10, "Yunus", 109), (11, "Hud", 123), (12, "Yusuf", 111),
    (13, "Ar-Rad", 43), (14, "Ibrahim", 52), (15, "Al-Hijr", 99),
    (16, "An-Nahl", 128), (17, "Al-Isra", 111), (18, "Al-Kahf", 110),
    (19, "Maryam", 98), (20, "Ta-Ha", 135), (21, "Al-Anbiya", 112),
    (22, "Al-Hajj", 78), (23, "Al-Mu-minun", 118), (24, "An-Nur", 64),
    (25, "Al-Furqan", 77), (26, "Ash-Shuara", 227), (27, "An-Naml", 93),
    (28, "Al-Qasas", 88), (29, "Al-Ankabut", 69), (30, "Ar-Rum", 60),
    (31, "Luqman", 34), (32, "As-Sajdah", 30), (33, "Al-Ahzab", 73),
    (34, "Saba", 54), (35, "Fatir", 45), (36, "Ya-Sin", 83),
    (37, "As-Saffat", 182), (38, "Sad", 88), (39, "Az-Zumar", 75),
    (40, "Ghafir", 85), (41, "Fussilat", 54), (42, "Ash-Shura", 53),
    (43, "Az-Zukhruf", 89), (44, "Ad-Dukhan", 59), (45, "Al-Jathiyah", 37),
    (46, "Al-Ahqaf", 35), (47, "Muhammad", 38), (48, "Al-Fath", 29),
    (49, "Al-Hujurat", 18), (50, "Qaf", 45), (51, "Adh-Dhariyat", 60),
    (52, "At-Tur", 49), (53, "An-Najm", 62), (54, "Al-Qamar", 55),
    (55, "Ar-Rahman", 78), (56, "Al-Waqiah", 96), (57, "Al-Hadid", 29),
    (58, "Al-Mujadilah", 22), (59, "Al-Hashr", 24), (60, "Al-Mumtahanah", 13),
    (61, "As-Saff", 14), (62, "Al-Jumuah", 11), (63, "Al-Munafiqun", 11),
    (64, "At-Taghabun", 18), (65, "At-Talaq", 12), (66, "At-Tahrim", 12),
    (67, "Al-Mulk", 30), (68, "Al-Qalam", 52), (69, "Al-Haqqah", 52),
    (70, "Al-Maarij", 44), (71, "Nuh", 28), (72, "Al-Jinn", 28),
    (73, "Al-Muzzammil", 20), (74, "Al-Muddaththir", 56), (75, "Al-Qiyamah", 40),
    (76, "Al-Insan", 31), (77, "Al-Mursalat", 50), (78, "An-Naba", 40),
    (79, "An-Nazi-at", 46), (80, "Abasa", 42), (81, "At-Takwir", 29),
    (82, "Al-Infitar", 19), (83, "Al-Mutaffifin", 36), (84, "Al-Inshiqaq", 25),
    (85, "Al-Buruj", 22), (86, "At-Tariq", 17), (87, "Al-A-la", 19),
    (88, "Al-Ghashiyah", 26), (89, "Al-Fajr", 30), (90, "Al-Balad", 20),
    (91, "Ash-Shams", 15), (92, "Al-Layl", 21), (93, "Ad-Duha", 11),
    (94, "Ash-Sharh", 8), (95, "At-Tin", 8), (96, "Al-Alaq", 19),
    (97, "Al-Qadr", 5), (98, "Al-Bayyinah", 8), (99, "Az-Zalzalah", 8),
    (100, "Al-Adiyat", 11), (101, "Al-Qari-ah", 11), (102, "At-Takathur", 8),
    (103, "Al-Asr", 3), (104, "Al-Humazah", 9), (105, "Al-Fil", 5),
    (106, "Quraysh", 4), (107, "Al-Ma-un", 7), (108, "Al-Kawthar", 3),
    (109, "Al-Kafirun", 6), (110, "An-Nasr", 3), (111, "Al-Masad", 5),
    (112, "Al-Ikhlas", 4), (113, "Al-Falaq", 5), (114, "An-Nas", 6)
]

# Mapping of special ayah names
SPECIAL_NAMES = {
    "2:255": "Ayatul_Kursi",
    "2:285-286": "Amanar_Rasul",
    "24:35": "Ayatul_Nur",
    "1:1-7": "Al-Fatihah_Complete"
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except: pass
    return {"reciter_idx": 0}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def print_surah_list():
    print("\n" + "="*50)
    print("SURAH LIST (Number: Name [Ayahs])")
    print("="*50)
    for i in range(0, len(SURAH_DATA), 2):
        line = ""
        for j in range(2):
            if i + j < len(SURAH_DATA):
                idx, name, count = SURAH_DATA[i+j]
                line += f"{str(idx).rjust(3)}. {name.ljust(18)} ({count} ayahs)".ljust(35)
        print(line)
    print("\nSPECIAL VERSES:")
    for key, val in SPECIAL_NAMES.items():
        print(f"  {key.ljust(10)} -> {val}")
    print("="*50)

def select_reciter():
    print("\n--- SELECT RECITER ---")
    for i, r in enumerate(RECITERS):
        print(f"{i}: {r['name']}")
    try:
        choice = int(input("\nChoice: "))
        if 0 <= choice < len(RECITERS):
            save_config({"reciter_idx": choice})
            print(f"✅ Selected: {RECITERS[choice]['name']}")
        else: print("❌ Invalid number.")
    except ValueError: print("❌ Enter a number.")

def download_file(url, path):
    try:
        urllib.request.urlretrieve(url, path)
        return True
    except: return False

def merge_and_tag(files, output_path, reciter_name, album_name):
    print(f"🔄 Merging and adding tags...")
    with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False) as f:
        for file in files: f.write(f"file '{os.path.abspath(file)}'\n")
        list_path = f.name
    try:
        subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', list_path, '-metadata', f'artist={reciter_name}', '-metadata', f'album={album_name}', '-c', 'copy', output_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Success: {os.path.abspath(output_path)}")
    finally: os.unlink(list_path)

def tag_single_file(input_path, output_path, reciter_name, album_name):
    try:
        subprocess.run(['ffmpeg', '-y', '-i', input_path, '-metadata', f'artist={reciter_name}', '-metadata', f'album={album_name}', '-c', 'copy', output_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"✅ Success: {os.path.abspath(output_path)}")
    except: pass

def process_request(request, reciter):
    try:
        if ":" not in request: return
        surah_part, ayah_part = request.split(":")
        s_idx = int(surah_part)
        if not (1 <= s_idx <= 114): return
        
        idx, name, count = SURAH_DATA[s_idx - 1]
        s_num = surah_part.zfill(3)

        special_suffix = ""
        key = f"{s_idx}:{ayah_part}"
        if key in SPECIAL_NAMES:
            special_suffix = f"_{SPECIAL_NAMES[key]}"

        if "-" in ayah_part:
            start_a, end_a = map(int, ayah_part.split("-"))
            ayahs = range(start_a, end_a + 1)
            output_name = f"{name}_{ayah_part}{special_suffix}.mp3"
        else:
            ayah_at = int(ayah_part)
            ayahs = [ayah_at]
            output_name = f"{name}_{ayah_at}{special_suffix}.mp3"

        temp_files = []
        with tempfile.TemporaryDirectory() as tmpdir:
            for a in ayahs:
                a_str = str(a).zfill(3)
                url = f"https://mirrors.quranicaudio.com/everyayah/{reciter['path']}/{s_num}{a_str}.mp3"
                tmp_path = os.path.join(tmpdir, f"{a_str}.mp3")
                print(f"⬇️  Downloading: {name} ({surah_part}:{a})...")
                if download_file(url, tmp_path): temp_files.append(tmp_path)
                else: print(f"⚠️ Ayah {a} not found")

            if len(temp_files) > 1:
                merge_and_tag(temp_files, output_name, reciter['name'], f"Surah {name}")
            elif len(temp_files) == 1:
                tag_single_file(temp_files[0], output_name, reciter['name'], f"Surah {name}")
    except Exception as e: print(f"❌ Error: {e}")

if __name__ == "__main__":
    config = load_config()
    reciter = RECITERS[config['reciter_idx']]

    if len(sys.argv) > 1:
        if sys.argv[1] == "--reciter": select_reciter()
        elif sys.argv[1] == "list": print_surah_list()
        else:
            for arg in sys.argv[1:]: process_request(arg, reciter)
    else:
        print(f"🎙 Reciter: {reciter['name']}")
        print("Commands: 2:255, 2:285-286, list, --reciter, exit")
        while True:
            val = input("\nqdow > ").strip()
            if val.lower() == 'exit': break
            if val == '--reciter': select_reciter(); config = load_config(); reciter = RECITERS[config['reciter_idx']]
            elif val == 'list': print_surah_list()
            else: process_request(val, reciter)
