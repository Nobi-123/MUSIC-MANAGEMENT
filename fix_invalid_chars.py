import os

# Folder where your bot's source code is (change if needed)
BOT_FOLDER = "."

# Unicode characters that often cause SyntaxError in Python code
SUSPICIOUS_CHARS = [
    '\uFFFC',  # Object Replacement Character
    '\uFEFF',  # Zero Width No-Break Space (BOM)
    '\u200B',  # Zero Width Space
    '\u200C',  # Zero Width Non-Joiner
    '\u200D',  # Zero Width Joiner
    '\u25CC',  # Dotted Circle
]

def clean_file(file_path):
    changed = False
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        original_line = line
        for char in SUSPICIOUS_CHARS:
            if char in line:
                line = line.replace(char, "")
                changed = True
        new_lines.append(line)

    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"✅ Cleaned: {file_path}")

def clean_folder(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".py"):
                clean_file(os.path.join(root, file))

if __name__ == "__main__":
    print("🧹 Removing invalid/invisible characters from Python files...")
    clean_folder(BOT_FOLDER)
    print("✅ Cleaning complete.")
