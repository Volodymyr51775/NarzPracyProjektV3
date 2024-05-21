import sys
import myjson

def validate_json_syntax(json_str):
    try:
        json.loads(json_str)
        return True
    except ValueError:
        print("Niepoprawna składnia pliku JSON.")
        return False

def read_from_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            json_content = file.read()
            if validate_json_syntax(json_content):
                data = json.loads(json_content)
                return data
            else:
                return None
    except FileNotFoundError:
        print("Podany plik nie istnieje")
    except json.JSONDecodeError:
        print("Błąd wczytywania danych JSON:", file_path)
    except Exception as e:
        print("Wystąpił nieoczekiwany błąd:", str(e))
    return None

# Головна функція
def main():
    if len(sys.argv) < 3:
        print("Podaj nazwę pliku wejściowego i wyjściowego jako argumenty.")
        sys.exit(1)

    input_file = sys.argv[1]
    data = read_from_json_file(input_file)

    if data:
        print("Wczytano dane z pliku JSON:")
        print(data)

if __name__ == "__main__":
    main()
