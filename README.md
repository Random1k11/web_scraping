Web scraper 

Создайте виртуальное окружение командой

virtualenv venv

source venv/bin/activate

pip install -r requirements.txt

В файле config.py укажите настройки для парсера и базы данных.

Запустите парсер командой

python run_dental.py


Либо запустите в Docker

docker build -t dental .

docker run -it --entrypoint=/bin/sh dental
