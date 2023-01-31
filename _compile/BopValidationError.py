class BopValidationError(Exception):

    def __init__(self, err_type: str, error_num: str, msg: str):
        self.msg = msg
        self.error_type = err_type
        self.error_num = error_num

    def __str__(self):
        return str(self.error_type) + " " + str(self.error_num) + ":\n" + str(self.msg)
