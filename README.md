*How to add verbs*: 

1. Add AddBlock extension (see below)
2. Run add_words_from_pealim.py with provided list of hebrew infinitives (add_verbs_to_file_batch)

*How to add AddBlock*:

1. To download and save the extension as .crx file
2. Add option to the driver: driver.add_extension('User/path_to_file.crx')

*How to set reminder*: 

Currently, to use reminder you need to create a crontab.
You'll need to navigate to the project directory and activate venv, then run file reminder.py 
Reminder will open a window with word-translation and close it after 5sec

*For verbs practicing*:

Run questions_verbs.py
It'll ask you a correct translation of added words


