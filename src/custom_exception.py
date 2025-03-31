import traceback
import sys
from types import ModuleType
from typing import Union, Optional, Type


class CustomException(Exception):
    def __init__(
        self, 
        error_message: str, 
        error_detail: Union[Exception, ModuleType, Type[Exception]]
    ):
        super().__init__(error_message)
        self.error_message = self.get_detailed_error_message(error_message, error_detail)
        self.traceback = traceback.format_exc()

    @staticmethod
    def get_detailed_error_message(
        error_message: str, 
        error_detail: Union[Exception, ModuleType, Type[Exception]]
    ) -> str:
        exc_type, exc_value, exc_tb = sys.exc_info() if isinstance(error_detail, (ModuleType, type)) else (
            type(error_detail), error_detail, error_detail.__traceback__
        )
        
        if exc_tb is None:
            return error_message
            
        file_name = exc_tb.tb_frame.f_code.co_filename
        line_number = exc_tb.tb_lineno
        return f"{error_message} (File: {file_name}, Line: {line_number})"
    
    def __str__(self) -> str:
        return self.error_message