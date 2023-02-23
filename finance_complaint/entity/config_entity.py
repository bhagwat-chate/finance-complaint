from collections import namedtuple

TrainingPipelineConfig = namedtuple("PipelineConfig", ["pipeline_name", "artifact_dir"])

DataIngestionConfig = namedtuple("DataIngestionConfig", ["from_date", 
                                                         "to_date", 
                                                         "data_ingestion_dir", 
                                                         "file_name", 
                                                         "feature_store_dir", 
                                                         "metadata_file_path", 
                                                         "datasource_url"])
