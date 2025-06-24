import os 
from pathlib import Path
import logging
import pandas as pd
from typing import Optional, Union
from error_messages import DataReadingErrorMessages as em , SUPPORTED_FILE_EXTENSIONS

logging.basicConfig (

    level = logging.INFO,format = '%(asctime)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

class DataLoader:
   

    def load_data(self, file_path: Union[str, Path]) -> Optional[ pd.DataFrame]:
        
        if not isinstance(file_path, (str, Path)):
            logger.error(
                em.INVALID_FILE_PATH_.value.format(type=type(file_path))
            )
            raise TypeError(em.INVALID_FILE_PATH_.value.format(type=type(file_path)))
        
        if not Path(file_path).exists():
            logger.error(em.FILE_NOT_FOUND_.value.format(file_path=file_path))
            raise FileNotFoundError(em.FILE_NOT_FOUND_.value.format(file_path=file_path))
        
        ext =  Path(file_path).suffix
        
        if ext not in SUPPORTED_FILE_EXTENSIONS:
            logger.error(em.EXT_NOT_SUPPORTED.value.format(ext=ext, supported_extensions=SUPPORTED_FILE_EXTENSIONS))
            raise ValueError(em.EXT_NOT_SUPPORTED.value.format(ext=ext, supported_extensions=SUPPORTED_FILE_EXTENSIONS))


        data = pd.read_csv(file_path)
        if data.empty:
            logger.warning(em.EMPTY_DATA.value)
            raise ValueError(em.EMPTY_DATA.value)

    
