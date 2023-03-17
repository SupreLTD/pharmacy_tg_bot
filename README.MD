В ветке sbercloud сервис разбит на 3 микросервиса с использованием [Docker](https://www.docker.com/) и технологий [SberCloud.Advanced](https://sbercloud.ru/ru/advanced).

Сервис поиска и заказа лекарств оналйн. Реализован в виде телеграм-бота и веб-сервиса. Реализован нечёткий поиск с опечатками с помощью движка [Elasticsearch](https://www.elastic.co/elasticsearch/) (используется сервис [Elastic Cloud](https://www.elastic.co/cloud/)). Для поиска ближайших аптек и отображения цен на карте используются [HERE Technologies](https://www.here.com/)

Телеграм-бот [@digital_druggist_bot](https://t.me/digital_druggist_bot) умеет искать лекарства как по текстовому запросу, так и по фото. Для распознования лекарств с изображения, оно предварительно обрабатывается с помощью библиотеки [OpenCV](https://opencv.org/), извлекается текст с помощью [Tesseract OCR](https://github.com/tesseract-ocr/tesseract). Из полученного текста удаляется весь мусор и лишние слова, не относящиеся к названию лекарства. Так же бот может находить ближайшие аптеки.

Веб-сервис http://mburavczov.beget.tech/ умеет так же находить лекарства и отображать цены по ним на карте