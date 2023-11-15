# This is a Python script.
# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
import random

# Setzen Sie die maximale Anzahl der Dateien, die pro Tag kopiert werden sollen
max_files = 50

# Pfad zum Quellverzeichnis
source_dir = os.path.expanduser("~/Bilder/background/")

# Pfad zum Zielverzeichnis
dest_dir = os.path.expanduser("~/Bilder/tag/")

# Leeren Sie das Zielverzeichnis
for filename in os.listdir(dest_dir):
    file_path = os.path.join(dest_dir, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
    except Exception as e:
        print(f'Fehler beim Löschen von {file_path}. Grund: {e}')

# Liste der Dateien im Quellverzeichnis
files = os.listdir(source_dir)

# Mischen Sie die Dateiliste
random.shuffle(files)

# Zählen Sie, wie viele Dateien bereits kopiert wurden
count = 0

# Kopieren Sie maximal 'max_files' Dateien
for file in files:
    # Brechen Sie die Schleife ab, wenn die maximale Anzahl erreicht ist
    if count >= max_files:
        break

    # Pfad zur Quelldatei
    source_file = os.path.join(source_dir, file)
    # Pfad zum Zielverzeichnis
    dest_file = os.path.join(dest_dir, file)

    # Erstellen Sie einen symbolischen Link zur Quelldatei
    os.symlink(source_file, dest_file)

    # Erhöhen Sie den Zähler
    count += 1
