## Веб-тестирование
### Требования к ПО
+ Python 3.10 и выше
### Копирование репозитория и установка зависимостей
```
git clone https://github.com/ecoreee/test_web.git
cd test_web
python3 -m venv venv
pip install -r requirements.txt
```
### Запуск тестов
+ Перед запуском тестов необходимо перейти в каталог test_web
#### Аргументы запуска:
+ pytest -v - запуск тестового фреймворка Pytest
+ -v - verbose, режим, чтобы видеть, какие тесты были запущены
#### Запуск API-тестов: 
```
pytest -v
```
