import logging
import sqlite3

from PySide2.QtCore import QSettings, QCoreApplication

from app.shared.constants import Constants
from app.shared.helpers import Helpers, obj


class StorageService(object):
    settings = None

    conn = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(StorageService, cls).__new__(cls)
            cls.instance.on_init()
        return cls.instance

    def on_init(self):
        # logging.getLogger(__name__)
        self.settings = QSettings('settings.ini', QSettings.IniFormat)  # , 'Tarder', 'Sync'
        self.settings.sync()
        self.settings_autoload = QSettings("HKEY_CURRENT_USER\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
                                           , QSettings.NativeFormat)
        self.base_init()

    def set_value(self, name, value):
        self.settings.setValue(name, value)
        self.settings.sync()

    def get_value(self, name):
        return self.settings.value(name)

    def base_init(self):

        try:
            self.conn = sqlite3.connect('database.db')
            # self.conn = sqlite3.connect(':memory:')
            self.conn.row_factory = sqlite3.Row
            logging.info("DB connection created")
        except sqlite3.Error as err:
            logging.error("DB Error create connection: " + str(err))
            return

        # # recreate base
        # if Constants.APP_VERSION != self.get_value('APP_VERSION'):
        #     if self.base_delete_all():
        #         logging.info("DB successfully removed all tables")
        #     else:
        #         logging.info("DB STOPPED removed all tables")
        #         return False

        if Constants.APP_VERSION != self.get_value('APP_VERSION'):
            from app.shared.main_service import MainService
            if self.base_update_tables() or Variables().isDebug:  # create or update tables
                self.set_value('APP_VERSION', Constants.APP_VERSION)
                pass
        pass

    def create_table(self, query):
        logging.debug("DB query: " + query)
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return True
        except sqlite3.Error as err:
            logging.error("DB Error create table: " + str(err))
            return False

    def table_exists(self, table_name):
        query = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='{}';".format(table_name)
        return self.execute_count(query)

    def update_table(self, table_name, query_create, fields_to_copy):

        if not self.table_exists(table_name):
            return self.create_table(query_create)
        else:

            cursor = self.conn.cursor()
            cursor.execute('PRAGMA table_info({})'.format(table_name))
            fields_exist_to_copy = []
            for r in cursor.fetchall():
                field_name = str(r['name'])
                if field_name in fields_to_copy:
                    fields_exist_to_copy.append(field_name)

            fields_to_copy_string = ", ".join(map("{}".format, fields_exist_to_copy))
            query = """
                    PRAGMA foreign_keys=off;
    
                    BEGIN TRANSACTION;
                    
                    DROP TABLE IF EXISTS _{table_name}_old;
                    
                    ALTER TABLE {table_name} RENAME TO _{table_name}_old;
                    
                    {query_create};
                    
                    INSERT INTO {table_name} ({fields_to_copy})
                      SELECT {fields_to_copy}
                      FROM _{table_name}_old;
                    
                    DROP TABLE _{table_name}_old;
                    
                    COMMIT;
                    
                    PRAGMA foreign_keys=on;
            """.format(
                table_name=table_name,
                query_create=query_create,
                fields_to_copy=fields_to_copy_string)
            logging.debug("DB query: " + query)
            try:
                cursor = self.conn.cursor()
                cursor.executescript(query)
                return True
            except sqlite3.Error as err:
                logging.error("DB Error update table: " + str(err))
                return False

    def delete_table(self, name):
        query = 'DROP TABLE IF EXISTS {}'.format(name)
        logging.debug("DB query: " + query)
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return True
        except sqlite3.Error as err:
            logging.error("DB Error delete table: " + str(err))
            return False

    def create_index(self, query):
        logging.debug("DB query: " + query)
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            return True
        except sqlite3.Error as err:
            logging.error("DB Error create index: " + str(err))
            return False

    def execute_count(self, query, values=None):
        logging.debug("DB query: " + query)
        try:
            cursor = self.conn.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            result = cursor.fetchone()
            return result[0]
        except sqlite3.Error as err:
            logging.error("DB Error: " + str(err))
            return False

    def execute(self, query, values=None):
        logging.debug("DB query: " + query)
        try:
            cursor = self.conn.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            self.conn.commit()
            return True
        except sqlite3.Error as err:
            logging.error("DB Error: " + str(err))
            return False

    def execute_select(self, query, values=None):
        logging.debug("DB query: " + query)
        try:
            cursor = self.conn.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)

            data = []
            for r in cursor.fetchall():
                data.append(dict(r))
            # res = cursor.execute(query).fetchall()
            # data = dict(zip([c[0] for c in cursor.description], res[0]))
            data = Helpers.to_obj(data)
            return data
        except sqlite3.Error as err:
            logging.error("DB Error select : " + str(err))
            return False

    def base_delete_all(self):
        tables = ['companies', 'items', 'points', 'item_in_points']
        for table in tables:
            if not self.delete_table(table):
                return False

        return True

    def base_update_tables(self):
        logging.info("DB STARTED working with tables")

        # if self.base_delete_all():
        #     logging.info("DB successfully removed all tables")
        # else:
        #     logging.info("DB STOPPED removed all tables")
        #     return False

        # create companies table
        if not (
                self.update_table('companies',
                                  """
CREATE TABLE IF NOT EXISTS companies
(
    ext_id text PRIMARY KEY, ext_inn text NOT NULL, ext_name text NOT NULL,
    int_inn text, int_name text,
    int_source_type integer, int_con_type integer, int_1c_type integer, int_1c_com text, 
    int_file_path text, int_base_path text, int_server_name text, int_base_name text,  
    int_base_login text, int_base_password text, int_type_price text,
    ext_enable integer,
    int_enable integer, sync_main_now integer, sync_main text, sync_main_error text, sync_main_next text,
    sync_server_items_now integer, sync_server_items text, sync_server_items_error text,
    sync_source_items_now integer, sync_source_items text, sync_source_items_error text,
    sync_server_points_now integer, sync_server_points text, sync_server_points_error text,
    sync_source_points_now integer, sync_source_points text, sync_source_points_error text,
    sync_source_iip_now integer, sync_source_iip text, sync_source_iip_error text,
    sync_server_iip_now integer, sync_server_iip text, sync_server_iip_error text
)
                                  """, [
                                      'ext_id', 'ext_inn', 'ext_name', 'int_inn', 'int_name', 'int_source_type',
                                      'int_con_type', 'int_1c_type', 'int_1c_com', 'int_file_path', 'int_base_path',
                                      'int_server_name', 'int_base_name', 'int_base_login', 'int_base_password',
                                      'int_type_price', 'ext_enable', 'int_enable',
                                      'sync_main_now', 'sync_main', 'sync_main_error', 'sync_main_next',
                                      'sync_server_items_now', 'sync_server_items', 'sync_server_items_error',
                                      'sync_source_items_now', 'sync_source_items', 'sync_source_items_error',
                                      'sync_server_points_now', 'sync_server_points', 'sync_server_points_error',
                                      'sync_source_points_now', 'sync_source_points', 'sync_source_points_error',
                                      'sync_source_iip_now', 'sync_source_iip', 'sync_source_iip_error',
                                      'sync_server_iip_now', 'sync_server_iip', 'sync_server_iip_error'
                                  ])
        ):
            logging.error("DB STOPPED working with table companies")
            return False

        # create items table
        if not (
                self.update_table('items',
                                  """
                                CREATE TABLE IF NOT EXISTS items
                                (ext_id text PRIMARY KEY, ext_company_id text NOT NULL, ext_name text, ext_sku text, 
                                ext_id_internal text, int_id text, int_name text)
                                """, [
                                      'ext_id', 'ext_company_id', 'ext_name', 'ext_sku', 'ext_id_internal',
                                      'int_id', 'int_name'
                                  ])
                and self.create_index("""
                                CREATE INDEX IF NOT EXISTS dx_items_ext_company_id
                                ON items (ext_company_id)
                                """)
                and self.create_index("""
                                CREATE INDEX IF NOT EXISTS idx_items_ext_id_internal
                                ON items (ext_id_internal)
                                """)
        ):
            logging.error("DB STOPPED working with table items")
            return False

        # create points table
        if not (
                self.update_table('points',
                                  """
                                CREATE TABLE IF NOT EXISTS points
                                (ext_id text PRIMARY KEY, ext_company_id text NOT NULL, ext_name text, 
                                ext_id_internal text, int_id text, int_name text)
                                """, [
                                      'ext_id', 'ext_company_id', 'ext_name', 'ext_id_internal', 'int_id', 'int_name'
                                  ])
        ):
            logging.error("DB STOPPED working with table points")
            return False

        # create item in points table
        if not (
                self.update_table('item_in_points',
                                  """
                                CREATE TABLE IF NOT EXISTS item_in_points
                                (ext_id text, 
                                item_id_internal text NOT NULL, point_id_internal text NOT NULL, 
                                ext_price INTEGER, ext_count INTEGER, 
                                int_price INTEGER, int_count INTEGER, 
                                PRIMARY KEY (item_id_internal, point_id_internal))
                                """, [
                                      'ext_id', 'item_id_internal', 'point_id_internal', 'ext_price', 'ext_count',
                                      'int_price', 'int_count'
                                  ])
        ):
            logging.error("DB STOPPED working with table item_in_points")
            return False

        logging.info("DB DONE working with tables")
        return True

    def base_remove(self):

        pass

    def update_row(self, table, id_key, item, where=None):
        # id_value = None
        # columns = []
        # values = []
        # for key, value in item.items():
        #     if key == id_key:
        #         id_value = value
        #     else:
        #         columns.append(key)
        #         values.append(value)
        #
        # if isinstance(id_value, str):
        #     id_value = '"{}"'.format(id_value)
        #
        # data = ", ".join(map("{} = ?".format, columns))
        #
        # sql = "UPDATE {table} SET {data} WHERE {id_key} = {id_value}".format(
        #     table=table, data=data, id_key=id_key, id_value=id_value
        # )
        # return self.execute(sql, values)

        id_value = None
        columns = []
        values = []
        for key, value in item.items():
            if key == id_key:
                id_value = value
            columns.append(key)
            values.append(value)

        data_update = ", ".join(map("{} = ?".format, columns))

        data_where = ''
        if where:
            data_where = " AND ".join(map(lambda x: "{} = '{}'".format(x, where[x]), where))
        else:
            data_where = "{} = '{}'".format(id_key, id_value)

        sql = """ UPDATE {table} SET {data_update} WHERE {data_where} """.format(
            table=table, data_update=data_update, data_where=data_where
        )
        return self.execute(sql, values)

    def update_rows(self, table, fields, where=None):
        columns = []
        values = []
        for key, value in fields.items():
            columns.append(key)
            values.append(value)

        data = ", ".join(map("{} = ?".format, columns))

        data_where = ''
        if where:
            data_where = " AND ".join(map(lambda x: "{} = '{}'".format(x, where[x]), where))
            sql = "UPDATE {table} SET {data} WHERE {data_where} ".format(
                table=table, data=data, data_where=data_where
            )
        else:
            sql = "UPDATE {table} SET {data}".format(
                table=table, data=data
            )
        return self.execute(sql, values)

    def upsert_row(self, table, id_key, item, where=None):
        id_value = None
        columns = []
        values = []
        for key, value in item.items():
            if key == id_key:
                id_value = value
            columns.append(key)
            values.append(value)

        data_insert_cols = ", ".join(columns)
        data_insert_values = ", ".join(map("?".format, values))

        data_update = ", ".join(map("{} = ?".format, columns))

        data_where = ''
        data_conflict = ''
        if where:
            data_where = " AND ".join(map(lambda x: "{} = '{}'".format(x, where[x]), where))
            data_conflict = ", ".join(map(lambda x: "{}".format(x), where))
        else:
            data_where = "{} = '{}'".format(id_key, id_value)
            data_conflict = "{}".format(id_key)

        sql = """
                INSERT INTO {table} ({data_insert_cols}) VALUES({data_insert_values}) 
                ON CONFLICT({data_conflict}) 
                DO UPDATE SET {data_update} WHERE {data_where}
            """.format(
            table=table, data_insert_cols=data_insert_cols, data_insert_values=data_insert_values,
            data_update=data_update, data_where=data_where, data_conflict=data_conflict
        )
        return self.execute(sql, values + values)

    # # companies from Tarder
    # def set_companies(self, array):
    #     cursor = self.conn.cursor()
    #     try:
    #         items = []
    #         for item in array:
    #             items.append((
    #                 item['id'],
    #                 item['inn'],
    #                 item['name']
    #             ))
    #
    #         cursor.executemany("REPLACE INTO companies (ext_id, ext_inn, ext_name) VALUES (?,?,?)", items)
    #         self.conn.commit()
    #     except sqlite3.DatabaseError as err:
    #         logging.error("set_companies: " + str(err))
    #
    #     pass

    def get_companies(self):
        array = self.execute_select("SELECT * FROM companies")
        if not array:
            return array

        for company in array:
            if company.int_source_type is None:
                company.int_source_type = 0
            if company.int_con_type is None:
                company.int_con_type = 0
            if company.int_1c_type is None:
                company.int_1c_type = 0

        return array
        pass

    def get_company(self, inn):
        company = self.execute_select("SELECT * FROM companies WHERE ext_inn = ?", [inn])
        if len(company) > 0:
            company = company[0]
        else:
            company = None
        return company

    # def set_items(self, array, on_success = lambda x: x, on_error = lambda x: x):
    #     cursor = self.conn.cursor()
    #     try:
    #         items = []
    #         for item in array:
    #             items.append((
    #                 item['id'],
    #                 item['companyId'],
    #                 item['name'],
    #                 item['sku'],
    #                 item['idInternal']
    #             ))
    #
    #         cursor.executemany("REPLACE INTO items ("
    #                            "ext_id, ext_company_id, ext_name, ext_sku, ext_id_internal"
    #                            ") VALUES (?,?,?,?,?)", items)
    #         self.conn.commit()
    #     except sqlite3.DatabaseError as err:
    #         logging.error("set_items: " + str(err))
    #
    #     pass

    def upsert_companies(self, companies, on_success=lambda x: x, on_error=lambda x: x):
        try:

            # for first - make inactive all companies (we receive only active)
            fields = {
                'ext_enable': 0,
            }
            if not self.update_rows('companies', fields):
                err = 'Ошибка обнуления значения "включено"'
                from app.shared.main_service import MainService

                logging.error(err)
                if on_error:
                    on_error(err)
                return False

            for company in companies:
                fields = {
                    'ext_id': company.id,
                    'ext_inn': company.inn,
                    'ext_name': company.name,
                    'ext_enable': 1,
                }
                if not self.upsert_row('companies', 'ext_id', fields):
                    err = 'Обновление компаний завершено с ошибкой'
                    from app.shared.main_service import MainService
                    logging.error(err)
                    if on_error:
                        on_error(err)
                    return False

            if on_success:
                on_success(True)



        except sqlite3.DatabaseError as err:
            logging.error("upsert_companies: " + str(err))

            if on_error:
                on_error(err)

        pass

    def update_company(self, company, on_success=lambda x: x, on_error=lambda x: x):
        try:

            self.update_row('companies', 'ext_id', company)

            if on_success:
                on_success(True)

            return True

        except sqlite3.DatabaseError as err:
            logging.error("update_company: " + str(err))

            if on_error:
                on_error(err)

        return False

    # ITEMS

    def upsert_items(self, array, on_success=lambda x: x, on_error=lambda x: x):
        try:

            for item in array:
                fields = {
                    'ext_id': item.id,
                    'ext_company_id': item.companyId,
                    'ext_name': item.name,
                    'ext_sku': item.sku,
                    'ext_id_internal': item.idInternal
                }
                self.upsert_row('items', 'ext_id', fields)

            if on_success:
                on_success(True)

        except sqlite3.DatabaseError as err:
            logging.error("upsert_items: " + str(err))

            if on_error:
                on_error(err)

        pass

    def clear_items_source(self, ext_company_id, on_success=lambda x: x, on_error=lambda x: x):
        try:
            fields = {
                'int_id': None,
                'int_name': None
            }
            where = {
                'ext_company_id': ext_company_id
            }
            self.update_rows('items', fields, where)

            if on_success:
                on_success(True)

        except sqlite3.DatabaseError as err:
            logging.error("upsert_items_from_source: " + str(err))

            if on_error:
                on_error(err)

        pass

    def update_items_from_source(self, ext_company_id, array, on_success=lambda x: x, on_error=lambda x: x):
        try:

            for item in array:
                fields = {
                    'int_id': item.int_id,
                    'int_name': item.int_name
                }
                where = {
                    'ext_id_internal': item.int_id,
                    'ext_company_id': ext_company_id
                }
                self.update_row('items', 'ext_id_internal', fields, where)

            if on_success:
                on_success(True)

        except sqlite3.DatabaseError as err:
            logging.error("upsert_items_from_source: " + str(err))

            if on_error:
                on_error(err)

        pass

    def get_items(self, company_id, exist_ext_id_internal=False, include_iip=False):
        if not company_id:
            return False
        if exist_ext_id_internal:
            return self.execute_select("SELECT * FROM items "
                                       "WHERE ext_company_id=? AND ext_id_internal IS NOT NULL "
                                       "ORDER BY int_id ASC", [company_id])
        elif include_iip:
            items_raw = self.execute_select("SELECT i.*, iip.*, p.ext_id as point_ext_id, "
                                            "i.ext_id as item_ext_id, iip.ext_id as iip_ext_id FROM items i "
                                            "LEFT OUTER JOIN item_in_points iip ON i.ext_id_internal = iip.item_id_internal "
                                            "LEFT OUTER JOIN points p ON iip.point_id_internal = p.ext_id_internal "
                                            "WHERE i.ext_company_id=? AND i.ext_id_internal IS NOT NULL ", [company_id])
            items = []

            for item_raw in items_raw:
                item = next(filter(lambda x:
                                   x.item_id_internal == item_raw.item_id_internal, items), None)

                iip = obj()
                for name in ['item_id_internal', 'point_id_internal', 'ext_id', 'ext_count', 'ext_price',
                             'int_price', 'int_count', 'point_ext_id', 'item_ext_id', 'iip_ext_id']:
                    iip.__dict__[name] = item_raw.__dict__[name]

                if not item:
                    item = item_raw
                    item.iip = []
                    items.append(item)

                item.iip.append(iip)

            return items
        else:
            return self.execute_select("SELECT * FROM items WHERE ext_company_id=? ORDER BY int_id ASC", [company_id])
        pass

    # POINTS

    def upsert_points(self, array, on_success=lambda x: x, on_error=lambda x: x):
        try:

            for item in array:
                fields = {
                    'ext_id': item.id,
                    'ext_company_id': item.companyId,
                    'ext_name': item.name,
                    'ext_id_internal': item.idInternal
                }
                self.upsert_row('points', 'ext_id', fields)

            if on_success:
                on_success(True)

        except sqlite3.DatabaseError as err:
            logging.error("upsert_points: " + str(err))

            if on_error:
                on_error(err)

        pass

    def update_points(self, array, on_success=lambda x: x, on_error=lambda x: x):
        try:

            for item in array:
                fields = {
                    'ext_id_internal': item.int_id,
                    'int_id': item.int_id,
                    'int_name': item.int_name
                }
                self.update_row('points', 'ext_id_internal', fields)

            if on_success:
                on_success(True)

        except sqlite3.DatabaseError as err:
            logging.error("update_points_from_source: " + str(err))

            if on_error:
                on_error(err)

        pass

    def get_points(self, company_id, exist_ext_id_internal=False):
        if not company_id:
            return False
        if exist_ext_id_internal:
            return self.execute_select("SELECT * FROM points "
                                       "WHERE ext_company_id=? AND ext_id_internal IS NOT NULL "
                                       "ORDER BY int_id ASC", [company_id])
        else:
            return self.execute_select("SELECT * FROM points WHERE ext_company_id=? ORDER BY int_id ASC", [company_id])
        pass

    # ITEM IN POINTS

    def upsert_iip(self, array, on_success=lambda x: x, on_error=lambda x: x):
        try:

            for item in array:
                fields = {
                    'item_id_internal': item.item_id_internal,
                    'point_id_internal': item.point_id_internal,
                    'int_price': item.int_price,
                    'int_count': item.int_count
                }
                where = {
                    'item_id_internal': item.item_id_internal,
                    'point_id_internal': item.point_id_internal,
                }
                self.upsert_row('item_in_points', 'item_id_internal', fields, where)

            if on_success:
                on_success(True)

        except sqlite3.DatabaseError as err:
            logging.error("upsert_iip: " + str(err))

            if on_error:
                on_error(err)

        pass

    def update_iip(self, array, on_success=lambda x: x, on_error=lambda x: x):
        try:

            for item in array:
                fields = {
                    'item_id_internal': item.item_id_internal,
                    'point_id_internal': item.point_id_internal,
                    'ext_id': item.ext_id,
                    'ext_price': item.ext_price,
                    'ext_count': item.ext_count
                }
                where = {
                    'item_id_internal': item.item_id_internal,
                    'point_id_internal': item.point_id_internal,
                }
                self.update_row('item_in_points', 'item_id_internal', fields, where)

            if on_success:
                on_success(True)

        except sqlite3.DatabaseError as err:
            logging.error("update_iip: " + str(err))

            if on_error:
                on_error(err)

        pass

    # NUMERICAL INDICATORS OF THE COMPANY
    def get_company_counts(self, company_id):
        counts = obj()

        if not company_id:
            return counts

        counts.items = self.execute_count("SELECT count(*) FROM items "
                                          "WHERE ext_company_id=?", [company_id])

        counts.items_compared = self.execute_count("SELECT count(*) FROM items "
                                                   "WHERE ext_company_id=? and int_id IS NOT NULL", [company_id])

        counts.points = self.execute_count("SELECT count(*) FROM points "
                                           "WHERE ext_company_id=?", [company_id])

        counts.points_compared = self.execute_count("SELECT count(*) FROM points "
                                                    "WHERE ext_company_id=? and int_id IS NOT NULL", [company_id])

        counts.price = self.execute_count("""
SELECT count(*) FROM item_in_points WHERE item_id_internal IN (
    SELECT int_id FROM items WHERE ext_company_id=? AND int_id IS NOT NULL
)
""", [company_id])

        counts.price_founded = self.execute_count("""
SELECT count(*) FROM item_in_points WHERE item_id_internal IN (
    SELECT int_id FROM items WHERE ext_company_id=? AND int_id IS NOT NULL
) AND int_price IS NOT NULL
""", [company_id])

        counts.count = self.execute_count("""
SELECT count(*) FROM item_in_points WHERE item_id_internal IN (
    SELECT int_id FROM items WHERE ext_company_id=? AND int_id IS NOT NULL
)
""", [company_id])

        counts.count_founded = self.execute_count("""
SELECT count(*) FROM item_in_points WHERE item_id_internal IN (
    SELECT int_id FROM items WHERE ext_company_id=? AND int_id IS NOT NULL
) AND int_count IS NOT NULL
""", [company_id])

        return counts

    def change_to_autoload(self, add=None, remove=None):
        if add:
            self.settings_autoload.setValue("Tarder", self.get_autoload_value())
        elif remove:
            self.settings_autoload.remove("Tarder")

    def is_in_autoload(self):
        value = self.settings_autoload.value("Tarder")
        return value is not None and value == self.get_autoload_value()

    def get_autoload_value(self):
        return QCoreApplication.applicationFilePath().replace('/', '\\') + ' -hide'
