from app.core.config import settings

USER_PREFIX = ''
DONATION_PREFIX = '/donation'
CHARITY_PROJECT_PREFIX = '/charity_project'

USER_TAGS = []
DONATION_TAGS = ['Donations']
CHARITY_PROJECT_TAGS = ['Charity Projects']

PROJECT_NOT_FOUND_ERROR = 'Проект не найден'
PROJECT_EXISTS_ERROR = 'Проект с таким названием уже есть.'
FORBIDDEN_UPDATE_ERROR = 'Закрытый проект нельзя редактировать.'
INVESTED_RPOJECT_DELETE_ERROR = (
    'В проект инвестировали, невозможно удалить.'
)
INVALID_INVESTED_AMOUNT_ERROR = (
    'Новая сумма должна быть больше ранее внесенной'
)
JWT_TOKEN_LIFETIME = 3600
REPRESENTATION = (
    'Сумма: {full_amount}\n'
    'Дата создания: {create_date}\n'
    'В проект инвестировано: {invested_amount}\n'
    'Дата закрытия: {close_date}\n'
)
MIN_PASSWORD_LEN = 3
MAX_NAME_LEN = 100

GOOGLE_PREFIX = '/google'
GOOGLE_TAGS = ['Google']

PROJECT_NOT_FOUND_ERROR = 'Проект не найден'
PROJECT_EXISTS_ERROR = 'Проект с таким названием уже есть.'
FORBIDDEN_UPDATE_ERROR = 'Закрытый проект нельзя редактировать.'
INVESTED_RPOJECT_DELETE_ERROR = (
    'В проект инвестировали, невозможно удалить.'
)
INVALID_INVESTED_AMOUNT_ERROR = (
    'Новая сумма должна быть больше ранее внесенной'
)

EXCLUDE_FIELDS = (
    'user_id',
    'invested_amount',
    'fully_invested',
    'close_date'
)


USER_DELETION_ERROR = 'Удалять пользователя запрещено.'

SPREADSHEET_TEMPLATE = {
    "properties": {
        "title": "Отчёт от {date_time}",
        "locale": "ru_RU",
    },
    "sheets": [
        {
            "properties": {
                "sheetType": "GRID",
                "sheetId": 0,
                "title": "Лист1",
                "gridProperties": {
                    "rowCount": settings.ROW_COUNT,
                    "columnCount": settings.COLUMN_COUNT,
                },
            }
        }
    ],
}
TABLE_VALUES = [
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание'],
]

PERMISSIONS = {'type': 'user',
               'role': 'writer',
               'emailAddress': settings.email}
