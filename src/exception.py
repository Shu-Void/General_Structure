import sys

# This will generate a message whenever an error has occured
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    # The results are exception type, exception value and traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_no = exc_tb.tb_lineno
    msg = str(error)
    
    error_message = 'Error occured in python script name [{0}] line number [{1}] error message [{2}]'.format(
        file_name,line_no,msg
    )
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        # Here super inherits the initialisation function from the parent class i.e. Exception class

        self.error_message = error_message_detail(error_message , error_detail=error_detail)
    
    def __str__(self):
        # Return the error message whenever asked to print
        return self.error_message

