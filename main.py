from add_words_from_pealim import AddWord
from get_sentence_example import Reverso


if __name__ == '__main__':
    words = ["הלילה"]
    # add_words = AddWord()
    # add_words.add_verbs_to_file_batch(words)
    for w in words:
        r = Reverso(w)
        res = r.get_example()
        r.add_example_to_file(res['he'], res['en'])
