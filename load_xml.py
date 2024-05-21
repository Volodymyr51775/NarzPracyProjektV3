import sys
import xml.etree.ElementTree as ET

def validate_xml_syntax(file_path):
    try:
        with open(file_path, "r") as file:
            ET.fromstring(file.read())
        return True
    except ET.ParseError:
        print("Niepoprawna składnia pliku XML.")
        return False

def read_from_xml_file(file_path):
    if not validate_xml_syntax(file_path):
        return None
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        print("Podany plik nie istnieje")
    except ET.ParseError:
        print("Błąd wczytywania pliku XML:", file_path)
    except Exception as e:
        print("Wystąpił nieoczekiwany błąd:", str(e))
    return None

def main():
    if len(sys.argv) < 2:
        print("Podaj nazwę pliku wejściowego jako argument.")
        sys.exit(1)

    input_file = sys.argv[1]
    data = read_from_xml_file(input_file)

    if data:
        print("Wczytano dane z pliku XML:")
        print(data)

if __name__ == "__main__":
    main()
