import argparse
from pathlib import Path

def get_arguments():
    parser = argparse.ArgumentParser(description="Program do konwersji danych")
    parser.add_argument("input_file", type=argparse.FileType('r'), help="nazwa pliku wejściowego")
    parser.add_argument("output_file", type=str, help="nazwa pliku wyjściowego")
    return parser.parse_args()

def validate_file(file_path):
    if not file_path.is_file():
        raise ValueError("Podana ścieżka nie wskazuje na plik.")
    file_extension = file_path.suffix.lower()
    valid_extensions = [".xml", ".json", ".yml", ".yaml"]
    if file_extension not in valid_extensions:
        raise ValueError("Nieprawidłowe rozszerzenie pliku. Oczekiwano .xml, .json, .yml lub .yaml")

def process_files(input_file, output_file):
    print("Przetwarzanie plików...")
    print("Plik wejściowy: ", input_file)
    print("Plik wyjściowy: ", output_file)
    file_path = Path(input_file)
    validate_file(file_path)

if __name__ == "__main__":
    try:
        args = get_arguments()
        process_files(args.input_file.name, args.output_file)
    except FileNotFoundError as e:
        print("Podany plik nie istnieje. ", str(e))
    except ValueError as e:
        print("Nieprawidłowy format danych.", str(e))
    except Exception as e:
        print("Wystąpił nieoczekiwany błąd:", str(e))
    else:
        print("Plik został przetworzony pomyślnie.")
