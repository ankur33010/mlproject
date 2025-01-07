import sys
import logging

def error_message_detail(error,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"Error Occcured in python script name {file_name} line No. {exc_tb.tb_lineno} error message {str(error)}"
    error_message


class CustomException(Exception):  # here we have overriding the Exception function 
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_details=error_details)

    def __str__(self):  # this gonna come when you would you do the print 
        return self.error_message
    


# if __name__=="__main__":

#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divided by Zero")
#         raise CustomException(e,sys)
