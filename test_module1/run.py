# test_module_1/run.py
import numpy as np
from typing import Dict
from test_module1.schemas import InputSchema, OutputSchema
from naptha_sdk.schemas import AgentRunInput

def run(module_run: Dict, *args, **kwargs):
    module_run = AgentRunInput(**module_run)
    module_run.inputs = InputSchema(**module_run.inputs)    
    return OutputSchema(
        numpy_version=np.__version__,
        message=f"Module 1 says: {module_run.inputs.message}. Using numpy {np.__version__}"
    ).model_dump()