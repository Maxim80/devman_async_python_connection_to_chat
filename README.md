# Подключение к чату

Скрипт `reader.py` читает сообщения из чата.  
Аргументы:  
>`-H, --host` IP или URL адрес для подключения (Не обязательный аргумент, значение по умолчанию - minechat.dvmn.org).  
>`-p, --port` Порт для подключения (Не обязательный аргумент, значение по умолчанию - 5000).  
>`--history` Путь к файлу с историей переписки (Не обязательный аргумент, значение по умолчанию - ./minechat.history).  
>`-h, --help`Справочная информация (Не обязательный аргумент).  

Пример использования:  
```
python reader.py -H minechat.dvmn.org -p 5000 --history ./history
```

Скрипт `sender.py` публикует сообщения в чате.  
Аргументы:  
  > `-m, --message` Сообщение для публикации (Обязательный аргумент).  
  >`-H, --host` IP или URL адрес для подключения (Не обязательный аргумент, значение по умолчанию - minechat.dvmn.org).  
>`-p, --port` Порт для подключения (Не обязательный аргумент, значение по умолчанию - 5050).  
>`-r, --reg` Имя пользователя. Только при регистрации нового пользователя (Не обязательный аргумент).  
>`-l, --logger` Включить логирование (Не обязательный аргумент).  
>`-h, --help`Справочная информация (Не обязательный аргумент).  

Пример использования:  
 ```
python sender.py -m "Hello, chat" -r Alexx -l
 ```

### Установка:  
```
git clone https://github.com/Maxim80/devman_async_python_connection_to_chat.git
cd devman_async_python_connection_to_chat/
pip3 install -r requirements.txt
```

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).  

***
# Connect to chat  

The `reader.py` script reads messages from the chat.  
Arguments:  
>`-H, --host` IP or URL to connect to (Optional argument, default value - minechat.dvmn.org).  
>`-p, --port` Port for connection (Optional argument, default value - 5000).  
>`--history` Path to the file with the chat history (Optional argument, default value - ./minechat.history).  
>`-h, --help` Help information (Optional).  

Usage example:  
```
python reader.py -H minechat.dvmn.org -p 5000 --history ./history
```

The `sender.py` script publishes chat messages.  
Arguments:  
>`-m, --message` Message to publish (Required).  
>`-H, --host` IP or URL to connect to (Optional argument, default - minechat.dvmn.org).  
>`-p, --port` Port to connect to (Optional argument, default value - 5050).  
>`-r, --reg` Username. Only when registering a new user (Optional).  
>`-l, --logger` Enable logging (Optional).  
>`-h, --help` Help information (Optional).  

Usage example:  
```
python sender.py -m "Hello, chat" -r Alexx -l
```

### Installing:
```
git clone https://github.com/Maxim80/devman_async_python_connection_to_chat.git
pip3 install -r requirements.txt
cd devman_async_python_connection_to_chat/
python main.py
```

### Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
