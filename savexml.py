import sys
import xml.etree.ElementTree as ET

def check_xml_syntax(file_path):
    try:
        with open(file_path, "r") as file:
            ET.fromstring(file.read())
        return True
    except ET.ParseError:
        print("Niepoprawna składnia pliku XML.")
        return False

def read_from_xml_file(file_path):
    if not check_xml_syntax(file_path):
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

def write_to_xml_file(data, file_path):
    try:
        tree = ET.ElementTree(data)
        tree.write(file_path, encoding="utf-8", xml_declaration=True)
        print(f"Pomyślnie zapisano dane XML do pliku: {file_path}")
    except Exception as e:
        print(f"Wystąpił błąd podczas zapisu danych do pliku: {str(e)}")

def main():
    if len(sys.argv) < 3:
        print("Podaj nazwę pliku wejściowego i wyjściowego jako argumenty.")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    data = read_from_xml_file(input_file)

    if data:
        print("Wczytano dane z pliku XML:")
        print(ET.tostring(data, encoding='utf8').decode('utf8'))
        write_to_xml_file(data, output_file)

if __name__ == "__main__":
    main()
