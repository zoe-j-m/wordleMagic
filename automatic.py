from typing import List, Dict, Optional, Callable
from wordlists import score_words_naive, filter_word, get_best_words, load_wordlist
from collections import Counter


def auto_result(actual: str, guess_in: str) -> str:
    out = list("     ")
    working = list(actual)
    guess = list(guess_in)
    for i in range(5):
        if working[i] == guess[i]:
            out[i] = "g"
            working[i] = " "
            guess[i] = " "

    for i in range(5):
        if guess[i] != " ":
            for j in range(5):
                if working[j] == guess[i]:
                    out[i] = "y"
                    working[j] = " "
                    guess[i] = " "
                    break

    for i in range(5):
        if guess[i] != " ":
            out[i] = "x"

    return "".join(out)


def turn_auto(actual: str, turn_no: int, last_guess: str, last_result: str, word_list: List[str], score_words: Callable[[List[str]], Dict[str, int]]) -> Optional[int]:
    if turn_no == 1:
        new_word_list = word_list
    else:
        new_word_list = [word for word in word_list if filter_word(word, last_guess, last_result)]

    if new_word_list:
        scored_words = score_words(new_word_list)
        best_words = get_best_words(scored_words)
        if best_words:
            guess = best_words[0]
            this_result = auto_result(actual, guess)
            if this_result == "ggggg":
                return turn_no
            elif turn_no == 6:
                return None
            else:
                return turn_auto(actual, turn_no + 1, guess, this_result, new_word_list, score_words)

    else:
        print("ERROR! Either I don't know the word or you gave me wrong info earlier")
        return None


if __name__ == '__main__':
    words = load_wordlist("data/5-letter-words.json")
    output = {word: turn_auto(word, 1, "", "", words, score_words_naive) for word in words}
    count = Counter(output.values())
    print(count)