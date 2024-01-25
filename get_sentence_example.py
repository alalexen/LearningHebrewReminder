from reverso_api.context import ReversoContextAPI


class Reverso:
    def __init__(self, source_word):
        self.source_word = source_word

        self.reverso_api = ReversoContextAPI(source_text=source_word,
                                             source_lang="he",
                                             target_lang="en")

    def get_example(self):
        """ Returns a sentence in Hebrew and its translation in English """
        examples = self.reverso_api.get_examples()
        first_example = next(examples)

        return {"he": first_example[0][0],
                "en": first_example[1][0]}

    def add_example_to_file(self, en_example, he_example):
        with open("examples.csv", "a") as v:
            v.write(
                "\n" + self.source_word + "\n" +
                "Example: \n{} ".format(he_example)
                + "\n{}\n".format(en_example)
                + "======================================================================== "
            )

