## Generated Story 7882715103327446561
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
	- slot{"location_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
	- utter_ask_budget
    - action_restaurant
	- utter_ask_restaurants_list_to_mail
* affirm
    - utter_get_email
* enter_email{"emailId": "chiranshubhatia@gmail.com"}
	- slot{"emailId": "chiranshubhatia@gmail.com"}
	- action_mail_results
	- utter_email_sent
	- utter_goodbye
	- utter_restart

## Generated Story 3898277359004523010
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - validate_location
	- slot{"location_avl": "1"}
	- utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
	- action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "300 to 700"}
	- utter_ask_restaurants_list_to_mail
* affirm
	- utter_get_email
* enter_email{"emailId": "chiranshubhatia@gmail.com"}
	- slot{"emailId": "chiranshubhatia@gmail.com"}
	- action_mail_results
	- utter_email_sent
	- utter_goodbye
	- utter_restart
	
## Generated Story 7048052416262072766
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai", "price": "more than 700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - slot{"price": "more than 700"}
    - validate_location
    - slot{"location_avl": "1"}
	- action_restaurant
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "more than 700"}
	- utter_ask_restaurants_list_to_mail
* affirm
	- utter_get_email
* enter_email{"emailId": "chirubhatia@live.com"}
	- slot{"emailId": "chirubhatia@live.com"}
	- action_mail_results
	- utter_email_sent
	- utter_goodbye
	- utter_restart

## Generated Story 5678272359004523010
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Lucknow"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Lucknow"}
    - validate_location
	- slot{"location_avl": "1"}
	- utter_ask_budget
* restaurant_search{"price": "300 to 700"}
    - slot{"price": "300 to 700"}
	- action_restaurant
    - slot{"location": "Lucknow"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "300 to 700"}
	- utter_ask_restaurants_list_to_mail
* deny
	- utter_goodbye
	- utter_restart
	
## Generated Story 4032620909897627882
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mirzapur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mirzapur"}
    - validate_location
	- slot{"location_avl": "0"}
	- utter_not_operate
	- utter_goodbye
	- utter_restart

## Generated Story 4032620909897627882
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "wasseypur"}
    - slot{"location": "mirzapur"}
    - validate_location
	- slot{"location_avl": "0"}
	- utter_not_operate
	- utter_goodbye
	- utter_restart
	
## Generated Story 5678272359004523010
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "chennai"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "chennai"}
    - validate_location
	- slot{"location_avl": "1"}
	- utter_ask_budget
* restaurant_search{"price": "less than 300"}
    - slot{"price": "less than 300"}
	- action_restaurant
    - slot{"location": "chennai"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "300 to 700"}
	- utter_ask_restaurants_list_to_mail
* deny
	- utter_goodbye
	- utter_restart
	
	
## Generated Story -9080914373946007185
* greet
    - utter_greet
* restaurants_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"location_avl": "1"}
    - utter_ask_cuisine
* restaurants_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_budget
* restaurants_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_restaurant
    - slot{"location": "Delhi"}
    - slot{"cuisine": "north indian"}
    - slot{"price": "more than 700"}
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
    - action_mail_results
    - utter_email_sent
    - utter_goodbye
	- utter_restart
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
	- utter_restart
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
	- utter_restart
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
    - action_mail_results
    - utter_email_sent
    - utter_goodbye
	- utter_restart
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
    - action_mail_results
    - utter_email_sent
    - utter_goodbye
	- utter_restart
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
    - action_mail_results
    - utter_email_sent
    - utter_goodbye
	- utter_restart
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
    - action_mail_results
    - utter_email_sent
    - utter_goodbye
	- utter_restart
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
    - action_mail_results
    - utter_email_sent
    - utter_goodbye
	- utter_restart
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
