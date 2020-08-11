# coding=cp1251

import xlrd

from app.shared.helpers import obj, Helpers


class ConnectorExcel:
    is_type_price_required = False

    company = None

    book = None

    def __init__(self, parent, company):
        super(ConnectorExcel, self).__init__()
        self.company = company
        self.parent = parent

    # check file and his structure
    def connect(self):

        if not self.company.int_file_path:
            self.parent.log('Не указан путь до файла', is_error=True)
            return False

        errors = []

        self.book = xlrd.open_workbook(self.company.int_file_path)

        def check_sheet(table_name, col_names):
            if table_name not in self.book.sheet_names():
                errors.append('Лист с именем "{}" не найден'.format(table_name))
            else:
                sheet = self.book.sheet_by_name(table_name)
                cols = [sheet.cell_value(0, i) for i in range(sheet.ncols)]
                for i, name in enumerate(col_names):
                    if name not in cols:
                        errors.append('Лист "{}": колонка "{}" не найдена'.format(table_name, name))
                    elif cols.index(name) != i:
                        errors.append('Лист "{}": колонка "{}" должна быть в {} столбце'.format(table_name, name, str(i + 1)))

        check_sheet('Товары', ['ID', 'Наименование'])
        check_sheet('Склады', ['ID', 'Наименование'])
        check_sheet('Остатки и цены', ['ID товара', 'ID точки продаж (склада)', 'Количество', 'Цена'])

        if len(errors) > 0:
            for error in errors:
                self.parent.log(error, is_error=True)

            self.parent.log('Похоже у вас возникли проблемы с открытием файла, '
                            'попробуйте скачать образец файла "source_excel.xlsx"')
            return False

        # self.parent.log('Файл проверен, ошибок в структуре не найдено')

        return self.book

    def disconnect(self):
        return True

    def is_connected(self):
        return self.book is not None

    def get_company(self):
        company = obj({
            'int_name': self.company.ext_name,
            'int_inn': self.company.ext_inn,
        })
        return company

    def get_items(self, array_ids):
        if not self.connect():
            return

        sheet = self.book.sheet_by_name('Товары')

        array = []
        for i in range(1, sheet.nrows):
            item = obj({})
            item.int_id = str(sheet.cell_value(i, 0)).strip()
            if item.int_id not in array_ids:
                continue
            item.int_name = sheet.cell_value(i, 1)
            array.append(item)

        return array

    def get_points(self, array_ids):
        if not self.connect():
            return

        sheet = self.book.sheet_by_name('Склады')

        array = []
        for i in range(1, sheet.nrows):
            item = obj({})
            item.int_id = str(sheet.cell_value(i, 0)).strip()
            if item.int_id not in array_ids:
                continue
            item.int_name = sheet.cell_value(i, 1)
            array.append(item)

        return array

    def get_count_and_price_in_points(self, item_ids, point_ids, type_price):
        if not self.connect():
            return

        sheet = self.book.sheet_by_name('Остатки и цены')

        items = []

        for i in range(1, sheet.nrows):
            item_id = str(sheet.cell_value(i, 0)).strip()
            if item_id not in item_ids:
                continue
            point_id = str(sheet.cell_value(i, 1)).strip()
            if point_id not in point_ids:
                continue

            int_count = Helpers.parse_float(sheet.cell_value(i, 2))
            int_price = Helpers.parse_float(sheet.cell_value(i, 3))

            item = obj()
            item.item_id_internal = item_id
            item.point_id_internal = point_id

            item.int_price = Helpers.convert_number(int_price, False)
            item.int_count = Helpers.convert_number(int_count, False)

            items.append(item)

        return items
