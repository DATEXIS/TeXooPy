import copy
import json
import os
import unittest

from ..model.SectionAnnotation import SectionAnnotation
from ..model.Annotation import Annotation
from ..model.Document import Document, NotATeXooDocumentException
from ..model.MentionAnnotation import MentionAnnotation
from ..model.NamedEntityAnnotation import NamedEntityAnnotation
from ..model.Span import Span
from ..model.Dataset import Dataset

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'res', 'texoo_dataset.json')
SECTION_ANNOTATION_TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'res', 'pubmedsection_example.json')


class DatasetTest(unittest.TestCase):

    def setUp(self) -> None:
        with open(TESTDATA_FILENAME, 'r') as test_file:
            self.dataset_json_dict = json.load(test_file)
            self.dataset = Dataset.from_json(self.dataset_json_dict)

    def test_dataset_instance(self):
        self.assertIsInstance(self.dataset, Dataset)

    def test_dataset_name_property(self):
        self.assertEqual('dataset1', self.dataset.name)

    def test_dataset_language_property(self):
        self.assertEqual('de', self.dataset.language)

    def test_dataset_document_count(self):
        self.assertEqual(3, len(self.dataset.documents))

    def test_dataset_to_json(self):
        self.assertEqual(self.dataset_json_dict, json.loads(self.dataset.to_json()))

    def test_dataset_toJson_mutability(self):
        pass  # TODO IMPLEMENT ME


class DocumentTest(unittest.TestCase):

    def setUp(self) -> None:
        with open(TESTDATA_FILENAME, 'r') as test_file:
            self.dataset_json_dict = json.load(test_file)
            self.document_json_dict = copy.deepcopy(self.dataset_json_dict['documents'][0])
            self.dataset = Dataset.from_json(self.dataset_json_dict)
            self.document_1 = Document.from_json(copy.deepcopy(self.document_json_dict))

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
        self.assertEqual(4, len(self.dataset.documents[0].annotations))

    def test_illegal_teXoo_json_exception(self):
        with self.assertRaises(NotATeXooDocumentException):
            Document.from_json({'class': 'Span'})

    def test_document_to_json(self):
        self.assertEqual(self.document_json_dict, json.loads(self.document_1.to_json()))

    def test_document_toJson_mutability(self):
        before = copy.deepcopy(self.document_1.__dict__)
        self.document_1.to_json()
        after = copy.deepcopy(self.document_1.__dict__)
        # Annotations should get tested in a separate test so here we only compare the correct count.
        before['annotations'] = len(before.get('annotations'))
        after['annotations'] = len(after.get('annotations'))
        self.assertEqual(before, after)


class MentionAnnotationTest(unittest.TestCase):

    def setUp(self) -> None:
        with open(TESTDATA_FILENAME, 'r') as test_file:
            json_data = json.load(test_file)
            self.mention_ann_1_json_dict = json_data['documents'][0]['annotations'][0]
            self.mention_ann_1 = Annotation.from_json(self.mention_ann_1_json_dict)
            self.mention_ann_2 = Annotation.from_json(json_data['documents'][0]['annotations'][1])

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

    def test_mention_ann_to_json(self):
        self.assertEqual(self.mention_ann_1_json_dict, json.loads(self.mention_ann_1.to_json()))

    def test_mention_ann_toJson_mutability(self):
        pass  # TODO IMPLEMENT ME


class NamedEntityAnnotationTest(unittest.TestCase):

    def setUp(self) -> None:
        with open(TESTDATA_FILENAME, 'r') as test_file:
            test_file_json = json.load(test_file)
            self.named_entity_ann_json_dict = test_file_json['documents'][0]['annotations'][2]
            self.named_entity_ann = Annotation.from_json(self.named_entity_ann_json_dict)
            self.named_entity_ann_with_type_json_dict = test_file_json['documents'][0]['annotations'][3]
            self.named_entity_ann_with_type = Annotation.from_json(self.named_entity_ann_with_type_json_dict)

    def test_named_ann_class(self):
        self.assertIsInstance(self.named_entity_ann, NamedEntityAnnotation)

    def test_named_ann_begin(self):
        self.assertEqual(67, self.named_entity_ann.begin)

    def test_named_ann_length(self):
        self.assertEqual(5, self.named_entity_ann.length)

    def test_named_ann_text(self):
        self.assertEqual("König", self.named_entity_ann.text)

    def test_named_ann_source(self):
        self.assertEqual("GOLD", self.named_entity_ann.source)

    def test_named_ann_confidence(self):
        self.assertEqual(1.0, self.named_entity_ann.confidence)

    def test_named_ann_refId(self):
        self.assertEqual("TestRefId01", self.named_entity_ann.refId)

    def test_named_ann_to_json(self):
        self.assertEqual(self.named_entity_ann_json_dict, json.loads(self.named_entity_ann.to_json()))

    def test_named_ann_with_type_to_json(self):
        self.assertEqual(self.named_entity_ann_with_type_json_dict, json.loads(self.named_entity_ann_with_type.to_json()))

    def test_named_ann_type_set(self):
        self.assertEqual("PERSON", self.named_entity_ann_with_type.type)

    def test_named_ann_type_unset(self):
        self.assertEqual(None, self.named_entity_ann.type)

    def test_named_ann_toJson_mutability(self):
        pass  # TODO IMPLEMENT ME


class SectionAnnotationTest(unittest.TestCase):

    def setUp(self) -> None:
        with open(SECTION_ANNOTATION_TESTDATA_FILENAME, 'r') as test_file:
            self.section_ann_json_dict = json.load(test_file)['annotations'][0]
            self.section_ann = Annotation.from_json(self.section_ann_json_dict)

    def test_section_ann_class(self):
        self.assertIsInstance(self.section_ann, SectionAnnotation)

    def test_section_ann_begin(self):
        self.assertEqual(0, self.section_ann.begin)

    def test_section_ann_length(self):
        self.assertEqual(818, self.section_ann.length)

    def test_section_ann_text(self):
        self.assertIsNone(None, self.section_ann.text)

    def test_section_ann_source(self):
        self.assertEqual("GOLD", self.section_ann.source)

    def test_section_ann_confidence(self):
        self.assertEqual(1.0, self.section_ann.confidence)

    def test_section_ann_to_json(self):
        self.assertEqual(self.section_ann_json_dict, json.loads(self.section_ann.to_json()))

    def test_section_ann_toJson_mutability(self):
        pass  # TODO IMPLEMENT ME


if __name__ == '__main__':
    unittest.main()
