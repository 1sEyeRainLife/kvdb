import json


class Database(object):

    _data_path = "./data.txt"
    _data = {}

    def __init__(self):
        self.fd_r = open(self._data_path, "r", encoding="UTF-8")
        self._data = json.loads(self.fd_r.read())
        self.fd_w = open(self._data_path, "w", encoding="UTF-8")

    def close(self):
        self.fd_r.close()
        self.fd_w.close()

    def commit(self):
        self.fd_w.write(json.dumps(self._data, ensure_ascii=False))
        self.fd_w.flush()

    def get(self, key, *args, **kwargs):
        return self._data.get(key)

    def set(self, key, value, commit=False):
        self._data[key] = value
        if commit:
            self.commit()