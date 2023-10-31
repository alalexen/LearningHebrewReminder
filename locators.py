# ---------------------   Conjugations and id locators  -----------------------

conjugations = {
    "Base Form": "INF-L",
    "Masculine (Singular)": "AP-ms",
    "Feminine (Singular)": "AP-fs",
    "Masculine (Plural)": "AP-mp",
    "Feminine (Plural)": "AP-fp",
    "Past Tense (I)": "PERF-1s",
    "Past Tense (You, Male, Singular)": "PERF-2ms",
    "Past Tense (You, Female, Singular)": "PERF-2fs",
    "Past Tense (He)": "PERF-3ms",
    "Past Tense (She)": "PERF-3fs",
    "Past Tense (We)": "PERF-1p",
    "Past Tense (You, Male, Plural)": "PERF-2mp",
    "Past Tense (You, Female, Plural)": "PERF-2fp",
    "Past Tense (They, Male, Plural)": "PERF-3p",
    "Past Tense (They, Female, Plural)": "PERF-3p",
    "Future Tense (I)": "IMPF-1s",
    "Future Tense (You, Male, Singular)": "IMPF-2ms",
    "Future Tense (You, Female, Singular)": "IMPF-2fs",
    "Future Tense (He)": "IMPF-3ms",
    "Future Tense (She)": "IMPF-3fs",
    "Future Tense (We)": "IMPF-1p",
    "Future Tense (You, Male, Plural)": "IMPF-2mp",
    "Future Tense (You, Female, Plural)": "IMPF-2mp",
    "Future Tense (They, Male, Plural)": "IMPF-3mp",
    "Future Tense (They, Female, Plural)": "IMPF-3mp",
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
