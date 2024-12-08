import os
from testbook import testbook


@testbook('reuseGenerateData.ipynb', execute=True)
def test_reuseGenerateData(tb):
    HealthData = tb.get("HealthData")
    environment = "test"
    outputdir = "tests/data"
    filename = f"{outputdir}/health_data_{environment}.parquet"
    os.makedirs(outputdir, exist_ok=True)

    if os.path.exists(filename):
        os.remove(filename)
    print(f"Running notebook with environment {environment}")

    healthData = HealthData(environment, outputdir)  # type: ignore
    healthData.generate_data()
    assert os.path.exists(filename), f"{filename} has not been created"
    if os.path.exists(filename):
        os.remove(filename)
