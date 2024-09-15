import sys

def error_message_detail(error, error_detail: sys):
    print(error_detail)
    print(error)
    _, _, exc_tb = error_detail.exc_info()
    print(exc_tb)
    file_name = exc_tb.tb_frame.f_code.co_filename  # Corrected line
    print(exc_tb.tb_frame.f_code.co_filename)
    error_message = "Error occurred in python script name {0} line number[{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_details
        )

    def __str__(self):
        return self.error_message



try:
  a=1/0
except Exception as e:
   print(CustomException(str(e),sys))

print("Hello!!")