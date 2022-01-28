class NerModelMock:
    """
    Test double for Spacy NLP model
    """

    def __init__(self, model):
        self.model = model

    def returns_document_entities(self, entities):
        self.ents = entities

    def __call__(self, sentence):
        return DocumentMock(sentence, self.ents)


class DocumentMock:
    """
    Test double for spacy Document
    """

    def __init__(self, sentence, entities):
        self.ents = [SpanMock(ent['text'], ent['label_']) for ent in entities]


class SpanMock:
    """
    Test double for spacy Span
    """

    def __init__(self, text, label):
        self.text = text
        self.label_ = label
