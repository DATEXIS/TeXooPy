from model.Span import Span


class Annotation(Span):
    def __init__(self):
        super().__init__()
        # TODO IMPLEMENT ME

    @classmethod
    def from_json(cls, json_data: dict):
        pass  # TODO IMPLEMENT ME

    def to_json(self):
        pass  # TODO implement me after there is a test for me
