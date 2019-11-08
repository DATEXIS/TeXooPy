from model.Span import Span


class Token(Span):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # TODO IMPLEMENT ME

    @classmethod
    def from_json(cls, json_data: dict):
        return cls(**json_data)  # TODO IMPLEMENT ME

    def to_json(self):
        pass  # TODO implement me after there is a test for me
