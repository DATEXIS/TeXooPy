from texoopy.model.Document import Document


class Dataset:
    def __init__(self, **kwargs):
        self.name: str = kwargs.get('name')
        self.language: str = kwargs.get('language')
        self.documents: list = []

    @classmethod
    def from_json(cls, json_data: dict):
        dataset = cls(**json_data)
        for doc_json_data in json_data.get('documents', []):
            dataset.documents.append(Document.from_json(doc_json_data))
        return dataset

    def to_json(self):
        pass  # TODO implement me after there is a test for me

    def __str__(self):
        return "Dataset {}, name: {}, language: {}, # documents: {}".format(
            self.__hash__(),
            self.name,
            self.language,
            len(self.documents)
        )
