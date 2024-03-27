def get_key_by_value(dictionary, search_value):
    for key, value in dictionary.items():
        if value == search_value:
            return key
    return None


def encryption(path: str) -> None:
    key = {'а': 'r', 'б': 'k', 'в': 'v', 'г': 'y', 'д': 'w', 'е': 'p', 'ё': 's', 'ж': 'd', 'з': 'n', 'и': 'a', 'й': 'j', 'к': 't', 'л': 'i',
           'м': 'h', 'н': 'x', 'о': 'g', 'п': 'l', 'р': 'o', 'с': 'z', 'т': 'q', 'у': 'u', 'ф': 'f', 'х': 'm', 'ц': 'e', 'ч': 'b', 'ш': 'c',
           'щ': 'ф', 'ъ': 'ы', 'ы': 'в', 'ь': 'х', 'э': 'т', 'ю': 'ь', 'я': 'и', 'А': 'R', 'Б': 'K', 'В': 'V', 'Г': 'Y', 'Д': 'W', 'Е': 'P',
           'Ё': 'S', 'Ж': 'D', 'З': 'N', 'И': 'A', 'Й': 'J', 'К': 'T', 'Л': 'I', 'М': 'H', 'Н': 'X', 'О': 'G', 'П': 'L', 'Р': 'O', 'С': 'Z',
           'Т': 'Q', 'У': 'U', 'Ф': 'F', 'Х': 'M', 'Ц': 'E', 'Ч': 'B', 'Ш': 'C', 'Щ': 'р', 'Ъ': 'к', 'Ы': 'й', 'Ь': 'ш', 'Э': 'ж', 'Ю': 'я',
           'Я': 'с', '0': '9', '1': '7', '2': '8', '3': '0', '4': '2', '5': '6', '6': '4', '7': '1', '8': '3', '9': '5'}

    with open('wr.txt', 'w+', encoding='UTF-8') as write_f:
        with open(path, 'r', encoding='UTF-8') as file:
            for line in file:
                temp = ''
                line = line.strip()
                for i in line:
                    try:
                        temp += key[str(i)]
                    except:
                        temp += str(i)
                write_f.write(temp + '\n')


def decoding(path: str) -> None:
    key = {'а': 'r', 'б': 'k', 'в': 'v', 'г': 'y', 'д': 'w', 'е': 'p', 'ё': 's', 'ж': 'd', 'з': 'n', 'и': 'a', 'й': 'j', 'к': 't', 'л': 'i',
           'м': 'h', 'н': 'x', 'о': 'g', 'п': 'l', 'р': 'o', 'с': 'z', 'т': 'q', 'у': 'u', 'ф': 'f', 'х': 'm', 'ц': 'e', 'ч': 'b', 'ш': 'c',
           'щ': 'ф', 'ъ': 'ы', 'ы': 'в', 'ь': 'х', 'э': 'т', 'ю': 'ь', 'я': 'и', 'А': 'R', 'Б': 'K', 'В': 'V', 'Г': 'Y', 'Д': 'W', 'Е': 'P',
           'Ё': 'S', 'Ж': 'D', 'З': 'N', 'И': 'A', 'Й': 'J', 'К': 'T', 'Л': 'I', 'М': 'H', 'Н': 'X', 'О': 'G', 'П': 'L', 'Р': 'O', 'С': 'Z',
           'Т': 'Q', 'У': 'U', 'Ф': 'F', 'Х': 'M', 'Ц': 'E', 'Ч': 'B', 'Ш': 'C', 'Щ': 'р', 'Ъ': 'к', 'Ы': 'й', 'Ь': 'ш', 'Э': 'ж', 'Ю': 'я',
           'Я': 'с', '0': '9', '1': '7', '2': '8', '3': '0', '4': '2', '5': '6', '6': '4', '7': '1', '8': '3', '9': '5'}

    with open('wr.txt', 'r', encoding='UTF-8') as write_f:
        with open(path, 'w+', encoding='UTF-8') as file:
            for line in write_f:
                temp = ''
                line = line.strip()
                for i in line:
                    if get_key_by_value(key, i):
                        temp += get_key_by_value(key, i)
                    else:
                        temp += str(i)
                file.write(temp + '\n')


def main():

    encryption('text.txt')
    decoding('dec.txt')


if __name__ == "__main__":
    main()
