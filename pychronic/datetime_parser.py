from pychronic.models.parse_pattern import patterns_to_match
from pychronic.models.parsed_input import ParsedInput, MatchedPattern
from pychronic.tagger import Tagger


def parse(text: str):
    if not text:
        return text

    tagged_words = Tagger().tag(source_text=text)
    rv = ParsedInput([t.word for t in tagged_words])
    index = 0
    while index < len(tagged_words):
        for pattern in patterns_to_match:
            pattern_size = len(pattern.pattern)
            probable_match = tagged_words[index : index + pattern_size]
            if [p.datatype for p in probable_match] == list(pattern.pattern):
                value = pattern.parser(probable_match)
                if value:
                    rv.add_matched_pattern(
                        MatchedPattern(
                            from_index=index,
                            to_index=index + pattern_size - 1,
                            parsed_value=value,
                        )
                    )
                    index += pattern_size - 1
                    break
        index += 1
    return rv
