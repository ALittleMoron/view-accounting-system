# 📁 view-accounting-system

## 📖 Кратко о проекте

Проект представляет собой систему для учета заказанных видео с возможностью автоматической
записи всей информации в базу данных при помощи API донатных систем или в ручном режиме.

! Описание будет дополняться по мере моих раздумий над проектом.

---

## 🧾 Чеклист

- [ ] Инициировать проект (окружение, настройки, тестовый вывод домашней стр. и др.).
- [ ] Backend на FastAPI (основной функционал).
- [ ] Frontend на React (основной функционал).
- [ ] Хорошо провести время за программированием всего этого.

Более подробный TODO [тут](./project.todo).

---

## 💻 Запуск проекта

### С poetry/pip

В проекте используется [poetry](https://github.com/python-poetry/poetry) -
менеджер зависимостей. Для его установки на OSX / Linuxosx / linux /
bashonwindows используейте команду:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Для Windows:

```PowerShell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

### С docker compose
