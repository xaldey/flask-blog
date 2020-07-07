# flask-blog
### Блог на flask


1. Стянуть проект git clone 
2. Установить виртуальное окружение. Активировать окружение.
3. Установить необходимые модули pip install -r requirements.txt
4. Создать экземпляр БД. Запустить командную строку. Перейти в папку с проектом.
 
' $ sqlite3 blog.db

' sqlite> .tables

' sqlite> .exit

5. Создаем набор необходимых таблиц в соответствии с моделями.

Запустить python.

$ python

' >>> from app import db

' >>> db.create_all() 

' >>> exit()

6. Запуск путем старта файла app.py

' python app.py

7. Запуск более правильным путем

' export FLASK_APP=app.py

' export FLASK_DEBUG=1

' flask run

 
