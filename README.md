# 🚀 SoloBot

**SoloBot**!  
Бот для API 3x-UI VPN на протоколе vless
Бот для vless

## 📋 Оглавление
1. [Описание](#Описание)
2. [Требования](#Требования)
3. [Установка](#установка)
4. [Конфигурация](#конфигурация)
5. [Запуск](#запуск)
6. [Автор](#SoloBot)

---

## 📖 Описание

Бот предназначен для автоматизирования выдачи ключей, хранении их в базе данных и управления подключениями.
Также реализованы функции смены локации, автоматических и ручных уведомлений


---

## 💻 Требования

Для работы проекта необходимы следующие компоненты:

- **Python** версии 3.8 или выше
- **Git** для клонирования репозитория
- **Virtualenv** для создания виртуального окружения (рекомендуется)
- **postgresql** для работы базы данных

---

## ⚙️ Установка

### 1️⃣ Шаг 1: Клонирование репозитория

Клонируйте репозиторий и перейдите в его директорию:

```bash
git clone https://github.com/Vladless/Solo_bot.git
cd solo_bot
```

### 2️⃣ Шаг 2: Создание и активация виртуального окружения

```
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Шаг 3: Установка зависимостей

```
pip install -r requirements.txt
```

### 🛠️ Конфигурация

Для правильной работы вам нужно:

* установить и запустить postgresql, создать пользователя для работы с базой данных и выдать ему права
* Настроить ваш сервер на работу с ботом, выпустить SSL сертификат для домена
* Настроить вебхуки и пути до них в NGINX

* Создать файл config.py в корневой папке проекта с вашими данными:

```

API_TOKEN = токен вашего бота телеграм

ADMIN_USERNAME = логин от вашей панели x-ray
ADMIN_PASSWORD = пароль от вашей панели x-ray
ADD_CLIENT_URL = f"{API_URL}/panel/api/inbounds/addClient"
GET_INBOUNDS_URL = f"{API_URL}/panel/api/inbounds/list/"
AUTH_URL = f"{API_URL}/login/"
DATABASE_URL = путь к вашей базе данных, имеет вид "postgresql://{user}:{password}@{Ip-adress}:{port}/{имя базы данных}"
ADMIN_ID = ID телеграм профиля администратора
CHANNEL_URL = ссылка на ваш телеграм канал
YOOKASSA_SECRET_KEY = ваш ключ юкассы
YOOKASSA_SHOP_ID = ваш шопайди
WEBHOOK_HOST = адрес вашего сервера для вебхуков
WEBHOOK_PATH = '/webhook/' 
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
SUPPORT_CHAT_URL = ваша ссылка на поддержку 
```

### 🚀 Запуск

введите команду из виртуального окружения

```
python main.py
```
### 🔗 SoloBot в Telegram и Полная версия

Попробуйте SoloBot прямо сейчас в Telegram [по этой ссылке](https://t.me/SoloNetVPN_bot).

Вы также можете поддержать автора или купить полную версию бота с сопровождением по установке в поддержке бота!
Полная пошаговая инстуркция по запуску бота предоставляется в поддержке бота
