from model.Span import Span


class Document(Span):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.id: str = kwargs.get('id')
        self.title: str = kwargs.get('title')
        self.language: str = kwargs.get('language')
        self.type: str = kwargs.get('language')
        self.sentences: list = []
        self.annotations: list = []

    @classmethod
    def from_json(cls, json_data: dict, sentence_split=False):
        if json_data.get('class') != 'Document':
            raise NotATeXooDocumentException('')
        # TODO iterate over annotations and insert
        # TODO maybe perform sentence splitting
        return cls(**json_data)


class NotATeXooDocumentException(Exception):
    pass
