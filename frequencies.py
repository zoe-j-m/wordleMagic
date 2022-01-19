from collections import Counter
from typing import List, Dict

def create_frequencies(word_list: List[str]) -> Dict[str, int]:
    all_letters = ''.join(word_list)
    return dict(Counter(all_letters))