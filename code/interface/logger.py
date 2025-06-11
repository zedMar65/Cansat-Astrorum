import json

class Logger:
    def __init__(self, handlers: list["LoggerClass"]):
        self.handlers = handlers

    def _log(self, message, level):
        payload = json.dumps({
            "id": Vars.LOG_ID,
            "time": Vars.CURRENT_TIME,
            "status": level,
            "message": message
        })
        for h in self.handlers:
            try:
                h.send(payload)
            except Exception as e:
                ErrorHandler.async_error(e)
                continue

    def info(self, msg):
        self._log(msg, Consts.INFO)

    def error(self, msg):
        self._log(msg, Consts.ERROR)

    def data(self, data):
        self._log(data, Consts.DATA)