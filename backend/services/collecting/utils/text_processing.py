from collections import defaultdict
from geopy.geocoders import Nominatim
from natasha import MorphVocab
from loguru import logger
from razdel import tokenize
from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsNERTagger,
    Doc,
    NewsSyntaxParser,
    NewsMorphTagger
)


class TextProcessor():
    def __init__(self, text):
        self._text = text
        self.segmenter = Segmenter()
        self.morph_vocab = MorphVocab()
        self.emb = NewsEmbedding()
        self.doc = Doc(text)
        self.ner_tagger = NewsNERTagger(self.emb)
        self.syntax_parser = NewsSyntaxParser(self.emb)
        self.morph_tagger = NewsMorphTagger(self.emb)
        
    def get_text(self):
        return self._text

    def getNER(self):
        ner_dict = defaultdict(list)
        ners_categories = ["PER", "LOC", "ORG"]
        geolocator = Nominatim(user_agent="my_geocoder")
        self.doc.segment(self.segmenter)
        self.doc.parse_syntax(self.syntax_parser)
        self.doc.tag_ner(self.ner_tagger)
        self.doc.tag_morph(self.morph_tagger)
        docs_ners = list(set([x.type for x in self.doc.spans]))
        for ner_category in ners_categories:
            if ner_category in docs_ners:
                for span in self.doc.spans:
                    if ner_category == span.type:
                        span.normalize(self.morph_vocab)
                        span_dict = {"text": span.normal, "start": span.start, "stop": span.stop}
                        ner_dict[ner_category].append(span_dict)
                        if span.type == "LOC":
                            location = geolocator.geocode(span.normal)
                            if location:
                                span_dict["latitude"] = location.latitude
                                span_dict["longitude"] = location.longitude
                            else:
                                span_dict["latitude"] = 0
                                span_dict["longitude"] = 0
            else:
                ner_dict[ner_category] = []
        ner_dict = dict(ner_dict)
        return ner_dict
    
        
    
        
        
        
        
text = "Привет, Москва" 
processor = TextProcessor(text)
text = processor.get_text()
named_entities = processor.getNER()