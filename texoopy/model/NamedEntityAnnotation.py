import copy
import json

from .Annotation import Annotation


class NamedEntityAnnotation(Annotation):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refId: str = kwargs.get('refId')
        # it is not safe to aggregate refId to Annotation (see original data model)


    @classmethod
    def from_json(cls, json_data: dict):
        json_data = copy.deepcopy(json_data)
        return cls(**json_data)

    def to_json(self):
        return json.dumps(self.to_texoo_dict(), default=lambda o: o.to_texoo_dict())

    def to_texoo_dict(self) -> dict:
        content = super().to_texoo_dict()
        content['class'] = 'NamedEntityAnnotation'
        content['candidates'] = []
        return content