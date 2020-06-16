from typing import List


State = str
States = List[State]
Word = str
Wordlist = List[Word]


def read_file(filename: str) -> List:
    with open(filename, "r") as f:
        data = [w.lower() for w in f.read().split("\n")]
    return data


def overlap(word: Word, state: State) -> bool:
    return any(letter in state for letter in word)


def state_overlap(word: Word, states: States) -> int:
    return [overlap(word, state) for state in states]


def mackerel(wordlist: Wordlist, states: States) -> Word:
    return max(filter(lambda word: sum(state_overlap(word, states)) == 49,
        wordlist), key=len)


if __name__ == "__main__":

    words = read_file("data/enable1.txt")
    states = read_file("data/states.txt")

    print(mackerel(words, states))
