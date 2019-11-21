from texoopy.model.Span import Span


class Annotation(Span):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source: str = kwargs.get('source')
        self.text: str = kwargs.get('text')
        self.begin: int = kwargs.get('begin')
        self.end: int = kwargs.get('end')
        self.confidence: float = kwargs.get('confidence')

    @classmethod
    def from_json(cls, json_data: dict):
        from texoopy.model.MentionAnnotation import MentionAnnotation
        from texoopy.model.NamedEntityAnnotation import NamedEntityAnnotation
        if json_data['class'] == 'MentionAnnotation':
            return MentionAnnotation.from_json(json_data)
        elif json_data['class'] == 'NamedEntityAnnotation':
            return NamedEntityAnnotation.from_json(json_data)
        else:
            raise (Exception("Annotation type not supported!"))

    def to_json(self):
        pass  # TODO implement me after there is a test for me
