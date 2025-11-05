from kedro.runner import SequentialRunner

from purchase_predict_reloaded.pipelines.loading.pipeline import create_pipeline


def test_pipeline(catalog_test):
    runner = SequentialRunner()
    pipeline = create_pipeline()
    pipeline_output = runner.run(pipeline, catalog_test)
    assert "primary" in pipeline_output
