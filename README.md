# 🖱️ Python AutoClicker — Лёгкий и Быстрый Автокликер для Windows

**Python AutoClicker** — это простой, лёгкий и эффективный инструмент автоматизации кликов мыши. Программа написана на Python и позволяет настраивать интервал между кликами, автоматически кликать в нужной точке экрана и завершать работу по горячей клавише. Подходит для задач автоматизации, тестирования интерфейсов и игр.

---

## 🚀 Главные преимущества

- ⚡ **Моментальный запуск**: работает без лишних окон и зависимостей.
- 🧠 **Простой и понятный интерфейс** — запускается через консоль или по двойному клику по `.exe` файлу.
- 🔧 **Настраиваемый интервал кликов** — от долей секунды до нескольких секунд.
- ⌨️ **Удобное завершение** — нажмите `Ctrl + B` в любой момент.
- 💼 **Не требует установки** — готовый `.exe` можно скачать и использовать без Python.

---

## 📦 Структура проекта

```
AutoClicker/
├── .gitignore # Исключения для Git
├── dist/
  └── main.exe # Готовый исполняемый файл для Windows
├── main.py # Исходный код автокликера
└── requirements.txt # Зависимости для запуска из Python
```

---

## 🖥️ Как начать использовать

### ✅ Вариант 1: Скачать готовый `.exe`

1. Перейдите в папку `dist/`.
2. Скачайте файл [`main.exe`](dist/main.exe).
3. Запустите файл. Всё готово! Python не нужен.

### ⚙️ Вариант 2: Запуск из исходников (для разработчиков)

#### 1. Установка зависимостей

Убедитесь, что у вас установлен Python 3.7+  
Затем выполните:

```bash
python -m venv venv
source venv/bin/activate  # Для Linux/Mac
venv\Scripts\activate     # Для Windows
pip install -r requirements.txt
```
#### 2. Запуск
```bash
python main.py
```
#### 3. Управление
- Введите желаемый интервал между кликами (например, 0.2 для двух кликов в секунду).

- Чтобы остановить автокликер, нажмите Ctrl + B.

## 📂 Зависимости
- pyautogui
- pyinstaller (для сборки)

## 🛠️ Как собрать .exe самостоятельно (по желанию)
```bash
pip install pyinstaller
pyinstaller --onefile main.py
```
Готовый файл появится в папке dist/.

## 🧩 Где пригодится AutoClicker

- В автоматизации рутинных действий в Windows
- При тестировании GUI-приложений
- В играх, требующих частого клика
- Для ускорения работы с интерфейсами

## 🔍 SEO ключевые слова
Автокликер Python, AutoClicker Windows, auto clicker .exe скачать, автоматизация кликов, pyautogui clicker, лёгкий автокликер для Windows, open-source автокликер, автокликер без установки

## 📄 Лицензия
Проект распространяется под лицензией MIT. Используйте свободно.

Разработано с ❤️ на Python, чтобы сделать вашу работу быстрее и легче.