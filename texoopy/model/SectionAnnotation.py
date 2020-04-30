import copy
import json

from .Annotation import Annotation


class SectionAnnotation(Annotation):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sectionHeading: str = kwargs.get('sectionHeading')
        self.sectionLabel: str = kwargs.get('sectionLabel')
        self.label: str = kwargs.get('label')

    @classmethod
    def from_json(cls, json_data: dict):
        json_data = copy.deepcopy(json_data)
        return cls(**json_data)

    def to_json(self):
        return json.dumps(self.to_texoo_dict(), default=lambda o: o.to_texoo_dict())

    def to_texoo_dict(self) -> dict:
        content = super().to_texoo_dict()
        content['class'] = 'SectionAnnotation'
        if content['text'] is None:
            content = dict(content)
            del content['text']
        return content
