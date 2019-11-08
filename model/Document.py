from model.Annotation import Annotation
from model.Span import Span


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

        if json_data.get('class') != 'Document':
            raise NotATeXooDocumentException('')

        annotations = []
        for json_data_annotation in json_data.get('annotations'):
            annotations.append(Annotation.from_json(json_data_annotation))
        json_data['annotations'] = annotations

        if do_sentence_splitting:
            pass  # TODO add sentence splitting

        return cls(**json_data)

    def to_json(self):
        pass  # TODO implement me after there is a test for me


class NotATeXooDocumentException(Exception):
    pass
