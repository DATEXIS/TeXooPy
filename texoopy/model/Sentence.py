import copy
import json

from .Span import Span
from .Token import Token


class Sentence(Span):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tokens: list = kwargs.get('tokens', [])
        self.empty: bool  = kwargs.get('empty')

    @classmethod
    def from_json(cls, json_data: dict, do_tokenization=False):
        json_data = copy.deepcopy(json_data)
        if do_tokenization:
            pass  # TODO implement me (later)
        token_json_data = json_data.pop('tokens', [])
        sentence = cls(**json_data)
        for json_token in token_json_data:
            sentence.tokens.append(Token.from_json(json_token))
        return sentence

    def to_json(self):
        # TODO implement a test for me
        return json.dumps(self.to_texoo_dict(), default = lambda o:o.to_texoo_dict())
        
    def to_texoo_dict(self):
        return super().to_texoo_dict()