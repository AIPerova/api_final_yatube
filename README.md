# Проект «API для Yatube»
### Описание
API для Yatub представляет проект социальной сети в которой можно публиковать записи на любые темы и делиться впечатлениями, комментировать свои и чужие записи, подписываться на интересных авторов и следить за их обновлениями.
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/yandex-praktikum/kittygram.git
```

```
cd kittygram
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

