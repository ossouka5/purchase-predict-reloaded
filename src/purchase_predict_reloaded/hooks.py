"""Project hooks for Kedro."""

from typing import Any, Dict, Iterable, Optional
from kedro.config import ConfigLoader
from kedro.framework.hooks import hook_impl
from kedro.io import DataCatalog
from kedro.pipeline import Pipeline
from kedro.versioning import Journal

from purchase_predict_reloaded.pipelines import processing
from purchase_predict_reloaded.pipelines.training import pipeline as training_pipeline
from purchase_predict_reloaded.pipelines.loading import pipeline as loading_pipeline


class ProjectHooks:
    """Custom Kedro hooks for pipeline registration and other lifecycle events."""

    @hook_impl
    def register_pipelines(self) -> Dict[str, Pipeline]:
        """Register the project's pipelines."""
        p_processing = processing.create_pipeline()
        p_training = training_pipeline.create_pipeline()
        p_loading = loading_pipeline.create_pipeline()

        # Ajout du pipeline global
        p_global = p_loading + p_processing + p_training

        return {
            "loading": p_loading,
            "processing": p_processing,
            "training": p_training,
            "global": p_global,  # ✅ IMPORTANT : il faut ce nom exact
            "__default__": p_processing,
        }

    @hook_impl
    def register_config_loader(self, conf_paths: Iterable[str]) -> ConfigLoader:
        """Register the configuration loader for Kedro."""
        return ConfigLoader(conf_paths)

    @hook_impl
    def register_catalog(
        self,
        catalog: Dict[str, Any],
        credentials: Dict[str, Any],
        load_versions: Optional[Dict[str, str]],
        save_version: str,
        journal: Journal,
    ) -> DataCatalog:
        """Register the project's data catalog."""
        return DataCatalog.from_config(
            catalog,
            credentials,
            load_versions,
            save_version,
            journal,
        )
