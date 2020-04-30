import copy
import json

from .Span import Span


class Annotation(Span):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.source: str = kwargs.get('source')
        self.text: str = kwargs.get('text')
        self.begin: int = kwargs.get('begin')
        self.confidence: float = kwargs.get('confidence')

    @classmethod
    def from_json(cls, json_data: dict):
        json_data = copy.deepcopy(json_data)
        from texoopy.model.MentionAnnotation import MentionAnnotation
        from texoopy.model.NamedEntityAnnotation import NamedEntityAnnotation
        from texoopy.model.SectionAnnotation import SectionAnnotation
        if json_data['class'] == 'MentionAnnotation':
            return MentionAnnotation.from_json(json_data)
        elif json_data['class'] == 'NamedEntityAnnotation':
            return NamedEntityAnnotation.from_json(json_data)
        elif json_data['class'] == 'SectionAnnotation':
            return SectionAnnotation.from_json(json_data)
        else:
            raise (Exception("Annotation type not supported!"))

    def to_json(self):
        return json.dumps(self.to_texoo_dict(), default=lambda o: o.to_texoo_dict())

    def to_texoo_dict(self) -> dict:
        content = super().to_texoo_dict()
        return content
