Here are the versions of various packages:

Flask== 1.1.1
Flask_mail==0.9.1
rasa_core==0.10.1
rasa_nlu==0.12.3
pyyaml==5.1.2
spacy==2.1.8
tensorflow==1.8.0
zomatopy==1.0.10


To run the bot:

Run nlu_model.py followed by dialogue_management.py and then start typing your questions.
When prompted, please provide your email ID and the search results will be emailed to you.



Please note:

1) While entering location, please start with "in". Examples - "In Bangalore", "Mexican food in Mumbai"
2) For selecting cuisine, just state cuisine name like : chinese, italian
3) Please select only one of the price ranges - lesser than 300, between rs 300 and more than 700. Numbers outside these 3 ranges results invalid output