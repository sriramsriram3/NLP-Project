import os 
from pathlib import Path

folder_list=[
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transfer.py',
    'src/components/model_trainer.py',
    'src/components/model_evaluate.py',
    'src/pipelines/__init__.py',
    'src/pipelines/training_pipeline.py',
    'src/pipelines/prediction_pipeline.py',
    'src/logging/__init__.py',
    'src/logging/logger.py',
    'src/exception/__init__.py',
    'src/exceptions/exception.py',
    'setup.py',
    'setup.cfg',
    'requirements.txt',
    'dev_requirements.txt',
    'tests/__init__.py',
    'tests/unit_test.py',
    'tests/integrate_test.py',
    

]

for folders in folder_list:
    folders=Path(folders)
    folder,file=os.path.split(folders)
    if folder :
        os.makedirs(folder,exist_ok=True)
    if not os.path.exists(file) or (os.path.getsize(file) == 0):
        with open(folders,'w') as f:
            pass
