Репозиторий является частью проекта [Tarder](https://tarder.ru)

Инструкцию по работе с программой вы сможете найти в [справочной системе](https://tarder.ru/info/business/avtomaticheskoe-obnovlenie-dannyh):

Используя систему Tarder вы соглашаетесь с [условиями использования](https://tarder.ru/info/general/terms-of-use):


**Быстрый запуск из исходников**:

 - Установить зависимости:
 
 `pip install -r requirements.txt`

 - Скомпилировать exe файл:
 
 `pyinstaller -y -F -n TarderSync --windowed --icon="assets\logo.ico" --hidden-import="PySide2.QtXml"  main.py`


**Для разработчиков**:

- Сгенерировать зависимости для установки:

`pip freeze > requirements.txt`

- Изменять qt файлы можно в QtDesigner

- Сгенерировать '_ui.py' файл из '.ui':

`pyside2-uic --generator python $FileName$ -o $FileNameWithoutAllExtensions$_ui.py`

pyside2-uic из пакета pyside2-tools (может лежать в папке venv\Scripts)
 
- Сгенерировать '_rc.py' файл из '.qrc':

`rcc.exe --generator python $FileName$ -o $FileNameWithoutAllExtensions$_rc.py`

и затем заменить в нем символы '= "' на '= b"'

 rcc.exe (pyside2-rcc) расположен в папке "site-packages\PySide2"
 
- Решение ошибки "Не удалось инициализировать TLS" https://ru.stackoverflow.com/questions/952577/qt-network-ssl-qsslsocketconnecttohostencrypted-tls-initialization-failed
 
 