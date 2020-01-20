import copy
import json

from .Document import Document


class Dataset:
    def __init__(self, **kwargs):
        self.name: str = kwargs.get('name')
        self.language: str = kwargs.get('language')
        self.documents: list = []
        self.queries: list = []

    @classmethod
    def from_json(cls, json_data: dict):
        json_data = copy.deepcopy(json_data)
        dataset = cls(**json_data)
        for doc_json_data in json_data.get('documents', []):
            dataset.documents.append(Document.from_json(doc_json_data))
        return dataset

    def to_json(self):
        return json.dumps(self.to_texoo_dict(), default=lambda o: o.to_texoo_dict())

    def __str__(self):
        return "Dataset {}, name: {}, language: {}, # documents: {}".format(
            self.__hash__(),
            self.name,
            self.language,
            len(self.documents)
        )
    
    def to_texoo_dict(self):
        return copy.deepcopy(self.__dict__)