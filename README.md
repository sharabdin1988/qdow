# qdow - Quran Downloader

Скрипт для скачивания аятов для заучивания с quran.com.
Script for downloading ayahs for memorization from quran.com.

## Languages / Языки

- [Russian (Русский)](#russian)
- [English](#english)
- [Arabic (العربية)](#arabic)
- [Chinese (中文)](#chinese)
- [Hindi (हिन्दी)](#hindi)
- [Surah List / Список сур](#surah-list)

---

<a name="russian"></a>
### Русский
Утилита для скачивания отдельных аятов или диапазонов аятов Корана в высоком качестве (128kbps) с автоматической установкой метаданных (имя чтеца).

**Требования:**
- **Python 3**: Обычно предустановлен.
- **ffmpeg**: Необходим для склеивания аятов.
  - *macOS*: `brew install ffmpeg`
  - *Ubuntu/Debian*: `sudo apt install ffmpeg`

**Примеры команд:**
```bash
qdow 2:255          # Скачать Аят Аль-Курси
qdow 2:285-286      # Склеить несколько аятов
qdow --reciter      # Выбрать чтеца
```

---

<a name="english"></a>
### English
A utility for downloading individual ayahs or ranges of ayahs from the Quran in high quality (128kbps) with automatic metadata (reciter name).

**Requirements:**
- **Python 3**: Usually pre-installed.
- **ffmpeg**: Required for merging ayahs.
  - *macOS*: `brew install ffmpeg`
  - *Ubuntu/Debian*: `sudo apt install ffmpeg`

**Usage Examples:**
```bash
qdow 2:255          # Download Ayatul Kursi
qdow 2:285-286      # Merge multiple ayahs
qdow --reciter      # Select reciter
```

---

<a name="arabic"></a>
### العربية
أداة لتحميل آيات محددة أو مجموعة من الآيات من القرآن الكريم بجودة عالية (١٢٨ كيلوبت في الثانية) مع إضافة بيانات القارئ تلقائياً.

**المتطلبات:**
- **Python 3**: مثبت عادةً بشكل مسبق.
- **ffmpeg**: مطلوب لدمج الآيات.
  - *macOS*: `brew install ffmpeg`
  - *Ubuntu/Debian*: `sudo apt install ffmpeg`

**أمثلة:**
```bash
qdow 2:255          # تحميل آية الكرسي
qdow --reciter      # تغيير القارئ
```

---

<a name="chinese"></a>
### 中文
用于从 quran.com 下载高音质（128kbps）古兰经经文的工具。

**系统要求:**
- **Python 3**
- **ffmpeg**: 用于合并音频。
  - *macOS*: `brew install ffmpeg`
  - *Ubuntu/Debian*: `sudo apt install ffmpeg`

**命令示例:**
```bash
qdow 2:255          # 下载特定的经文
qdow --reciter      # 选择诵读家
```

---

<a name="hindi"></a>
### हिन्दी
कुरान की आयतों को डाउनलोड करने के लिए एक उपकरण।

**आवश्यकताएँ:**
- **Python 3**
- **ffmpeg**: आयतों को जोड़ने के लिए आवश्यक है।
  - *macOS*: `brew install ffmpeg`
  - *Ubuntu/Debian*: `sudo apt install ffmpeg`

**उदाहरण:**
```bash
qdow 2:255          # आयत डाउनलोड करें
qdow --reciter      # पाठक चुनें
```

---

## Installation / Установка

```bash
curl -sSL https://raw.githubusercontent.com/sharabdin1988/qdow/main/install.sh | bash
```

---

<a name="surah-list"></a>
## Surah List / Список сур (Numbers)

| # | Name | # | Name | # | Name |
|---|---|---|---|---|---|
| 1 | Al-Fatihah | 2 | Al-Baqarah | 3 | Ali-Imran |
| 4 | An-Nisa | 5 | Al-Maidah | 6 | Al-Anam |
| 7 | Al-Araf | 8 | Al-Anfal | 9 | At-Tawbah |
| 10 | Yunus | 18 | Al-Kahf | 19 | Maryam |
| 36 | Ya-Sin | 55 | Ar-Rahman | 56 | Al-Waqiah |
| 67 | Al-Mulk | 112 | Al-Ikhlas | 113 | Al-Falaq |
| 114 | An-Nas | ... | ... | ... | ... |

*(Full list is available inside the script or on Quran.com)*
