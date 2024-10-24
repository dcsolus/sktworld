import logging, os
from typing import Union

def MyLogger(setLevel:str='info', to_file:Union[str,None]='my.log') -> logging.Logger:
    
    # 로그 생성
    logger = logging.getLogger()
    
    formatter = logging.Formatter('%(asctime)s - %(module)s> %(funcName)s> %(lineno)s - %(levelname)s - %(message)s')

    # 로그의 출력 기준 설정
    match setLevel.upper():
        case 'INFO': logger.setLevel(logging.INFO)
        case 'DEBUG': logger.setLevel(logging.DEBUG)
        case 'ERROR': logger.setLevel(logging.ERROR)
        case 'WARN' | 'WARNING': logger.setLevel(logging.WARN)
            
    # log 출력
    if not logger.hasHandlers():
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # log를 파일에 출력
        if to_file:
            file_handler = logging.FileHandler(to_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
    
    return logger

def clean_log():
    log_file = 'my.log'
    if os.path.exists(log_file):
        os.remove(log_file)
        
if __name__=='__main__':
    clean_log()