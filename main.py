from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import (DataIngestionTrainingPipeline)
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTrainingPipeline
from cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        data_ingestion = DataIngestionTrainingPipeline()
        data_ingestion.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Prepare Base Model Stage"

try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        prepare_base_model = PrepareBaseModelTrainingPipeline()
        prepare_base_model.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Training Stage"

try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        training = ModelTrainingPipeline()
        training.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Evaluation Stage"

try:
        logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<")
        evaluation = EvaluationPipeline()
        evaluation.main()
        logger.info(f">>>>>>> Stage {STAGE_NAME} Completed <<<<<<<")
except Exception as e:
        logger.exception(e)
        raise e