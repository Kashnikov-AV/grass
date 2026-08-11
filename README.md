# Grass — Социальная сеть для поиска работы в сельском хозяйстве

**Grass** — это платформа, которая соединяет работодателей и соискателей в сфере сельского хозяйства. Проект предоставляет удобный интерфейс для создания профилей, публикации вакансий, общения в чате и получения аналитики по рынку труда.

---

## 📋 Оглавление

- [О проекте](#о-проекте)
- [Основные возможности](#основные-возможности)
- [Технологический стек](#технологический-стек)
- [Структура проекта](#структура-проекта)
- [Установка и запуск](#установка-и-запуск)
  - [Требования](#требования)
  - [Запуск через Docker (рекомендуется)](#запуск-через-docker-рекомендуется)
  - [Локальная разработка](#локальная-разработка)
- [Конфигурация](#конфигурация)
- [Модули приложения](#модули-приложения)
- [API и маршруты](#api-и-маршруты)
- [Разработка](#разработка)
- [Лицензия](#лицензия)

---

## 🌱 О проекте

Grass решает проблему трудоустройства в сельскохозяйственной отрасли, предоставляя единую платформу для:
- **Соискателей** — создание профиля, поиск подходящих вакансий, отклик на предложения
- **Работодателей** — публикация вакансий, поиск квалифицированных специалистов, управление откликами
- **Аналитики** — мониторинг рынка труда, статистика по вакансиям и спросу

---

## ✨ Основные возможности

- 👤 **Профили пользователей**
  - Раздельные профили для работников и работодателей
  - Загрузка аватаров и документов
  - Расширенная информация о навыках и опыте

- 💼 **Вакансии**
  - Публикация и редактирование вакансий
  - Фильтрация по категориям, регионам, типу занятости
  - Отклики на вакансии

- 💬 **Чат**
  - Real-time общение между пользователями
  - Поддержка WebSocket через Django Channels
  - История сообщений

- 📊 **Аналитика**
  - Статистика по вакансиям
  - Графики и визуализация данных (Plotly)
  - Анализ рынка труда по регионам

- 🔐 **Авторизация и регистрация**
  - Регистрация через email
  - Вход через социальные сети (OAuth)
  - JWT-аутентификация для API
  - Восстановление пароля

- 🏠 **Главная страница**
  - Лента вакансий
  - Рекомендации
  - Новости платформы

---

## 🛠 Технологический стек

### Backend
- **Django 4.2.3** — основной фреймворк
- **Django REST Framework 3.13.1** — построение API
- **Django Channels 4.0.0** — поддержка WebSocket и асинхронных соединений
- **Redis** — кэширование и брокер сообщений для Channels
- **PostgreSQL 15** — основная база данных
- **Gunicorn & Daphne** — ASGI/WSGI серверы

### Frontend
- **HTMX 1.16.0** — динамические запросы без написания JavaScript
- **Alpine.js** — легковесная реактивность для интерактивных элементов
- **Template Engine** — шаблонизатор Django

### Аналитика и визуализация
- **Pandas 2.1.4** — обработка данных
- **Plotly 5.18.0** — интерактивные графики
- **NumPy 1.26.2** — численные вычисления

### Безопасность и аутентификация
- **djoser 2.1.0** — регистрация и аутентификация
- **djangorestframework-simplejwt 4.8.0** — JWT-токены
- **social-auth-app-django 4.0.0** — OAuth-аутентификация
- **django-phonenumber-field 6.1.0** — валидация номеров телефонов

### DevOps
- **Docker & Docker Compose** — контейнеризация
- **Nginx** — обратный прокси и раздача статики
- **Let's Encrypt** — SSL-сертификаты

---

## 📁 Структура проекта

```
grass/
├── analytics_app/          # Модуль аналитики и статистики
├── chat_app/               # Модуль чата (WebSocket)
├── city_app/               # Модуль городов и регионов
├── grass/                  # Основной проект Django
│   ├── settings.py         # Настройки проекта
│   ├── urls.py             # Корневые URL-маршруты
│   ├── asgi.py             # ASGI-конфигурация
│   └── wsgi.py             # WSGI-конфигурация
├── home_app/               # Главная страница
├── profile_app/            # Профили пользователей
├── signup_app/             # Регистрация и аутентификация
├── users_app/              # Управление пользователями
├── vacancy_app/            # Вакансии и отклики
├── static/                 # Статические файлы (CSS, JS, изображения)
├── templates/              # HTML-шаблоны
├── media/                  # Загружаемые пользователем файлы
├── nginx/                  # Конфигурация Nginx
├── docker-compose.yml      # Docker Compose конфигурация
├── Dockerfile              # Docker образ приложения
├── requirements.txt        # Python-зависимости
└── manage.py               # Утилита управления Django
```

---

## 🚀 Установка и запуск

### Требования

- Docker 20+
- Docker Compose 1.29+
- Или для локальной разработки:
  - Python 3.11
  - PostgreSQL 15
  - Redis

### Запуск через Docker (рекомендуется)

1. **Клонируйте репозиторий:**
   ```bash
   git clone <repository-url>
   cd grass
   ```

2. **Создайте файл `.env` в директории `grass/`:**
   ```env
   POSTGRES_DB=grass_db
   POSTGRES_USER=grass_user
   POSTGRES_PASSWORD=your_secure_password
   SECRET_KEY=your_django_secret_key
   DEBUG=False
   ALLOWED_HOSTS=localhost,127.0.0.1,your_domain.com
   ```

3. **Запустите контейнеры:**
   ```bash
   cd grass
   docker-compose up --build -d
   ```

4. **Примените миграции (если не применились автоматически):**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

5. **Создайте суперпользователя:**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

6. **Откройте приложение:**
   - Веб-интерфейс: `http://localhost` или `https://your_domain.com`
   - Админ-панель: `http://localhost/admin/`

7. **Просмотр логов:**
   ```bash
   docker-compose logs -f
   ```

8. **Остановка контейнеров:**
   ```bash
   docker-compose down
   ```

### Локальная разработка

1. **Установите зависимости:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Настройте базу данных PostgreSQL:**
   ```sql
   CREATE DATABASE grass_db;
   CREATE USER grass_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE grass_db TO grass_user;
   ```

3. **Настройте переменные окружения:**
   Создайте файл `.env` или экспортируйте переменные:
   ```bash
   export SECRET_KEY='your-secret-key'
   export DEBUG=True
   export DATABASE_URL=postgres://grass_user:your_password@localhost:5432/grass_db
   export REDIS_URL=redis://localhost:6379/0
   ```

4. **Запустите Redis:**
   ```bash
   redis-server
   ```

5. **Примените миграции:**
   ```bash
   python manage.py migrate
   ```

6. **Соберите статические файлы:**
   ```bash
   python manage.py collectstatic
   ```

7. **Запустите сервер разработки:**
   ```bash
   python manage.py runserver
   ```

8. **Для поддержки WebSocket запустите Daphne:**
   ```bash
   daphne -p 8000 grass.asgi:application
   ```

---

## ⚙️ Конфигурация

### Переменные окружения

| Переменная | Описание | Пример |
|------------|----------|--------|
| `SECRET_KEY` | Секретный ключ Django | `your-secret-key` |
| `DEBUG` | Режим отладки | `True` / `False` |
| `ALLOWED_HOSTS` | Разрешённые хосты | `localhost,example.com` |
| `POSTGRES_DB` | Имя базы данных | `grass_db` |
| `POSTGRES_USER` | Пользователь PostgreSQL | `grass_user` |
| `POSTGRES_PASSWORD` | Пароль PostgreSQL | `secure_password` |
| `REDIS_URL` | URL Redis | `redis://redis:6379/0` |
| `EMAIL_HOST` | SMTP-сервер для почты | `smtp.gmail.com` |
| `EMAIL_PORT` | Порт SMTP | `587` |

### Настройка HTTPS (Production)

Проект поддерживает SSL через Let's Encrypt:

1. Установите Certbot:
   ```bash
   apt-get install certbot
   ```

2. Получите сертификат:
   ```bash
   certbot certonly --webroot -w /var/www/certbot -d your_domain.com
   ```

3. Контейнеры автоматически подключат сертификаты из `/etc/letsencrypt`.

---

## 📦 Модули приложения

### 1. `analytics_app` — Аналитика
- Сбор статистики по вакансиям
- Визуализация данных (графики, диаграммы)
- Анализ трендов рынка труда
- **Технологии:** Pandas, Plotly, Django

### 2. `chat_app` — Чат
- Real-time сообщения через WebSocket
- Индивидуальные и групповые чаты
- История переписки
- **Технологии:** Django Channels, Redis, Alpine.js

### 3. `city_app` — Города и регионы
- Справочник городов (на основе `cities_cleaned.csv`)
- Привязка вакансий и профилей к локациям
- Поиск по регионам

### 4. `profile_app` — Профили
- Профиль соискателя (резюме, навыки, опыт)
- Профиль работодателя (информация о компании)
- Загрузка фото и документов
- Рейтинги и отзывы

### 5. `signup_app` — Регистрация и аутентификация
- Регистрация через email
- Вход через социальные сети (Google, VK, etc.)
- JWT-токены для API
- Восстановление пароля
- **Технологии:** Djoser, DRF SimpleJWT, Social Auth

### 6. `users_app` — Управление пользователями
- Кастомная модель пользователя
- Роли и права доступа
- Верификация пользователей

### 7. `vacancy_app` — Вакансии
- CRUD операции для вакансий
- Категории и теги
- Отклики на вакансии
- Фильтрация и поиск
- Статусы вакансий (активна, закрыта, на рассмотрении)

### 8. `home_app` — Главная страница
- Лента последних вакансий
- Рекомендуемые предложения
- Статистика платформы

---

## 🌐 API и маршруты

### Основные URL-маршруты

| Путь | Описание |
|------|----------|
| `/` | Редирект на главную |
| `/home/` | Главная страница |
| `/admin/` | Панель администратора Django |
| `/accounts/` | Аутентификация (регистрация, вход, выход) |
| `/profile/` | Управление профилем |
| `/vacancy/` | Вакансии (список, создание, детали) |
| `/analytics/` или `/analytic/` | Аналитика и статистика |
| `/chat/` | Чат (WebSocket) |
| `/coming-soon/` | Страница "В разработке" |
| `/test/` | Тестовая страница |

### API Endpoints (REST)

| Метод | Endpoint | Описание |
|-------|----------|----------|
| `POST` | `/api/auth/jwt/create/` | Получить JWT-токен |
| `POST` | `/api/auth/users/` | Регистрация пользователя |
| `GET` | `/api/vacancies/` | Список вакансий |
| `POST` | `/api/vacancies/` | Создать вакансию |
| `GET` | `/api/vacancies/{id}/` | Детали вакансии |
| `PUT` | `/api/vacancies/{id}/` | Обновить вакансию |
| `DELETE` | `/api/vacancies/{id}/` | Удалить вакансию |
| `GET` | `/api/profiles/` | Список профилей |
| `GET` | `/api/analytics/stats/` | Статистика платформы |

---

## 👨‍💻 Разработка

### Запуск тестов
```bash
python manage.py test
```

### Линтинг кода
```bash
flake8 .
```

### Создание миграций
```bash
python manage.py makemigrations
python manage.py migrate
```

### Сборка Docker-образа вручную
```bash
docker build -t grass-app .
```

### Работа с базой данных
```bash
# Дамп данных
python manage.py dumpdata > data.json

# Загрузка данных
python manage.py loaddata data.json
```

### Очистка статики и медиа
```bash
rm -rf staticfiles/*
rm -rf media/*
```

---

## 🤝 Вклад в проект

1. Fork репозитория
2. Создайте ветку (`git checkout -b feature/AmazingFeature`)
3. Commit изменения (`git commit -m 'Add some AmazingFeature'`)
4. Push в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

---

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. файл `LICENSE`.

---

## 📞 Контакты

- **Email:** support@grass.agro
- **Telegram:** @grass_support
- **GitHub:** [grass-project](https://github.com/your-org/grass)

---

## 🙏 Благодарности

- Команда Django за отличный фреймворк
- Разработчикам HTMX и Alpine.js за упрощение frontend-разработки
- Сообществу open-source за многочисленные библиотеки

---

**Grass** © 2024. Все права защищены.
