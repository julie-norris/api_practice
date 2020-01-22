from Flask import Flask, request, render_template, session, redirect 
import requests, json

app=Flask(__name__)



"""You are building a web application that can tell people what elections they have coming up based on their address. It is similar to the kinds of things you'd be working on at Democracy Works and uses one of our APIs.



When someone visits the site you create, they will be presented with an address form. """


@app.route('/')
def index():
    """Homepage"""

    return render_template("address_form.html")



"""When the user submits the form, your code will translate the address into some OCD-IDs"""


@app.route('/search', methods=['POST'])
def find_user_OCDID():
    """Translates the address submitted into OCD-IDs"""

    """setting information submitted from user to variable names"""
    street = request.form["street"]
    street2 = request.form["street-2"]
    city = request.form["city"]
    state = request.form["state"]
    zipcode = request.form["zip"]
    
    """verifying that the zip code is a 5 or 9 digit numeric entry"""
    match = re.match(r'^[0-9 -]{5,9}$', zipcode)

    if not match:
        flash("Invalid zipcode. Try again.")
        return redirect("/search")


def find_upcoming_elections(city, state):
     """translate the address into some OCD-IDs"""

    ocd-division-state="ocd-division/country:us/state:"+ state.lower()
    ocd-division-place= ocd-division-state + "/place:" + city.lower()


    """Query the Democracy Works Elections API for upcoming elections for those OCD-IDs"""
    payload={'district-divisions':[ocd-division-state, ocd-division-place]}
    headers = {"Content-Type": "application/json"}
    url = "https://api.turbovote.org/elections/upcoming?"
    response = requests.get(url, params=payload, headers=headers)
    r=response.json()
    

"""Returned elections are displayed to the user
The results are formatted for the user"""
@app.route('/election_results', methods=['GET'])
def display_upcoming_elections():

	return render_template(election_results.html, elections=r)



if __name__ == '__main__':
	app.run(debug=True)