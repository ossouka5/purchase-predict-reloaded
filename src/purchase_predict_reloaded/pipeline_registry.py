"""Project pipelines."""

from typing import Dict
from kedro.pipeline import Pipeline

from purchase_predict_reloaded.pipelines import processing
from purchase_predict_reloaded.pipelines.training import pipeline as training_pipeline
from purchase_predict_reloaded.pipelines import loading as loading_pipeline
from purchase_predict_reloaded.pipelines.prediction import (
    pipeline as prediction_pipeline,
)


def register_pipelines() -> Dict[str, Pipeline]:
    processing_pipe = processing.create_pipeline()
    training_pipe = training_pipeline.create_pipeline()
    loading_pipe = loading_pipeline.create_pipeline()
    prediction_pipe = prediction_pipeline.create_pipeline()

    full_pipeline = processing_pipe + training_pipe

    return {
        "loading": loading_pipe,
        "training": training_pipe,
        "processing": processing_pipe,
        "prediction": prediction_pipe,
        "full": full_pipeline,
        "__default__": processing_pipe,
    }
