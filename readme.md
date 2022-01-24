# Python Pip Template
Шаблон проекта пакета для pypi.

## Разработка
### Тестирование пакета
Для тестирования нужно установить локальную копию, доступную для интерпретатора. Причем, делать это нужно в virtualenv.
```
python setup.py develop
```

### Сборка и загрузка дистрибутивных файлов
Необходим пакет python-dotenv, перед началом работы его нужно установить. Сборка:
```
python3 setup.py sdist bdist_wheel
```

Загрузка дистрибутивных файлов на _testpypi_ и _pypi_
```
python3 -m twine upload --repository testpypi dist/*
python3 -m twine upload --repository pyp
```

### Проверка на ошибки
```
python3 -m twine check dist/*
```

## Использование
Информация о пакете, авторе и прочая информация указана в _setup.py_. Подробное описание указано в файле _readme.md_.
Версия пакета указана в файле __init__.py пакета _src_. 

Точка входа определена так же в файле _setup.py_:
```python
entry_points={                                         
    'console_scripts': [
        'python-pip-template = src.cmd:run',
    ],
},

# python-pip-template - команда выполнения скрипта;   
# src                 - пакет с исходными файлами;  
# cmd                 - модуль с точкой входа;  
# run                 - точка входа (отсюда начинается выполнения всего скрипта).
```
