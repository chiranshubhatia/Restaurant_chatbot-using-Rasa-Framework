## regex:zipcode
- [0-9]{5}
- [0-9]{6}
## regex:greet
- hey[^\\s]*
- hello[^\\s]*
- hi[^\\s]*
## regex:emailId
- ^(\\D\\w.)*@(\\w.*)
## regex:Lesser than Rs. 300
- <[\\s]+300
## regex:Rs. 300 to 700
- >[\\s]+300+<[\\s]+700

## regex:More than 700
- >[\\s]+700

## synonym:Lesser than Rs. 300
- cheap
- cheaper
- between Rs. 100 and 300
- pocket-friendly
- budget
- low cost
- less than 300
- budget-friendly
- low-cost
- inexpensive
- under 300
- upto 300
- lite
- less than rs. 300
- less than 300
- <300

##synonym:Rs. 300 to 700
- reasonable
- around 500
- around 700
- below 700
- mid budget
- meduim price
- medium price
- within 700
- within 600
- good price
- upto rs700
- 700
- 600
- 500
- 400
- average price
- medium range
- > 300
- good price
- upto 700 rs.

## synonym:More than 700
- expensive
- more than rs 700
- more than 700
- gourmet
- costly
- high class
- fancy
- above 700
- over 700rs
- most expensive
- costliest
- > rs 700
- rich
- >700 Rs


## intent:greet
- Hi
- Hey
- Hi bot
- Hey bot
- Hello
- Good morning
- hi again
- hi folks
- hi Mister
- hi pal!
- hi there
- greetings
- hello everybody
- hello is anybody there
- hello robot
- hallo
- heeey
- hi hi
- hey
- hey hey
- hello there
- hi
- hello
- yo
- hola
- hi?
- hey bot!
- hello friend
- good morning
- hii
- hello sweet boy
- yoo
- hey there
- hiihihi
- hello sweatheart
- hellooo
- helloooo
- heyo
- ayyyy whaddup
- hello?
- Hallo
- heya
- hey bot
- howdy
- Hellllooooooo
- whats up
- Hei
- Well hello there ;)
- I said, helllllloooooO!!!!
- Heya
- Whats up my bot
- hiii
- heyho
- hi there
- hi
- jop
- hi friend
- hi there it's me
- good evening
- good morning
- good afternoon

## intent:affirm
- yes
- of course
- sure
- yeah
- ok
- cool
- go for it
- yep
- yep, will do thank you
- I'm sure I will!
- oh awesome!
- Yes
- accept
- I accept
- i accept
- ok i accept
- I changed my mind. I want to accept it
- ok cool
- alright
- i will!
- ok, I behave now
- yop
- oki doki
- yes please
- yes please!
- jo
- yep if i have to
- amayzing
- confirm
- nice
- coolio
- definitely yes without a doubt
- yas
- yup
- perfect
- sure thing
- absolutely
- Oh, ok
- Sure
- hm, i'd like that
- ja
- sure!
- yes i accept
- Sweet
- amazing!
- how nice!
- cool!
- yay
- yes accept please
- great
- oh cool
- yes
- fine

## synonym:vegetarian
- veggie
- veg
- vegg


## synonym:restaurants
- restarants
- resturants

## synonym:Chinese
- Chinese
- chines
- chines
- chini


## synonym:Mexican
- mxcn
- Mxcn
- Mexica
- mexican
- mexcan

## synonym:Italian
- italian
- italn
- itln
- italn
- Itlan
- Italan
- italian

## synonym:American
- american
- amrcn
- amricn
- amirican
- Amricn

## synonym:South Indian
- south india
- southInd
- SothInd
- sth indian
- southindain
- south-indian

## synonym:North Indian
- nothInd
- northInd
- Northindain
- nrthindian
- northindain
- nothindian
- north-indian
## synonym:Ahmedabad
- Ahmadabad
- Ahmdbd
- Ahmdbad
- ahmedabad

## synonym:Bangalore
- bangalore
- Bengaluru
- bnglr
- Bnglor
- bengaluru
- bengluru


## synonym:Chennai
- Madras
- madras
- chn
- Chenai
- chnnai
- chenni
- madrs

## synonym:Delhi
- Dilli
- Dehli
- Deli
- delhi
- new delhi
- New Delhi
- delli

