from kedro.pipeline import Pipeline, node
from .nodes import load_csv_from_bucket


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                func=load_csv_from_bucket,
                inputs=["params:project", "params:bucket_path"],
                outputs="raw_data",
                name="load_data_from_gcs",
            ),
        ]
    )
