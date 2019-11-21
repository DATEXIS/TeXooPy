class Span(object):
    def __init__(self, **kwargs):
        self.uid = kwargs.get('uid', None)
        self.begin = kwargs.get('begin', 0)
        self.length = kwargs.get('length', 0)
        self.text = kwargs.get('text', "")

    def to_texoo_dict(self) -> dict:
        content = self.__dict__
        content.pop('uid')
        return content
