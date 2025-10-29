
"""Project pipelines."""

from typing import Dict
from kedro.pipeline import Pipeline
from purchase_predict_reloaded.pipelines import processing


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns
    -------
    Dict[str, Pipeline]
        A dictionary with pipeline names as keys and Pipeline objects as values.
    """
    processing_pipeline = processing.create_pipeline()
    
    return {
        "processing": processing_pipeline,
        "__default__": processing_pipeline,
    }
