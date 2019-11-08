from model.Annotation import Annotation


class NamedEntityAnnotation(Annotation):
    def __init__(self, **kwargs):
        super().__init__()
        # TODO IMPLEMENT ME

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)  # TODO IMPLEMENT ME
