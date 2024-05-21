import sys
import json

def check_json_syntax(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError:
        return False

def read_from_json_file(file_path):
    with open(file_path, "r") as file:
        json_content = file.read()
        if not check_json_syntax(json_content):
            print("Niepoprawna składnia pliku JSON:", file_path)
            return None
        try:
            data = json.loads(json_content)
            return data
        except FileNotFoundError:
            print("Podany plik nie istnieje")
        except json.JSONDecodeError:
            print("Błąd wczytywania danych JSON:", file_path)
        except Exception as e:
            print("Wystąpił nieoczekiwany błąd:", str(e))
        return None

def write_to_json_file(data, file_path):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def main():
    if len(sys.argv) < 3:
        print("Podaj nazwy plików wejściowego i wyjściowego jako argumenty.")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = read_from_json_file(input_file)

    if data:
        print("Wczytano dane z pliku JSON:")
        print(data)
        write_to_json_file(data, output_file)
        print(f"Pomyślnie zapisano dane JSON do pliku {output_file}")

if __name__ == "__main__":
    main()
