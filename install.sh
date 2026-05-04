#!/bin/bash

# Цвета для вывода
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}==> Начинаю установку qdow...${NC}"

# Создаем директорию для бинарников
mkdir -p "$HOME/.local/bin"

# Определяем, откуда брать файл (если запуск локальный или через curl)
if [ -f "quran.py" ]; then
    cp quran.py "$HOME/.local/bin/qdow"
else
    echo "Загружаю скрипт из GitHub..."
    curl -sSL https://raw.githubusercontent.com/sharabdin1988/qdow/main/quran.py -o "$HOME/.local/bin/qdow"
fi

chmod +x "$HOME/.local/bin/qdow"

# Проверка ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo -e "${BLUE}Внимание: ffmpeg не найден. Он нужен для склеивания аятов.${NC}"
    if [[ "$OSTYPE" == "darwin"* ]]; then
        echo "На macOS установите его через: brew install ffmpeg"
    else
        echo "На Linux установите его через ваш менеджер пакетов (например: sudo apt install ffmpeg)"
    fi
fi

# Настройка путей в зависимости от оболочки (bash или zsh)
SHELL_CONFIG=""
if [[ "$SHELL" == *"zsh"* ]]; then
    SHELL_CONFIG="$HOME/.zshrc"
elif [[ "$SHELL" == *"bash"* ]]; then
    SHELL_CONFIG="$HOME/.bashrc"
fi

if [ -n "$SHELL_CONFIG" ]; then
    if ! grep -q ".local/bin" "$SHELL_CONFIG"; then
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_CONFIG"
        echo -e "${GREEN}==> Путь добавлен в $SHELL_CONFIG${NC}"
    fi
fi

echo -e "${GREEN}==> Установка завершена!${NC}"
echo -e "${GREEN}==> Перезапустите терминал или введите: source $SHELL_CONFIG${NC}"
echo -e "${GREEN}==> Теперь вы можете использовать команду: qdow 2:255${NC}"
