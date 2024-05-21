import sys
import yaml

# Функція для перевірки синтаксису YAML
def check_yaml_syntax(yaml_str):
    try:
        yaml.safe_load(yaml_str)
        return True
    except yaml.YAMLError:
        print("Niepoprawna składnia pliku YAML.")
        return False

# Функція для зчитування YAML файлу
def read_from_yaml_file(file_path):
    try:
        with open(file_path, "r") as file:
            yaml_content = file.read()
            if check_yaml_syntax(yaml_content):
                data = yaml.safe_load(yaml_content)
                return data
            else:
                return None
    except FileNotFoundError:
        print("Podany plik nie istnieje")
    except yaml.YAMLError:
        print("Błąd wczytywania danych YAML:", file_path)
    except Exception as e:
        print("Wystąpił nieoczekiwany błąd:", str(e))
    return None

# Функція для запису YAML файлу
def write_to_yaml_file(data, file_path):
    try:
        with open(file_path, "w") as file:
            yaml.dump(data, file)
        print(f"Pomyślnie zapisano dane YAML do pliku: {file_path}")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisu danych YAML: {str(e)}")

def main():
    if len(sys.argv) < 3:
        print("Podaj nazwy plików wejściowego i wyjściowego jako argumenty.")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = read_from_yaml_file(input_file)

    if data:
        print("Wczytano dane z pliku YAML:")
        print(data)
        write_to_yaml_file(data, output_file)

if __name__ == "__main__":
    main()
