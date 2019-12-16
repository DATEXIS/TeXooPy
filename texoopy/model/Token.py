import json

from texoopy.model.Span import Span


class Token(Span):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # TODO IMPLEMENT ME

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)  # TODO IMPLEMENT ME

    def to_json(self):
        return json.dumps(self.to_texoo_dict())
        # TODO implement a test for me

    def to_texoo_dict(self):
        return super().to_texoo_dict()