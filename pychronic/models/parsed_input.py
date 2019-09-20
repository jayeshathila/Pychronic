from typing import List


class MatchedPattern:
    def __init__(self, from_index: int, to_index: int, parsed_value):
        self.from_index = from_index
        self.to_index = to_index
        self.parsed_value = parsed_value

    def __eq__(self, other):
        return (
            self.from_index == other.from_index
            and self.to_index == other.to_index
            and self.parsed_value == other.parsed_value
        )


class ParsedInput:
    def __init__(self, input_array: List[str]):
        self.input_array = input_array
        self.matched_pattern = []

    def add_matched_pattern(self, matched_pattern: MatchedPattern):
        self.matched_pattern.append(matched_pattern)
