# Python Pip Template
Шаблон проекта пакета для pypi.

## Разработка
### Тестирование пакета
Для тестирования нужно установить локальную копию, доступную для интерпретатора. Причем, лучше этого делать в virtualenv.
```
python setup.py develop
```

### Сборка и загрузка дистрибутивных файлов
Необходим пакет python-dotenv, перед началом работы его нужно установить. Сборка:
```
python setup.py sdist bdist_wheel
```

Загрузка дистрибутивных файлов на _testpypi_ и _pypi_
```
python -m twine upload --repository testpypi dist/*
python -m twine upload --repository pypi dist/*
```

## Использование
Информация о пакете, авторе и прочая информация указана в setup.py. Чтобы использовать свое имя пакета необходимо:  
1. Переименовать каталог _python_pip_template_;  
2. Изменить поля _name_, _packages_ и _entry_points_ в файле setup.py.