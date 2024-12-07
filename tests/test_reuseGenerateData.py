import os
import pytest
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import pandas as pd
from io import StringIO
from testbook import testbook

# from reuseGenerateData import HealthData
# os.path.exists("reuseGenerateData.ipynb")
@testbook('reuseGenerateData.ipynb', execute=True)
def test_reuseGenerateData(tb):
        HealthData = tb.get("HealthData")
    #with open("reuseGenerateData.ipynb") as f:
        #nb = nbformat.read(f, as_version=4)
        environment = "test"
        outputdir = "tests/data"
        filename = f"{outputdir}/health_data_{environment}.parquet"
        # os.makedirs(outputdir, exist_ok=True)

        if os.path.exists(filename):
            os.remove(filename)

        print(f"Running notebook with environment {environment}")

        healthData = HealthData(environment, outputdir)  # type: ignore
        healthData.generate_data()
        assert os.path.exists(filename), f"{filename} has not been created"
        if os.path.exists(filename):
            os.remove(filename)