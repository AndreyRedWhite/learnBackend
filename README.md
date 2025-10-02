# Hotel Booking Service (учебный проект)

Сервис бронирования отелей: базовые сущности (отель, номер/категория номера, пользователь/клиент, бронь), CRUD-операции и поиск доступных номеров по датам. Проект пишется в рамках обучения Python backend.

> Репозиторий: https://github.com/AndreyRedWhite/learnBackend

## Стек

- Python 3.11+
- SQLAlchemy / Alembic (миграции)
- (Обычно) FastAPI + Uvicorn для REST API
- SQLite по умолчанию для локальной разработки; легко переключается на PostgreSQL

> В корне есть `alembic.ini`, а исходники лежат в `src/` (см. дерево репозитория). Также присутствуют `.github/workflows/` и `requirements.txt`. Это удобно для CI и воспроизводимой установки. :contentReference[oaicite:1]{index=1}

## Быстрый старт (локально)

### 1) Клонирование и окружение

```bash
git clone https://github.com/AndreyRedWhite/learnBackend.git
cd learnBackend

python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
# .venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install -r requirements.txt
