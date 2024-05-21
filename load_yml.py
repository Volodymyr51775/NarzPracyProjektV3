import sys
import yaml

def validate_yaml_syntax(yaml_str):
    try:
        yaml.safe_load(yaml_str)
        return True
    except yaml.YAMLError:
        print("Niepoprawna składnia pliku YAML.")
        return False

def read_from_yaml_file(file_path):
    try:
        with open(file_path, "r") as file:
            yaml_content = file.read()
            if validate_yaml_syntax(yaml_content):
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

def main():
    if len(sys.argv) < 2:
        print("Podaj nazwę pliku wejściowego jako argument.")
        sys.exit(1)

    input_file = sys.argv[1]
    data = read_from_yaml_file(input_file)

    if data:
        print("Wczytano dane z pliku YAML:")
        print(data)

if __name__ == "__main__":
    main()
