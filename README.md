# parse_answers_2

Сначала нужно установить все модули и библиотеки
```python
pip install -r requirements.txt
```
Для парсига всех тестов.
```python
python bot.py
```
Если какой-то из файлов json пустой нужно спарсить отдельно с
```python
python bot.py 2  (это спарсить все со второго теста)
python bot.py {номер_пустого_файла}
```
После того как все файлы json готовы запускаем transform.py для генерации excel
```python
python transform.py
```
