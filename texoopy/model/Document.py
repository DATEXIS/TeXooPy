import copy
import json

from texoopy.model.Annotation import Annotation
from texoopy.model.Span import Span


class Document(Span):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id: str = kwargs.get('id')
        self.title: str = kwargs.get('title')
        self.language: str = kwargs.get('language')
        self.type: str = kwargs.get('type')
        self.annotations: list = kwargs.get('annotations', [])
        sentences: list = kwargs.get('sentences', [])

    @classmethod
    def from_json(cls, json_data: dict, do_sentence_splitting=False):
        json_data = copy.deepcopy(json_data)
        if json_data.get('class') != 'Document':
            raise NotATeXooDocumentException('Supplied JSON is not a valid TeXoo document.')

        annotations = []
        for json_data_annotation in json_data.get('annotations'):
            annotations.append(Annotation.from_json(json_data_annotation))
        json_data['annotations'] = annotations

        if do_sentence_splitting:
            raise NotImplementedError("Sentence splitting is not implemented yet.")  # TODO add sentence splitting

        return cls(**json_data)

    def to_json(self):
        content = self.to_texoo_dict()
        return json.dumps(content, default=lambda o: o.to_texoo_dict())

    def to_texoo_dict(self) -> dict:
        content = super().to_texoo_dict()
        content['class'] = 'Document'
        return content


class NotATeXooDocumentException(Exception):
    pass
