
# yaCut


### учебный проект яндекса по укорачиванию ссылок

Проект основан на базе Flask фреймворка. Позволяет пользователю укоротить ссылку, сделав ее красивой, обратившись за помощью к встроенному генератору, а если повезет, и кастомная ссылка не занята, то указать красивую ссылку (до 16 символов)

#### Как запустить проект

Клонируй проект к себе на локальную машину
`git clone https://github.com/authorIsRight/yacut.git`

Разверните, активируйте виртуальное окружение у установите зависимости
```
python -m venv venv
source venv/Scripts/activate 
pip install -r requirements.txt
```
Перейдите в папку yacut
`cd yacut`

Выполните команды последовательно в shell
```
flask shell
>>> from yacut import db
>>> from yacut.models import URLMap
>>>> db.create_all()
>>> exit()
```
Запустите проект 
`flask run`
##### Пользуйтесь на здоровье
![enter image description here](https://pictures.s3.yandex.net/resources/S01_130_1649172122.png)