## synonym:Hyderabad
- Hydrbd
- hyderabad
- hyd
- Hyd

## synonym:Kolkata
- Klkta
- kolkata
- Calcutta
- Calcuta
- kolkatta
- kolkata
- calcutta
- calicut

## synonym:Mumbai
- Bombay
- mumbai
- Bmbay
- bmby
- bombay
- bomb

## synonym:Pune
- pune
- Poona
- Puna
- Pona
- pune
- pune
- punae

## synonym:Ajmer
- Azmer
- Ajmer Sharif
- ajmer
- Ajmer Shareef

## synonym:Aligarh
- aligarh
- Aligadh
- Algdh

## synonym:Allahabd
- Illahabad
- allahabad
- Prayagraj
## synonym:Amritsar
- Amrtsr
- amritsar
## synonym:Bareilly
- bareilly
- Barely
- Bareilli
- Bareli
- Barele

## synonym:Bhopal
- bhopal
- Bhpal
## synonym:Bhubaneswar
- bhubaneswar
- Bhubaneswhar
- Bhvnswr
- Bhuvnswar
## synonym:Chandigarh
- Chandigadh
- Chndigdh
- Chndigadh
- Chandigarh
## synonym:Dehradun
- dehradum
- Dehradoon
- Dhraadun
## synonym:Faridabad
- faridabad
- Fridabad
## synonym:Gurgaon
- gurgaon
- Gurugram
- gorgaon
## synonym:Jaipur
- Pink City
- jaipur
## synonym:Noida
- noida
- noidaa

