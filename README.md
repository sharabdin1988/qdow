# qdow - Quran Downloader

Скрипт для скачивания аятов для заучивания с quran.com.
Script for downloading ayahs for memorization from quran.com.

## Languages / Языки

- [Russian (Русский)](#russian)
- [English](#english)
- [Arabic (العربية)](#arabic)
- [Chinese (中文)](#chinese)
- [Hindi (हिन्दी)](#hindi)

---

<a name="russian"></a>
### Русский
Утилита для скачивания отдельных аятов или диапазонов аятов Корана в высоком качестве (128kbps) с возможностью выбора чтеца. Идеально подходит для заучивания (хифза).

**Примеры команд:**
```bash
qdow 2:255          # Скачать Аят Аль-Курси
qdow 2:285-286      # Скачать последние два аята Бакары (склеенные в один файл)
qdow 114:1-6        # Скачать всю суру Ан-Нас целиком
qdow --reciter      # Выбрать чтеца (Шейх Аль-Хусари, Мишари Рашид и др.)
```

---

<a name="english"></a>
### English
A utility for downloading individual ayahs or ranges of ayahs from the Quran in high quality (128kbps) with reciter selection. Perfect for memorization (Hifz).

**Usage Examples:**
```bash
qdow 2:255          # Download Ayatul Kursi
qdow 2:285-286      # Download the last two ayahs of Baqarah (merged into one file)
qdow 114:1-6        # Download the entire Surah An-Nas
qdow --reciter      # Select reciter (Husary, Mishary Rashid, etc.)
```

---

<a name="arabic"></a>
### العربية
أداة لتحميل آيات محددة أو مجموعة من الآيات من القرآن الكريم بجودة عالية (١٢٨ كيلوبت في الثانية) مع إمكانية اختيار القارئ. مثالي للحفظ.

**أمثلة على الاستخدام:**
```bash
qdow 2:255          # تحميل آية الكرسي
qdow 2:285-286      # تحميل آخر آيتين من سورة البقرة (دمج في ملف واحد)
qdow 114:1-6        # تحميل سورة الناس كاملة
qdow --reciter      # اختيار القارئ (الحصري، مشاري راشد، إلخ)
```

---

<a name="chinese"></a>
### 中文
用于从 quran.com 下载高音质（128kbps）古兰经经文（Ayah）的工具，支持选择诵读家。非常适合背诵。

**使用示例：**
```bash
qdow 2:255          # 下载阿亚特·库尔西 (Ayatul Kursi)
qdow 2:285-286      # 下载巴卡拉苏拉的最后两节经文（合并为一个文件）
qdow 114:1-6        # 下载整个安纳斯苏拉 (Surah An-Nas)
qdow --reciter      # 选择诵读家（Husary, Mishary Rashid 等）
```

---

<a name="hindi"></a>
### हिन्दी
quran.com से कुरान की आयतों को उच्च गुणवत्ता (128kbps) में डाउनलोड करने के लिए एक उपकरण। यह हिफ्ज़ (याद करने) के लिए बेहतरीन है।

**उपयोग के उदाहरण:**
```bash
qdow 2:255          # आयतुल कुर्सी डाउनलोड करें
qdow 2:285-286      # बक़राह की आखिरी दो आयतें डाउनलोड करें (एक फ़ाइल में मर्ज की गई)
qdow 114:1-6        # पूरी सूरह अन-नास डाउनलोड करें
qdow --reciter      # पाठक (कारी) चुनें (हुसारी, मिशारी राशिद, आदि)
```

---

## Installation / Установка

### macOS & Linux
```bash
curl -sSL https://raw.githubusercontent.com/sharabdin1988/qdow/main/install.sh | bash
```

## Requirements / Требования
- Python 3
- ffmpeg (for merging ayahs / для склеивания аятов)
