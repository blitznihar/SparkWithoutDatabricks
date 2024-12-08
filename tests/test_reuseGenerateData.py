import os
from testbook import testbook


@testbook("reuseGenerateData.ipynb", execute=True)
def test_reuseGenerateData(tb):
    HealthData = tb.get("HealthData")
    environment = "test"
    outdir = "tests/data"
    filename = f"{outdir}/health_data_{environment}.parquet"
    os.makedirs(outdir, exist_ok=True)

    if os.path.exists(filename):
        os.remove(filename)
    print(f"Running notebook with environment {environment}")

    healthData = HealthData(environment, outdir)  # type: ignore
    healthData.generate_data()
    assert os.path.exists(filename), f"{filename} has not been created"
    if os.path.exists(filename):
        os.remove(filename)
