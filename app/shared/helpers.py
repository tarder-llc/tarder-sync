import json
import os
import re
from datetime import datetime
from pathlib import Path

import dateparser as dateparser
import pytz
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QVBoxLayout

DATE_FORMAT_PRETTY = '%d-%m-%Y %H:%M:%S'


class Switch:
    def __init__(self, value):
        self.value = value

    def case(self, value, code):
        if self.value == value:
            code()
        return self


# Switch(index) \
#     .case(0, lambda: value_12('params')) \
#     .case(1, lambda: value_13('13 params')) \

class obj(object):
    def __init__(self, dict_={}):
        self.__dict__.update(dict_)

    def __getattr__(self, item):
        return None

    def __getvalue__(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        else:
            return None


class MyEncoder(json.JSONEncoder):
    def default(self, object_in):
        if isinstance(object_in, obj):
            return object_in.__dict__
        return json.JSONEncoder.default(self, object_in)


class Helpers:
    @staticmethod
    def get_ui(file):
        file = QFile(Helpers.adjust_filename(Path(file).stem, file) + '.ui')
        if not file.exists():
            print('file not exist')
            return
        if not file.open(QFile.ReadOnly):
            return
        file.open(QFile.ReadOnly)
        loader = QUiLoader()
        widget = loader.load(file)
        file.close()
        return widget

    @staticmethod
    def set_ui(parent, file):
        parent.ui = Helpers.get_ui(file)  # just load ui file
        layout = QVBoxLayout(parent)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(parent.ui)

    @staticmethod
    def adjust_filename(filename, orig_mod_filename):
        dir_path = os.path.dirname(os.path.abspath(orig_mod_filename))
        return os.path.join(dir_path, filename)

    @staticmethod
    def add_to_log(text_widget, text, isError=False):
        text_widget.setPlainText(text_widget.toPlainText() + str(text) + '\n')
        text_widget.ensureCursorVisible()
        pass

    @staticmethod
    def dict2obj(dict):
        return json.loads(json.dumps(dict), object_hook=obj)

    @staticmethod
    def to_obj(value):
        if isinstance(value, list):
            array = []
            for item in value:
                array.append(Helpers.dict2obj(item))
            return array
        else:
            return Helpers.dict2obj(value)
        pass

    @staticmethod
    def convert_number(value, to_float, return_pretty=False):
        if value is None:
            return None
        if to_float:
            result = float(value / 100)
            if return_pretty:
                result = f'{result:n}'
            return result
        else:
            return int(value * 100)

    @staticmethod
    def get_separator(value1, value2):
        result = value1
        # if value2:
        #     result += "___" + value2
        return result

    @staticmethod
    def now():
        return datetime.now(tz=pytz.utc)

    @staticmethod
    def parse_date(string):
        if string is None:
            return None

        date = dateparser.parse(string)

        return date

    @staticmethod
    def get_date_str():
        date = str(Helpers.now())
        return date

    @staticmethod
    def get_pretty_date(string_or_date):
        if isinstance(string_or_date, datetime):
            date = string_or_date
        else:
            date = dateparser.parse(string_or_date)
        date = date.astimezone()
        date = date.strftime(DATE_FORMAT_PRETTY)
        date = str(date)
        return date

    @staticmethod
    def copy_fields(obj_from, obj_to=obj(), fields=None):
        if fields is None:
            fields = []

        changed = False
        for field in fields:
            if obj_to.__dict__[field] != obj_from.__dict__[field]:
                obj_to.__dict__[field] = obj_from.__dict__[field]
                changed = True

        return changed

    @staticmethod
    def remove_from_array(array, value):
        if value in array:
            try:
                array.remove(value)
            except Exception as e:
                print(str(e))
                return False
            return True
        return True

    @staticmethod
    def parse_float(value):
        if value is None or value != value:  # or is NaN
            return None

        if isinstance(value, float):
            return value

        try:
            if isinstance(value, str):
                value = value.replace(',', '.')
                value = re.sub('[^.\-\d]', '', value)
            number = float(value)
            return number
        except Exception:
            return None

        pass

    @staticmethod
    def parse_int(value):
        if value is None:
            return None

        if isinstance(value, int):
            return value

        try:
            if isinstance(value, str):
                value = value.replace(',', '.')
                value = re.sub('[^.\-\d]', '', value)
            number = float(value)
            return int(number + 0.5)
        except Exception:
            return None

        pass
