# ---------------------   Conjugations and id locators  -----------------------

conjugations = {
    "Base Form": "INF-L",
    "אתה, ההווה": "AP-ms",
    "אתה, הווה": "AP-fs",
    "אתם, ההווה": "AP-mp",
    "אתן, ההווה": "AP-fp",
    "אני, עבר": "PERF-1s",
    "אתה, עבר": "PERF-2ms",
    "את, עבר": "PERF-2fs",
    "הוא, עבר": "PERF-3ms",
    "היא, עבר": "PERF-3fs",
    "אנחנו, עבר": "PERF-1p",
    "אתם, עבר": "PERF-2mp",
    "אתן, עבר": "PERF-2fp",
    "הם ,עבר": "PERF-3p",
    "הן, עבר": "PERF-3p",
    "אני, עתיד": "IMPF-1s",
    "אתה, עתיד": "IMPF-2ms",
    "את, עתיד": "IMPF-2fs",
    "הוא, עתיד": "IMPF-3ms",
    "היא, עתיד": "IMPF-3fs",
    "אנחנו ,עתיד": "IMPF-1p",
    "אתם, עתיד": "IMPF-2mp",
    "אתן, עתיד": "IMPF-2mp",
    "הם, עתיד": "IMPF-3mp",
    "הן, עתיד": "IMPF-3mp",
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
