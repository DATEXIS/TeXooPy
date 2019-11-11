from texoopy.model.Span import Span


class Sentence(Span):
    def __init__(self, **kwargs):
        # TODO IMPLEMENT ME
        super().__init__(**kwargs)

    @classmethod
    def from_json(cls, json_data: dict, do_tokenization=False):
        if do_tokenization:
            pass  # TODO implement me (later)

        return cls(**json_data)  # TODO IMPLEMENT ME

    def to_json(self):
        pass  # TODO implement me after there is a test for me
