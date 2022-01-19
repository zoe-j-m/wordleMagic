from typing import List, Dict
from frequencies import create_frequencies
import json
from collections import Counter

def load_wordlist(file_name: str) -> List[str]:
    f = open(file_name)
    json_words = json.load(f)
    words = [v["word"] for v in json_words]
    f.close()
    return words


def score_words_naive(word_list: List[str]) -> Dict[str, int]:
    freqs = create_frequencies(word_list)
    output = {}
    for word in word_list:
        score = 0
        for letter in set(word):
            score = score + freqs[letter]
        output[word] = score
    return output


def filter_word(word: str, last_guess: str, last_result: str) -> bool:
    word_counter = Counter(word)
    guess_counter = Counter(last_guess)

    for i in range(5):
        if last_result[i] == 'x' and last_guess[i] in word and word_counter[last_guess[i]] >= guess_counter[
            last_guess[i]]:
            return False
        elif last_result[i] == 'y' and (last_guess[i] not in word or word[i] == last_guess[i]):
            return False
        elif last_result[i] == 'g' and word[i] != last_guess[i]:
            return False

    return True


def get_best_words(scored_words: Dict[str, int]) -> List[str]:
    max_score = max(scored_words.values())
    return [word for word, score in scored_words.items() if score == max_score]