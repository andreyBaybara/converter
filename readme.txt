Для разверкти  проекта локально  на linux необходимо  иметь установленный git и python.
Инструкция по разворачивании проекта
1  sudo apt install python3-venv установить пакет для создания виртуального окружения
2 python3 -m venv myvenv - создать виртуальное окружение
3 source myenv/bin/activate - активировать виртуальное окружение 
4 pip install django - установить фреймворк django
5 git clone https://gitlab.com/Yushin35/lightit.git  - склонировать из репозитория проект
6 python manage.py runserver 
7 зайти на главную по адресу http://127.0.0.1:8000/