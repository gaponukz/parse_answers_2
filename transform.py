import json
import xlsxwriter

from config import file_name

black_list = [6, 7, 8, 15, 16]

for i in range(1, 14):
    if not i in black_list:
        with open(f'{i}.json') as json_file:
            data = json.load(json_file)
            workbook = xlsxwriter.Workbook(f'{file_name[str(i)]}.xlsx') 
            worksheet = workbook.add_worksheet()
            
            row, column = 0, 0
            titles = ['Вопрос', 'Все ответи', 'Правильний ответ']
            for item in titles: 
                worksheet.write(row, column, item) 
                column += 1

            row = 1
            for item in data['data']:
                column = 0
                all_answers = ''
                true_answer = ''

                for answer in item['answers']:
                    all_answers += answer['title'] + '\n'
                    if answer['is_true_answer']:
                        true_answer = answer['title']

                worksheet.write(row, column, item['title'])
                worksheet.write(row, column + 1, all_answers)
                worksheet.write(row, column + 2, true_answer)

                row += 1

            workbook.close()