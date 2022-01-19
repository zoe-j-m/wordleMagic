from typing import List, Dict, Optional, Callable
from wordlists import score_words_naive, filter_word, get_best_words, load_wordlist


def turn(turn_no: int, last_quess: str, last_result: str, word_list: List[str],
         score_words: Callable[[List[str]], Dict[str, int]]):
    if turn_no == 1:
        new_word_list = word_list
    else:
        new_word_list = [word for word in word_list if filter_word(word, last_quess, last_result)]

    if new_word_list:
        print(f"{len(new_word_list)} possibilities remain")
        scored_words = score_words(new_word_list)
        best_words = get_best_words(scored_words)
        if best_words:
            guess = best_words[0]
            print(f"I guess: {guess}")
            this_result = input("Enter result - x for misses, y for yellow, g for green, 'not' if not a wordle word: ")
            if this_result == "ggggg":
                print(f"Victory! The word was {guess} and I got it in {turn_no} turns")
            elif this_result == "not":
                new_word_list.remove(guess)
                turn(turn_no, last_quess, last_result, new_word_list)
            elif turn_no == 6:
                print('Rats. Defeated.')
            else:
                turn(turn_no + 1, best_words[0], this_result, new_word_list, score_words)
    else:
        print("ERROR! Either I don't know the word or you gave me wrong info earlier")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    words = load_wordlist("data/5-letter-words.json")
    turn(1, "", "", words, score_words_naive)

