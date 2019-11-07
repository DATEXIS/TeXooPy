import json
import unittest

from model.Document import Document, NotATeXooDocumentException
from model.Span import Span
from model.Dataset import Dataset


class DatasetTest(unittest.TestCase):

    def setUp(self) -> None:
        with open('res/texoo_dataset.json', 'r') as test_file:
            self.dataset = Dataset.from_json(json.load(test_file))

    def test_dataset_instance(self):
        self.assertIsInstance(self.dataset, Dataset)

    def test_dataset_name_property(self):
        self.assertEqual('dataset1', self.dataset.name)

    def test_dataset_language_property(self):
        self.assertEqual('de', self.dataset.language)

    def test_dataset_document_count(self):
        self.assertEqual(3, len(self.dataset.documents))


class DocumentTest(unittest.TestCase):

    def setUp(self) -> None:
        with open('res/texoo_dataset.json', 'r') as test_file:
            self.dataset = Dataset.from_json(json.load(test_file))

    def test_document_instances(self):
        self.assertIsInstance(self.dataset.documents[0], Document)
        self.assertIsInstance(self.dataset.documents[1], Document)

    def test_document_inheritance(self):
        self.assertTrue(issubclass(Document, Span))

    def test_document_id_property(self):
        self.assertEqual('document1', self.dataset.documents[0].id)

    def test_document_title_property(self):
        self.assertEqual('Der Froschkönig', self.dataset.documents[0].title)

    def test_document_language_property(self):
        self.assertEqual('de', self.dataset.documents[0].language)
        self.assertEqual(None, self.dataset.documents[2].language)

    def test_document_begin_property(self):
        self.assertEqual(0, self.dataset.documents[0].begin)

    def test_document_type_property(self):
        self.assertEqual(None, self.dataset.documents[0].type)
        self.assertEqual('test', self.dataset.documents[2].type)

    def test_document_length_property(self):
        self.assertEqual(7416, self.dataset.documents[0].length)

    def test_document_text_property(self):
        self.assertEqual("I am very short and do contain öä?@ß.", self.dataset.documents[2].text)

    def test_illegal_texoo_json_exception(self):
        with self.assertRaises(NotATeXooDocumentException):
            Document.from_json({'class': 'Span'})


# class DocumentTest(unittest.TestCase):
#
#     def setUp(self) -> None:
#         with open('res/texoo_dataset.json', 'r') as test_file:
#             self.dataset = Dataset.from_json(json.load(test_file))
#


if __name__ == '__main__':
    unittest.main()
