import xml.etree.ElementTree as ET
import json

# Читаем XML файл и парсим его
def read_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    data = []

    # Проходимся по каждому элементу person и сохраняем данные в виде словаря
    for person in root.findall('person'):
        person_data = {
            "name": person.find('name').text,
            "age": int(person.find('age').text),
            "profession": person.find('profession').text,
            "city": person.find('city').text
        }
        data.append(person_data)
    return data

# Конвертируем данные в JSON и сохраняем в файл
def write_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# Основная логика программы
def main():
    xml_file = 'data.xml'
    json_file = 'data.json'

    # Чтение XML файла и конвертация в JSON
    data = read_xml(xml_file)
    write_json(data, json_file)
    print(f"Файл успешно конвертирован в {json_file}")

if __name__ == '__main__':
    main()
