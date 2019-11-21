from texoopy.model.Annotation import Annotation


class NamedEntityAnnotation(Annotation):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.refId: str = kwargs.get('refId')

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)

    def to_json(self):
        pass  # TODO implement me after there is a test for me
