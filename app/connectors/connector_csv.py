import pandas

from app.shared.helpers import obj, Helpers

class ConnectorCSV:
    is_type_price_required = False

    company = None

    book = None

    def __init__(self, parent, company):
        super(ConnectorCSV, self).__init__()
        self.company = company
        self.parent = parent

    # check file and his structure
    def connect(self):

        if not self.company.int_file_path:
            self.parent.log('Не указан путь до файла', is_error=True)
            return False

        errors = []

        col_names = ['item_id', 'point_id', 'count', 'price', 'item_name', 'point_name']

        self.data = pandas.read_csv(self.company.int_file_path)

        if self.data is None:
            return False

        cols = list(self.data.columns)
        for i, name in enumerate(col_names):
            if name not in cols:
                errors.append('Колонка "{}" не найдена'.format(name))
            # elif cols.index(name) != i:
            #     errors.append('Колонка "{}" должна быть в {} столбце'.format(name, str(i + 1)))

        if len(errors) > 0:
            for error in errors:
                self.parent.log(error, is_error=True)

            self.parent.log('Похоже у вас возникли проблемы с открытием файла, '
                            'попробуйте скачать образец файла "source_excel.csv"')
            return False

        # self.parent.log('Файл проверен, ошибок в структуре не найдено')

        return True

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

        data = self.data
        filtered = data[data['item_id'].isin(array_ids)].sort_values(by=['item_name'])

        array = []
        array_exist = []

        for index, row in filtered.iterrows():
            item = obj({})
            item.int_id = str(row['item_id']).strip()
            if item.int_id in array_exist:
                continue
            item.int_name = row['item_name']
            array.append(item)
            array_exist.append(item.int_id)

        return array

    def get_points(self, array_ids):
        if not self.connect():
            return

        data = self.data
        filtered = data[data['point_id'].isin(array_ids)].sort_values(by=['point_name'])

        array = []
        array_exist = []

        for index, row in filtered.iterrows():
            item = obj({})
            item.int_id = str(row['point_id']).strip()
            if item.int_id in array_exist:
                continue
            item.int_name = row['point_name']
            array.append(item)
            array_exist.append(item.int_id)

        return array

    def get_count_and_price_in_points(self, item_ids, point_ids, type_price):
        if not self.connect():
            return

        data = self.data

        items = []

        for index, row in data.iterrows():
            item_id = str(row['item_id']).strip()
            if item_id not in item_ids:
                continue
            point_id = str(row['point_id']).strip()
            if point_id not in point_ids:
                continue

            int_count = Helpers.parse_float(row['count'])
            int_price = Helpers.parse_float(row['price'])

            item = obj()
            item.item_id_internal = item_id
            item.point_id_internal = point_id

            item.int_price = Helpers.convert_number(int_price, False)
            item.int_count = Helpers.convert_number(int_count, False)

            items.append(item)

        return items
