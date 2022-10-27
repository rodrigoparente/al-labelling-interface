# python imports
from typing import Optional

# third-party imports
from pydantic import BaseModel, Field
from bson import ObjectId

# local imports
from .utils import PyObjectId


class InstanceModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    dataset_name: Optional[str]
    labels: list = []
    columns: list = []
    entries: list = []

    class Settings:
        name = "instance"

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "dataset_name": "iris flowers dataset",
                "labels": ["iris-setosa", "iris-versicolour", "iris-virginica"],
                "columns": ["sepal-length", "sepal-width", "petal-length", "petal-width"],
                "entries": [
                    {"sepal-length": 4.9, "sepal-width": 3.0, "petal-length": 1.4, "petal-width": 0.2},
                    {"sepal-length": 4.7, "sepal-width": 3.2, "petal-length": 1.3, "petal-width": 0.2},
                    {"sepal-length": 5.0, "sepal-width": 3.6, "petal-length": 1.4, "petal-width": 0.2},
                ]
            }
        }


class ActiveLearningModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    model_path: str
    labels: list = []
    labelled_instances: list = []
    unlabelled_instances: list = []

    class Settings:
        name = "active_learning"

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "model_path": "/models/alli_1_model.pickle",
                "labels": [
                    "iris-setosa"
                ],
                "labelled_instances": [
                    {"sepal-length": 4.9, "sepal-width": 3.0, "petal-length": 1.4, "petal-width": 0.2}
                ],
                "unlabelled_instances": [
                    {"sepal-length": 4.7, "sepal-width": 3.2, "petal-length": 1.3, "petal-width": 0.2},
                    {"sepal-length": 5.0, "sepal-width": 3.6, "petal-length": 1.4, "petal-width": 0.2},
                ]
            }
        }
