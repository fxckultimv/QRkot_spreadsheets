from datetime import datetime

from aiogoogle import Aiogoogle
from const import PERMISSIONS, SPREADSHEET_TEMPLATE, TABLE_VALUES

from app.core.config import settings
from app.models.charity_project import CharityProject


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
):
    permissions_body = PERMISSIONS
    service = await wrapper_services.discover(
        'drive', settings.DRIVE_VERSION
    )
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields='id'
        )
    )


async def spreadsheets_create(
        wrapper_services: Aiogoogle,
        body: dict = None
) -> tuple[str, str]:
    body = SPREADSHEET_TEMPLATE.copy()
    now_date_time = datetime.now().strftime(settings.FORMAT)
    body["properties"]["title"] = f"{settings.TITLE}{now_date_time}"
    service = await wrapper_services.discover(
        "sheets", settings.SPREADSHEETS_VERSION
    )
    request = service.spreadsheets().create(body=body)
    response = await request.execute()
    return response["spreadsheet_id"], response["spreadsheet_url"]


async def spreadsheets_update_value(
        spreadsheet_id: str,
        projects: list[CharityProject],
        wrapper_services: Aiogoogle,
):
    table_values = [
        [settings.TITLE, datetime.now().strftime(settings.FORMAT)],
        *TABLE_VALUES,
        *[
            list(
                map(
                    str,
                    [
                        project.name,
                        project.close_date - project.create_date,
                        project.description,
                    ],
                )
            )
            for project in projects
        ],
    ]

    table_row_count = len(table_values)
    table_column_count = max(map(len, table_values))
    if (
            table_row_count > settings.ROW_COUNT
    ) or (
            table_column_count > settings.COLUMN_COUNT
    ):
        raise ValueError(
            (
                'Невозможно поместить данные размером {}x{} в '
                'таблице размером {}x{}.'
            ).format(
                table_column_count,
                table_row_count,
                settings.COLUMN_COUNT,
                settings.ROW_COUNT,
            ),
        )
    await wrapper_services.as_service_account(
        (
            await wrapper_services.discover(
                'sheets', settings.SPREADSHEETS_VERSION
            )
        ).spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=f'R1C1:R{table_row_count}C{table_column_count}',
            valueInputOption='USER_ENTERED',
            json={'majorDimension': 'ROWS', 'values': table_values},
        )
    )
