import os
import enchant
import re
import sys

# Укажите папку с файлами для проверки
FILES_DIR = "./"

# Файлы конфигурации
EXCEPTIONS_FILE = "scripts/exceptions.txt"  # Список слов-исключений
EXCLUDE_PATHS_FILE = "scripts/exclude_paths.txt"  # Список файлов/папок для исключения

# Регулярное выражение для извлечения слов из текста
WORD_REGEX = re.compile(r'\b\w+\b', re.UNICODE)

# Инициализация словарей для английского и русского языков
en_dict = enchant.Dict("en_US")
ru_dict = enchant.Dict("ru_RU")

def load_exceptions(file_path):
    """
    Загружает список слов-исключений из указанного файла.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return set(word.strip() for word in f if word.strip())
    except FileNotFoundError:
        print(f"Exceptions file not found: {file_path}")
        return set()

def load_exclude_paths(file_path):
    """
    Загружает список исключённых файлов и папок.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return set(path.strip() for path in f if path.strip())
    except FileNotFoundError:
        print(f"Exclude paths file not found: {file_path}")
        return set()

def is_excluded(file_path, exclude_paths):
    """
    Проверяет, исключён ли файл или папка из проверки.
    """
    for exclude_path in exclude_paths:
        # Проверяем совпадение с файлом или вложенность папки
        if file_path.startswith(exclude_path):
            return True
    return False

def check_spelling(file_path, exceptions):
    """
    Проверяет орфографию в указанном файле, пропуская слова-исключения.
    """
    errors = []
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line_number, line in enumerate(lines, start=1):
            words = WORD_REGEX.findall(line)
            for word in words:
                if word in exceptions:
                    continue
                if not (en_dict.check(word) or ru_dict.check(word)):
                    errors.append((line_number, word))
    return errors

def main():
    """
    Основная функция для проверки всех файлов.
    """
    # Загрузка исключений и путей
    exceptions = load_exceptions(EXCEPTIONS_FILE)
    exclude_paths = load_exclude_paths(EXCLUDE_PATHS_FILE)

    print(f"Loaded {len(exceptions)} word exceptions.")
    print(f"Loaded {len(exclude_paths)} excluded paths.")

    # Флаг для отслеживания наличия ошибок
    error_found = False

    # Проверка файлов
    for root, _, files in os.walk(FILES_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=".")
            if is_excluded(relative_path, exclude_paths):
                print(f"Skipping excluded file: {relative_path}")
                continue

            print(f"Checking file: {relative_path}")
            errors = check_spelling(file_path, exceptions)
            if errors:
                print(f"Found errors in {relative_path}:")
                for line, word in errors:
                    print(f"  Line {line}: {word}")
                error_found = True
                print()

    # Если найдены ошибки, завершить с кодом 1
    if error_found:
        print("Spell check found errors. Exiting with failure.")
        sys.exit(1)
    else:
        print("No spelling errors found.")
        sys.exit(0)

if __name__ == "__main__":
    main()