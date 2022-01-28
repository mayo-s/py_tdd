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
