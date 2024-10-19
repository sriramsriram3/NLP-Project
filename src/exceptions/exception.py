import sys

class custom_exception(Exception):
    def __init__(self,error_message,error_details: sys):
        self.error_message=error_message
        _,_,extb=error_details.exc_info()
        self.line_no=extb.tb_lineno
        self.filename=extb.tb_frame.f_code.co_filename


    def __str__(self):
        return "Error occured in file name [{0}]  line number : [{1}] error message: [{2}] ".format(self.filename,self.error_message,self.line_no)
    


