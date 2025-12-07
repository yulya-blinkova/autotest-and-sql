Финальный проект 
Часть 2 
Задание 1. Список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true). https://github.com/yulya-blinkova/autotest-and-sql/blob/main/1.1.png

Задание 2. Трекеры заказов и их статусы - https://github.com/yulya-blinkova/autotest-and-sql/blob/main/1.2.png

Автоматизация теста к API 
Для запуска теста должны быть установлены пакеты pytest и requests Запуск всех тестов выполняется командой pytest. 
В файле "configuration.py" указаны url сервера и endpoint API. 
В файле "data.py" указаны данные для запросов: order_body, headers 
В файле "sender_stand_request.py" описаны функции создания нового заказа и получения заказа по номеру. 
В файле "create_order_test.py" прописан сам тест. 
Перед запуском тестов необходимо актуализировать переменную URL_SERVICE в "configuration.py". 
Скриншот с результатами теста https://github.com/yulya-blinkova/autotest-and-sql/blob/main/test.png.