## intent:restaurants_search
- restaurants
- i want a [American](cuisine) restaurant in [west](location)
- i'm looking for a [Chinese](cuisine) restaurant
- I need a new restaurant in [mumbai](location)
- help me find restaurant some [southindian](cuisine:South Indian)
- I'm gonna need help finding a restaurant
- Hey help me find a restaurant
- How can you help me find a restaurant.
- Show me how to find a restaurant
- I need to find [Italian](cuisine) restaurant in [pune](location)
- Help me with finding this restaurant
- Hey, can you help me with locating [Mexican](cuisine) restaurant.
- Find me a place to eat [indian](cuisine)
- Can you recommend [North Indian](cuisine) restaurant.
- I am hungry, find me some place to go
- I am hungry, find me some place to eat
- find me a [North Ind](cuisine:North Indian) place in the [hyderabad](location)
- Suggest me a good restaurant around
- What's a good place to eat [southindain](cuisine:South Indian) food
- Recommend me a restaurant around here.
- Pick a restaurant for me, please
- Help me find a restaurant in [madras](location:Chennai)
- Can you find a restaurant for me?
- Find a restaurant for me?
- show me a [americn](cuisine:American) place in [bengaluru](location:Bangalore)
- Would you find me a restaurant?
- Would you find a restaurant for me?
- find [american](cuisine) restaurant in [punae](location:Pune)
- Could you find me a restaurant?
- Could you find a restaurant for me?
- look for a [south-indian](cuisine:South Indian) place [new Delhi](location:Dehli)
- Could you find me a restaurant to eat at?
- Find a restaurant for me to eat at.
- Find me a restaurant where I can eat.
- Find a restaurant for me where I can eat.
- I need a restaurant.
- Can you find me a restaurant?
- Where should I eat?
- i'm looking for a place to eat
- I want to grab lunch
- find me a [North Ind](cuisine:North Indian) place in the [hyderabad](location:Hyderabad)
- i'm looking for a place in the [north](location) of town
- show me a [mexican](cuisine) place in the [centre](location)
- [Mexican](cuisine) + [300 to 700](price:Rs. 300 to 700) budget + [near me](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- anywhere near [18328](location)
- I am looking for [asian](cuisine:North Indian) fusion food
- I am looking a restaurant in [29432](location)
- in [delhi](location)
- Oh, sorry, in [Italy](location)
- I am looking for some restaurants in [bangalore](location).
- I am looking for [mexican indian fusion](cuisine:Mexican)
- can you book a table in [rome](location) in a [moderate](price) price range with [british](cuisine) food for four people
- [central](location) [indian](cuisine) restaurant
- i d like [Italian](cuisine)
- i'd like [American](cuisine)
- i would like [Mexican](cuisine)
- i'd like [Chinees](cuisine:Chinese)
- I d like [Americn](cuisine:American)
- I'd like prefer [Chinese](cuisine:Chinese)
- i ll prefer [America](cuisine:American)
- I will prefer [Mexican](cuisine:Mexican)
- [banaras](location)
- [ranchi](location)
- i am looking for [mexican](cuisine:Mexican) Cuisine in [south delhi](location:Delhi)
- [nagpur](location)
- [durgapur](location)
- [Pune](location)
- show me restaurant with average price budget of [less than rs 300](price:Lesser than Rs. 300)
- [Mumbai](location)
- [Delhi](location)
- [Kolkata](location)
- [Chennai](location)
- [Bangalore](location)
- [Hyderabad](location)
- [Ahmedabad](location)
- [Surat](location)
- [Kanpur](location)
- [Indore](location)
- [Jaipur](location)
- [Vadodara](location)
- [Patna](location)
- [vishakapatnam](location)
- [noida](location:Noida)
- [bombay](location:Mumbai)
- [delhi](location:delhi)
- [new delhi](location:delhi)
- which are the best [north indian](cuisine) restaurants in [chennai](location)
- [Mexican](cuisine)  [300 to 700 budget](price:Rs. 300 to 700)  [near me](location)
- show me restaurant with average price budget of [less than rs 300](price:Lesser than Rs. 300)
- show me restaurant with [average price budget](price)
- show me some [cheaper](price:Lesser than Rs. 300) restaurants
- find me [high class](price:More than 700) restaurants
- help me find [moderate](price:Rs. 300 to 700) place to eat.
- [below 300](price:Lesser than Rs. 300)
- restaurnts [less than rs.300](price:Lesser than Rs. 300)
- find [cheaper](price:Lesser than Rs. 300) place to eat in [delhi](location)
- get me [moderate](price:Rs. 300 to 700) [Italian](cuisine) restaurants [near by](location)
- show me [cheap](price:Lesser than Rs. 300) place to eat in [delhi](location)
- show me restaurant with average price budget of [300 to 700 rs](price) in [pune](location)
- show me [Indian](cuisine) restaurant with [average budget of 300 to 700](price) rupees
- [300-700 range](price)
- between [300 and 700](price:Rs. 300 to 700)
- show me restaurant with average price budget of [more than rs 700](price)
- get me [Italian](cuisine) restaurant with average price budget of [above rs 700] in [bangalore](location)
- with price [rs.700 or higher](price:More than 700)
- show me a [Mexican](cuisine) place in the [East Andheri](location)
- budget is [More than 700](price)
- budget is [less than 300](price)
- budget is [between 300 to 700](price)
- looking for [average cost](price) restaurant in [pune](location)
- looking for [medium range](price) place to eat
- show me restaurant with average price budget of [below 300](price:Lesser than Rs. 300)
- find some [mid range](price) restaurants in mumbai
- get me some [low cost](price) place to grab [Northindain](cuisine:North Indian) dinner
- show me restaurant with average price budget of [Rs.300 to Rs.700](price)
- help me finding restaurant with price budget of [300 to 700 rs](price) 
- could you show me [Italian](cuisine) restaurant with average budget of [300 to 700 rupees](price)
- could you find me [Chinese](cuisine) restaurant with average budget of [700 rupees and above](price:More than 700)
- Which are the best [Italian](cuisine) food joints in [Delhi](location) with average [cost of 500](price:Rs. 300 to 700) for 2 people
- Which place do I go for [sizzlers](cuisine) with a budget of [1000](price) for 2 people
- Where do I get breakfast buffet in [Mumbai](location) [under 300](price:Lesser than Rs. 300)
- Tell me the top 5 restaurants in [Pune](location) for dinner
- What are the top 10 places in [Goa](location) that serve vegetarian food?
- Where do I find the best [south Indian](cuisine) food in [Chandigarh](location)?
- Are there any [Maharashtrian thali](cuisine) joints in [Kolkata](location)?
- Can you give me the names of restaurants that have buffet [under 700](price:Rs. 300 to 700)
- i'm looking for a place in the [heart](location) of city
- I am Hungry, Show me some place [nearby](location)
- Find best restro for two people in [bangalore](location) within budget of [700 ](price)
- Find me something [Classy](price:More than 700) and [Italian](cuisine)
- Quick bite [fit in my pocket](price:Lesser than Rs. 300)
- [MId](price:Rs. 300 to 700) segment [Mexican](cuisine) restro close to me
- dinning out options [Mexican](cuisine) or [Italian](cuisine)
- get me good munching option preferably [Chines](cuisine)
- [300-700](price) range eating option anywhere
- I want to eat [indian](cuisine) food in [Bangalore](location)
- [american](cuisine) food [< 300](price:Lesser than Rs. 300)
- best [chinese](cuisine) [< 700](price:Rs. 300 to 700)
- [south indian](cuisine) [> 700](price:More than 700)
- budget [italian](cuisine) places in [bangalore](location)
- find me some [low budget](price:Lesser than Rs. 300) restaurant in [pune](location)
- get me [low budget](price:Lesser than Rs. 300) restaurant
- could help me finding [low budget](price:Lesser than Rs. 300) restaurant
- could you get list of [high class](price:More than 700) restarants
- [Chinese](cuisine)
- [Mexican](cuisine)
- [Italian](cuisine)
- [American](cuisine)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [more than 700](price:More than 700)
- [above 700](price:More than 700]
- [high class](price:More than 700 restaurnts
- between [rs 300 to 700](price:Rs. 300 to 700)
- restarants between [rs 300 to 700](price)
- [less than 300](price:Lesser than Rs. 300)
- [below 300](price:Lesser than Rs. 300)
- [300 and below](price:Lesser than Rs. 300)
- [less than rs.300](price:Lesser than Rs. 300)
- [<300](price:Lesser than Rs. 300)
- show me restaurant with average price budget of [Rs.300 to Rs.700](price:Rs. 300 to 700)
- [300-700](price:rs 300 to 700)
- between [300 and 700](price:rs 300 to 700)
- restaurant with average price budget of [over 700](price:More than 700)

## intent:enter_email
- [chirubhatia@live](emailId)
- [rajmalhotra@gmail.com](emailId)
- [rahul.jain@yahoo.co.in](emailId)
- [ravi_sen@hotmail.web](emailId)
- my email id is [chiranshubhatia@gmail.com](emailId)
- here is my email id [chirubhatia@live.com](emailId)
- emailid [abchlf@yahoo.co.in](emailId)
- email [jlasg@coowink.com](emailId)
- id [bdflbat@jlkjas.com](emailId)
## intent:goodbye
- goodbye
- goodnight
- good bye
- good night
- see ya
- toodle-oo
- bye bye
- gotta go
- farewell
- catch you later
- bye for now
- bye
- bye was nice talking to you
- bye bye bot
- bye bot
- tlak to you later
- ciao
- Bye bye
- bye!
## intent:deny
- no
- absolutely not
- no sorry
- No, not really.
- nah
- no thanks
- decline
- deny
- i decline
- never mind
- I'm not giving you my email address
- I don't want to give it to you
- no!
- nah thanks

## lookup:location
- Mumbai
- Delhi
- Kolkata
- Chennai
- Bangalore
- Hyderabad
- Ahmedabad
- Surat
- Pune
- Kanpur
- Indore
- Jaipur
- Vadodara
- Nagpur
- Lucknow
- Patna
- Vishakapatnam
- Bhopal
- Gwalior
- Jabalpur
- Aurangabad
- Gandhinagar
- Madurai
- Aligarh
- Kochi
- Coimbatore
- Vijayawada
- Tiruchirapalli
- Nashik
- Rajkot
- Solapur
- Anand
- Ludhiana
- Agra
- Meerut
- Thiruvananthapuram
- Kozhikode
- Faridabad
- Varanasi
- Jamshedpur
- Allahabad
- Amritsar
- Gorakhpur
- Hubli-Dharwad
- Bhavnagar
- Raipur
- Mysore
- Thrissur
- Mangalore
- Guntur
- Bhubaneswar
- Amravati
- Srinagar
- Bhilai
- Warangal
- Tirunelveli
- Nellore
- Ranchi
- Guwahati
- Aurangabad
- Chandigarh
- Patiala
- Jodhpur
- Pondicherry
- Salem


