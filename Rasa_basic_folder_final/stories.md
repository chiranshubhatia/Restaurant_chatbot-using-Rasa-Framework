## Generated Story 925343355894731888
* greet
    - utter_greet
* restaurants_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - validate_location
    - slot{"location_avl": "1"}
    - utter_ask_cuisine
* restaurants_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_budget
* restaurants_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_restaurant
    - slot{"location": "chennai"}
    - slot{"cuisine": "south indian"}
    - slot{"price": "more than 700"}
    - utter_ask_restaurants_list_to_mail
* affirm
    - utter_get_email
* enter_email{"emailId": "chirubhatia@live.com"}
    - slot{"emailId": "chirubhatia@live.com"}
    - mail_results
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -240370741048154657
* greet
    - utter_greet
* restaurants_search{"price": "Lesser than Rs. 300", "location": "mirzapur"}
    - slot{"location": "mirzapur"}
    - slot{"price": "Lesser than Rs. 300"}
    - validate_location
    - slot{"location_avl": "0"}
    - utter_not_operate
    - utter_goodbye
    - export

## Generated Story -3342962979616669412
* greet
    - utter_greet
* restaurants_search{"location": "dehradun"}
    - slot{"location": "dehradun"}
    - validate_location
    - slot{"location_avl": "1"}
    - utter_ask_cuisine
* restaurants_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurants_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_restaurant
    - slot{"location": "dehradun"}
    - slot{"cuisine": "north indian"}
    - slot{"price": "rs. 300 to 700"}
    - utter_ask_restaurants_list_to_mail
* deny
    - utter_goodbye
    - export

## Generated Story -8111098264992322313
* greet
    - utter_greet
* restaurants_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"location_avl": "1"}
    - utter_ask_budget
* restaurants_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "rs. 300 to 700"}
    - utter_ask_restaurants_list_to_mail
* affirm
    - utter_get_email
* enter_email{"emailId": "chiranshubhatia@gmail.com"}
    - slot{"emailId": "chiranshubhatia@gmail.com"}
    - mail_results
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story -2541248928669535452
* greet
    - utter_greet
* restaurants_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"location_avl": "1"}
    - utter_ask_cuisine
* restaurants_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurants_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_restaurant
    - slot{"location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "more than 700"}
    - utter_ask_restaurants_list_to_mail
* deny
    - utter_goodbye
    - export

## Generated Story -717805410393785846
* greet
    - utter_greet
* restaurants_search{"cuisine": "Italian", "location": "Delhi"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"location_avl": "1"}
    - utter_ask_budget
* restaurants_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_restaurant
    - slot{"location": "Delhi"}
    - slot{"cuisine": "italian"}
    - slot{"price": "rs. 300 to 700"}
    - utter_ask_restaurants_list_to_mail
* enter_email{"emailId": "chirubhatia@live.com"}
    - slot{"emailId": "chirubhatia@live.com"}
    - utter_get_email
    - mail_results
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 5553583103670084796
* greet
    - utter_greet
* restaurants_search{"location": "krishna"}
    - slot{"location": "krishna"}
    - validate_location
    - slot{"location_avl": "0"}
    - utter_not_operate
    - utter_ask_howcanhelp
* restaurants_search{"cuisine": "north indian", "location": "dehradun"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "dehradun"}
    - validate_location
    - slot{"location_avl": "1"}
    - utter_ask_budget
* restaurants_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - action_restaurant
    - slot{"location": "dehradun"}
    - slot{"cuisine": "north indian"}
    - slot{"price": "more than 700"}
    - utter_ask_restaurants_list_to_mail
* affirm
    - utter_get_email
* enter_email{"emailId": "chirubhatia@live.com"}
    - slot{"emailId": "chirubhatia@live.com"}
    - mail_results
    - utter_email_sent
    - utter_goodbye
    - export

## Generated Story 323698442682826510
* affirm
    - export

## Generated Story 6628384017287286689
* deny
    - utter_goodbye
    - export

## Generated Story -8955587768097926513
* greet
    - utter_greet
* restaurants_search{"cuisine": "Italian", "location": "Delhi"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"location_avl": "1"}
    - utter_ask_budget
* restaurants_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_restaurant
    - slot{"location": "Delhi"}
    - slot{"cuisine": "italian"}
    - slot{"price": "rs. 300 to 700"}
    - utter_ask_restaurants_list_to_mail
* affirm
    - utter_get_email
* enter_email{"emailId": "chirubhatia@live.com"}
    - slot{"emailId": "chirubhatia@live.com"}
    - action_mail_results
    - utter_email_sent
    - utter_goodbye
    - utter_restart
    - export

