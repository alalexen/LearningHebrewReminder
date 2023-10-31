# ---------------------   Conjugations and id locators  -----------------------

conjugations = {
    "Base Form": "INF-L",
    "אתה, ההווה - Masculine (Singular)": "AP-ms",
    "אתה, הווה - Feminine (Singular)": "AP-fs",
    "אתם, ההווה - Masculine (Plural)": "AP-mp",
    "אתן, ההווה - Feminine (Plural)": "AP-fp",
    "אני, עבר - Past Tense (I)": "PERF-1s",
    "אתה, עבר - Past Tense (You, Male, Singular)": "PERF-2ms",
    "את - Past Tense (You, Female, Singular)": "PERF-2fs",
    "הוא, עבר - Past Tense (He)": "PERF-3ms",
    "היא, עבר - Past Tense (She)": "PERF-3fs",
    "אנחנו, עבר - Past Tense (We)": "PERF-1p",
    "אתם, עבר - Past Tense (You, Male, Plural)": "PERF-2mp",
    "אתן, עבר - Past Tense (You, Female, Plural)": "PERF-2fp",
    "הם ,עבר - Past Tense (They, Male, Plural)": "PERF-3p",
    "הן, עבר - Past Tense (They, Female, Plural)": "PERF-3p",
    "אני, עתיד - Future Tense (I)": "IMPF-1s",
    "אתה, עתיד - Future Tense (You, Male, Singular)": "IMPF-2ms",
    "את, עתיד - Future Tense (You, Female, Singular)": "IMPF-2fs",
    "הוא, עתיד - Future Tense (He)": "IMPF-3ms",
    "היא, עתיד - Future Tense (She)": "IMPF-3fs",
    "אנחנו - Future Tense (We)": "IMPF-1p",
    "אתם, עתיד - Future Tense (You, Male, Plural)": "IMPF-2mp",
    "אתן, עתיד - Future Tense (You, Female, Plural)": "IMPF-2mp",
    "הם, עתיד - Future Tense (They, Male, Plural)": "IMPF-3mp",
    "הן, עתיד - Future Tense (They, Female, Plural)": "IMPF-3mp",
}

conjugation = "//div[@id='%s']//span[@class='menukad']"
translation = "//div[@class='lead']"

search_word_input = "//input[@id='search-box']"
go_button = "//input[@value='Go']"
view_full_conjugation = (
    "//a[@class='btn btn-primary' and contains(text(), 'View full conjugation')]"
)
meaning_title = "//h3[@class='page-header' and contains(text(), 'Meaning')]"
conjugation_of = "//h2[@class='page-header']"
