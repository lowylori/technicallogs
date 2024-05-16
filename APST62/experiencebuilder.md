# AGOL Experience Builder
### Summary

Description: Using AGOL Solution for Parks and Grounds Request Manager, Reverse engineer the Experience builder app.

Date: May 16, 2024

Total Time:

Reference Links:

### Steps:
- [x] Create and make file structure of Web Experience [10 mins]
- [x] Configure Home page
- [x] Configure Assignments Page
- [ ] Configure Monitor Page
- [ ] Embed crowdsorce app to the Manage page

## Create and make file structure of Web Experience [05/16/24 10 mins]

* Sign into AGOL
* In apps, choose Experience Builder
* In the top right corner, select create new
* choose a blank template and get started
* Rename the main page to 'home'

<img width="310" alt="Screenshot 2024-05-16 at 10 24 13 AM" src="https://github.com/lowylori/technicallogs/assets/49323685/abbce333-2da4-4fdb-bc06-afead2743c2a">

* Add a folder for Called requests and create 2 files within it: Manage and Monitor
* Create another file outside the folder called Assignments

<img width="311" alt="Screenshot 2024-05-16 at 10 29 37 AM" src="https://github.com/lowylori/technicallogs/assets/49323685/8c0e236f-aa84-4910-9077-73ae38902742">

  
* The Manage page is a crowdsource app that will be linked to on this page.
* the Monitor page links to a dashboard
* The assignment page links to workforce
* Use the 3 dots in the right corner to save as. Fill out the metadata and name.

<img width="934" alt="Screenshot 2024-05-16 at 10 30 53 AM" src="https://github.com/lowylori/technicallogs/assets/49323685/9a8eb805-5488-42cf-9578-307e5656fe84">


## Configure Home Page [05/16/24 20 mins]

* Select the home pg
* Enable the header by turning it on, set colour (#ded9cc) and height (50px)
  
<img width="263" alt="Screenshot 2024-05-16 at 10 40 44 AM" src="https://github.com/lowylori/technicallogs/assets/49323685/b208f4d7-e742-4add-b171-713b9c140688">

* Hover over the header and click 'edit header'
* search for the menu widget and drag it over

<img width="887" alt="Screenshot 2024-05-16 at 10 45 38 AM" src="https://github.com/lowylori/technicallogs/assets/49323685/75472da3-743a-4493-9056-304a2983ea65">

* Drop in in the top right of the header and configure the settings. Use the pill syle and set the 'selected' setting to colour #B82234

<img width="1023" alt="Screenshot 2024-05-16 at 10 50 02 AM" src="https://github.com/lowylori/technicallogs/assets/49323685/b1ed0d27-ef6e-44df-a823-45b4da678e98">

* Set a background image: insert widget> page element> image> resize to screen. Upload image from local.
  
<img width="1416" alt="Screenshot 2024-05-16 at 10 59 38 AM" src="https://github.com/lowylori/technicallogs/assets/49323685/22cda29d-0324-473c-a985-8595ff0c2a22">

* Add a fixed pannel from widgets, align center
* From widgets, create 2 text boxes within the pannel. Connect data later
<img width="1311" alt="Screenshot 2024-05-16 at 11 51 28 AM" src="https://github.com/lowylori/technicallogs/assets/49323685/f7e32cc4-cd6a-48ab-9b48-e1b5a93b314f">

* Had to go back to survey and add a hidden question 'status' and set default value to 'Submitted'
* now we can connect open requests to the survey results hosted feature layer (I'm not 100% sure if I should have created another feature layer from the survey here)
* On the right pannel with the Open Requests text box selected, turn on connect to data
* Choose select data and find your hosted feat layer

<img width="519" alt="Screenshot 2024-05-16 at 2 00 30 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/32f1f0d3-da36-4a75-a0f2-f21ec0534543">

* Choose to create a new view and set a filter to be be where the field 'Status' is 'Submitted'. Click apply changes

<img width="825" alt="Screenshot 2024-05-16 at 2 01 10 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/357e60b7-25c9-4e9b-824f-c0a12013b417">

* Now highlight the # sign above open requests and click the dynamic content button (looks like a DB). Under statistics connect the data, use the count operator on the field ObjID

<img width="582" alt="Screenshot 2024-05-16 at 2 03 25 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/1c57535a-4b39-4e5c-aab8-1a5d1ee7ee48">

* It will now update with the count of open requests (pretty cool!):

<img width="355" alt="Screenshot 2024-05-16 at 2 05 29 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/442cbe96-ffb9-4448-9f17-e93e6fb0776e">

* Now for unassigned Work, lets connect the data to the workforce project web map, choose the assignments layer

<img width="519" alt="Screenshot 2024-05-16 at 3 20 50 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/328e5b4a-fcdd-40ed-8a58-7e1b408caac1">

* Click the dropdown open create new view and open up the window. Label it Unassigned Assignments. Set the filter to be Status is Unassigned
  
<img width="969" alt="Screenshot 2024-05-16 at 3 24 32 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/8ebfb8bc-2845-4f77-a867-fd96281051a4">

* Set the dynamic content like in the previous one
<img width="518" alt="Screenshot 2024-05-16 at 3 30 16 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/b445afdf-5f7e-4af7-a69b-df2d175e2f9b">

* Last but not least, lets link to the manage requests and create assignments pages
* Highlight the text, then use the text format box in the right panel to connect a hyper link to another page

<img width="1320" alt="Screenshot 2024-05-16 at 3 35 53 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/16bc65fd-768b-4897-9456-5d823319bb46">

## Configure Assignment Page [05/16/24 10 mins]

* Create a new workforce Project
* Configure to requirements
* Open the workforce create assignment page
* copy url
* In experience builder, open the assignments page
* enable header
* Under widgets, locate 'embed', drag it onto the page
* resize to fit the screen. 
* paste the url to embed the assignment page
* That was an easy one :)
  
<img width="1164" alt="Screenshot 2024-05-16 at 3 09 20 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/3c78fceb-792c-4a51-9953-9eb1ac9ef57c">

## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc
