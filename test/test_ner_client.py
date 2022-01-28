import unittest

from ner_client import NamedEntityClient
from test_mocks import NerModelMock


class TestNerClient(unittest.TestCase):

    def test_get_entities_returns_dictionary_given_empty_string_causes_empty_spacy_document_entities(self):
        model = NerModelMock('eng')
        model.returns_document_entities([])
        ner = NamedEntityClient(model)
        entities = ner.get_entities("")
        self.assertIsInstance(entities, dict)  # add assertion here

    def test_get_entities_returns_dictionary_given_nonempty_stringcauses_empty_spacy_document_entities(self):
        model = NerModelMock('eng')
        model.returns_document_entities([])
        ner = NamedEntityClient(model)
        entities = ner.get_entities("Berlin is a City in Germany")
        self.assertIsInstance(entities, dict)  # add assertion here

    def test_get_entities_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NerModelMock('eng')
        doc_entities = [{'text': 'Yoshi', 'label_': 'PERSON'}]
        model.returns_document_entities(doc_entities)
        ner = NamedEntityClient(model)
        result = ner.get_entities('...')
        expected_result = {'ents': [{'ent': 'Yoshi', 'label': 'Person'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_entities_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = NerModelMock('eng')
        doc_entities = [{'text': 'Canada', 'label_': 'NORP'}]
        model.returns_document_entities(doc_entities)
        ner = NamedEntityClient(model)
        result = ner.get_entities('...')
        expected_result = {'ents': [{'ent': 'Canada', 'label': 'Group'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_entities_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model = NerModelMock('eng')
        doc_entities = [{'text': 'the north', 'label_': 'LOC'}]
        model.returns_document_entities(doc_entities)
        ner = NamedEntityClient(model)
        result = ner.get_entities('...')
        expected_result = {'ents': [{'ent': 'the north', 'label': 'Location'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_entities_given_spacy_LANGUAGE_is_returned_serializes_to_Language(self):
        model = NerModelMock('eng')
        doc_entities = [{'text': 'ASL', 'label_': 'LANGUAGE'}]
        model.returns_document_entities(doc_entities)
        ner = NamedEntityClient(model)
        result = ner.get_entities('...')
        expected_result = {'ents': [{'ent': 'ASL', 'label': 'Language'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_entities_given_spacy_GPE_is_returned_serializes_to_Location(self):
        model = NerModelMock('eng')
        doc_entities = [{'text': 'Australia', 'label_': 'LOC'}]
        model.returns_document_entities(doc_entities)
        ner = NamedEntityClient(model)
        result = ner.get_entities('...')
        expected_result = {'ents': [{'ent': 'Australia', 'label': 'Location'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_entities_given_multiple_entities_serializes_all(self):
        model = NerModelMock('eng')
        doc_entities = [{'text': 'Australia', 'label_': 'LOC'}, {'text': 'Yoshi', 'label_': 'PERSON'}]
        model.returns_document_entities(doc_entities)
        ner = NamedEntityClient(model)
        result = ner.get_entities('...')
        expected_result = {'ents': [
            {'ent': 'Australia', 'label': 'Location'}, {'ent': 'Yoshi', 'label': 'Person'}], 'html': ''}
        self.assertListEqual(result['ents'], expected_result['ents'])
