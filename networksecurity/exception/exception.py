import sys
from networksecurity.logging import logger #importing file logger.py

class NetworkSecurityException(Exception):
    def __init__(self,error_message,error_details:sys):#excepting error msg from system in sys parameter 
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno # in which line no  eroro is there 
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
    
    def __str__(self):  #display error msg
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        
# if __name__=='__main__':
#     try:
#         logger.logging.info("Enter the try block")
#         a=1/0  # to face error
#         print("This will not be printed",a) #as exception is handled 
#     except Exception as e:
#            raise NetworkSecurityException(e,sys) # for catchig exception