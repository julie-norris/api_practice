I completed this technical challenge using Python and Flask. 

<<<<<<< HEAD
The server.py file renders the html address_form to accept an address input from the user. 
=======
The /search route then uses that address to query the api to find elections in the vicinity of the city and state inputs. Initially the server failed if a city name was two words or more. Line 27 was added to join multiple word city names with an underscore to prevent the error. 

The results from the query are displayed on the html election_results page. I decided to display only the information from the results that would be useful to a non-technical user: Description - telling which election is occurring,  Polling Place Url - so the user can locate their polling place, Website - providing the user with a reference to get more information about the election, and Date. If there are no elections in the vicinity of the address that was input, a message is displayed on the election_results page stating that there are no elections.

>>>>>>> 82ec124a416187027f57da6861c622e019448d0d

The /search route then uses that address to query the api to find elections in the vicinity of the city and state inputs. Initially the server failed if a city name was two words or more. Line 27 was added to join multiple word city names with an underscore to prevent the error. 

The results from the query were displayed on the html election_results page. I display only the information from the results that would be useful to a non-technical user: Description - telling which election is occurring,  Polling Place Url - so the user can locate their polling place, Website - providing the user with a reference to get more information about the election, and Date. If there are no elections in the vicinity of the address that was input, a message is displayed on the election_results page stating that there are no elections.

