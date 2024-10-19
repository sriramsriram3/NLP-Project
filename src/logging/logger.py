
import os
from datetime import datetime
import logging

log_dir="logs"
os.makedirs(log_dir,exist_ok=True)

log_path=os.path.join(log_dir,f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.logs")

logging.basicConfig(filename=log_path,
                    level=logging.INFO,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s")
