#Задание 3
#Дан текстовый файл, в котором встечаются указания денежных сумм в долларах 
#('123.5$' или '123.5 USD') или евро ('123.5€' или '123.5 EUR'). 
#Напишите программу, которая будет переводить все встреченные суммы в тенге, 
#по текущему курсу, используя знак ₸ для обозначения валюты. 
#В качестве аргументов программа должна принимать имена входного и 
#выходного файлов:
#> python converter.py input.txt output.txt

import re

def convert_usd_to_tenge(amount_usd, exchange_rate):
    return f'{amount_usd * exchange_rate:.2f} ₸'

def main():
    input_file = 'sum.txt'
    output_file = 'result.txt'
    exchange_rate = 480

    try:
        with open('sum.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            pattern = r'\$([0-9]+)'
            matches = re.findall(pattern, content)
            for match in matches:
                amount_usd = float(match)
                converted_amount = convert_usd_to_tenge(amount_usd, exchange_rate)
                content = content.replace(f"${amount_usd}", converted_amount)
            with open('result.txt', 'w', encoding='utf-8') as output:
                output.write(content)
            print(f"Successful convertation from dollar to tenge and was saved in {output_file} file.")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()

#конвертация не получается