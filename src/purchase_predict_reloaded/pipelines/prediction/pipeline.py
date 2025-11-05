from kedro.pipeline import Pipeline, node
from .nodes import load_model, predict


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=load_model,
                inputs="params:model_path",
                outputs="model",
                name="load_model_node",
            ),
            node(
                func=predict,
                inputs=["model", "X_test"],
                outputs="predictions",
                name="prediction_node",
            ),
        ]
    )
