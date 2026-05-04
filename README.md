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

**Особенности:**
- Скачивание конкретных аятов (например, 2:255).
- Скачивание и автоматическая склейка диапазонов (например, 2:285-286).
- Выбор чтеца (Шейх Аль-Хусари, Мишари Рашид и др.).
- Названия файлов на английском (транслитерация названий сур).

**Требования:**
- Python 3
- ffmpeg (для склеивания аятов)

---

<a name="english"></a>
### English
A utility for downloading individual ayahs or ranges of ayahs from the Quran in high quality (128kbps) with reciter selection. Perfect for memorization (Hifz).

**Features:**
- Download specific ayahs (e.g., 2:255).
- Download and auto-merge ranges (e.g., 2:285-286).
- Reciter selection (Husary, Mishary Rashid, etc.).
- File names with Surah titles.

---

<a name="arabic"></a>
### العربية
أداة لتحميل آيات محددة أو مجموعة من الآيات من القرآن الكريم بجودة عالية (١٢٨ كيلوبت في الثانية) مع إمكانية اختيار القارئ. مثالي للحفظ.

**المميزات:**
- تحميل آيات معينة (مثلاً ٢:٢٥٥).
- تحميل ودمج تلقائي لمجموعة آيات (مثلاً ٢:٢٨٥-٢٨٦).
- اختيار القارئ (الحصري، مشاري راشد، إلخ).
- أسماء الملفات بأسماء السور.

---

<a name="chinese"></a>
### 中文
用于从 quran.com 下载高音质（128kbps）古兰经经文（Ayah）的工具，支持选择诵读家。非常适合背诵。

**功能：**
- 下载特定的经文（例如 2:255）。
- 下载并自动合并范围（例如 2:285-286）。
- 选择诵读家（Husary, Mishary Rashid 等）。
- 包含苏拉（Surah）名称的文件名。

---

<a name="hindi"></a>
### हिन्दी
quran.com से कुरान की आयतों को उच्च गुणवत्ता (128kbps) में डाउनलोड करने के लिए एक उपकरण। यह हिफ्ज़ (याद करने) के लिए बेहतरीन है।

**विशेषताएं:**
- विशिष्ट आयतें डाउनलोड करें (जैसे, 2:255)।
- आयतों की श्रेणियों को डाउनलोड और ऑटो-मर्ज करें (जैसे, 2:285-286)।
- पाठक (कारी) का चयन करें (हुसारी, मिशारी राशिद, आदि)।
- सूरह के नाम के साथ फ़ाइल नाम।

---

## Installation / Установка

### macOS & Linux
```bash
curl -sSL https://raw.githubusercontent.com/sharabdin1988/qdow/main/install.sh | bash
```

## Usage / Использование
```bash
qdow 2:255          # Single ayah
qdow 2:285-286      # Range (merged)
qdow --reciter      # Select reciter
```
