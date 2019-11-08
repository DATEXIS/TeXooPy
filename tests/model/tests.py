import json
import unittest

from model.Annotation import Annotation
from model.Document import Document, NotATeXooDocumentException
from model.MentionAnnotation import MentionAnnotation
from model.NamedEntityAnnotation import NamedEntityAnnotation
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

    def test_document_annotation_count(self):
        self.assertEqual(3, len(self.dataset.documents[0].annotations))

    def test_illegal_teXoo_json_exception(self):
        with self.assertRaises(NotATeXooDocumentException):
            Document.from_json({'class': 'Span'})


class MentionAnnotationTest(unittest.TestCase):

    def setUp(self) -> None:
        with open('res/texoo_dataset.json', 'r') as test_file:
            self.mention_ann_1 = Annotation.from_json(json.load(test_file)['documents'][0]['annotations'][0])
            self.mention_ann_2 = Annotation.from_json(json.load(test_file)['documents'][0]['annotations'][1])

    def test_mention_ann_class(self):
        self.assertIsInstance(self.mention_ann_1, MentionAnnotation)

    def test_mention_ann_begin(self):
        self.assertEqual(67, self.mention_ann_1.begin)

    def test_mention_ann_length(self):
        self.assertEqual(5, self.mention_ann_1.length)

    def test_mention_ann_text(self):
        self.assertEqual("König", self.mention_ann_1.text)

    def test_mention_ann_source(self):
        self.assertEqual("TRAIN", self.mention_ann_1.source)

    def test_mention_ann_confidence(self):
        self.assertEqual(0.0, self.mention_ann_1.confidence)
        self.assertEqual(0.4, self.mention_ann_2.confidence)

    def test_mention_ann_type(self):
        self.assertEqual("GENERIC", self.mention_ann_1.type)


class NamedEntityAnnotationTest(unittest.TestCase):

    def setUp(self) -> None:
        with open('res/texoo_dataset.json', 'r') as test_file:
            self.named_entity_ann = Annotation.from_json(json.load(test_file)['documents'][0]['annotations'][2])

    def test_mention_ann_class(self):
        self.assertIsInstance(self.named_entity_ann, NamedEntityAnnotation)

    def test_mention_ann_begin(self):
        self.assertEqual(67, self.named_entity_ann.begin)

    def test_mention_ann_length(self):
        self.assertEqual(5, self.named_entity_ann.length)

    def test_mention_ann_text(self):
        self.assertEqual("König", self.named_entity_ann.text)

    def test_mention_ann_source(self):
        self.assertEqual("GOLD", self.named_entity_ann.source)

    def test_mention_ann_confidence(self):
        self.assertEqual(1.0, self.named_entity_ann.confidence)

    def test_mention_ann_refId(self):
        self.assertEqual("TestRefId01", self.named_entity_ann.refId)


if __name__ == '__main__':
    unittest.main()
