# Week 11 Log
### Summary

Description: Exploring some open source solutions, survey123 and task management with microsoft.

Date: Mar 20/24

Total Time: 3 hrs

Reference Links: 
https://leafletjs.com/examples/quick-start/
https://www.esri.com/arcgis-blog/products/survey123/field-mobility/survey123-microsoft-flow/

### Steps:
- [x] KoboToolbox [30 mins]
- [x] Leaflet Javascript API [45 mins]
- [x] Creating a survey on survey123 [20 mins]
- [X] Task Managment Solutions and automation [80 mins]


## KoboToolbox [03/21/24 30 mins]
An alternative to Survey123. Advertized as open source, however they do offer a free community plan for educational institutions and also paid plans.
<img width="1070" alt="Screenshot 2024-03-21 at 12 44 40 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/554d3fe9-e62f-4982-9b6c-9c32d9e4bed1">

* Create an account on KoboToolBox
* Confirm through email
* Create first project
<img width="840" alt="Screenshot 2024-03-21 at 12 38 02 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/04cba9e5-7253-4c61-be05-30c1833837e1">
* Create a survey form with custom questions
<img width="1075" alt="Screenshot 2024-03-21 at 12 43 18 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/45fc32c9-5c20-4815-919d-867aca5d2cbe">

* You can preview the form and save when you are satisfied
<img width="869" alt="Screenshot 2024-03-21 at 12 45 50 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/26d48909-894b-4ee9-bd4c-809b2a50d38e">
* From the home menu, deploy the form to make it public
<img width="1082" alt="Screenshot 2024-03-21 at 12 46 42 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/057ae9d1-c753-4abd-ad38-ff04d0b84a55">

* You can also manage different language options for your form.
<img width="561" alt="Screenshot 2024-03-21 at 12 47 21 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/f36046a2-2070-45f0-826f-0822159f937e">

* Within you project, go into settings, select the option on the left panel for sharing. You can share this with stakeholders to make modifications to the survey and manage it.
<img width="820" alt="Screenshot 2024-03-21 at 12 49 23 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/db72bbb4-129f-4d31-98c5-a4f8a3a020fa">

* Within settings there is an option to use rest services to post submissions to a thrid party application.
<img width="819" alt="Screenshot 2024-03-21 at 12 50 56 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/16a67244-b3cc-4123-a03d-27f6438a7405">

* Try out the survey as a user
* From the Form page, click copy and paste it into a new window. Alternatively, you can click open.
<img width="896" alt="Screenshot 2024-03-21 at 12 55 41 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/7671bef5-3a1e-46f9-86f3-ca528ab80c58">

* complete the survey and submit.
* There is now one submitted survey. Open the data tab in KoboToolbox
* There are multiple ways to view your data: Table, Reports, Gallery, Download and Map.
* Table is a typical table view.
* You can create custom reports. The options are very basic. Pretty much select what questions on the survey you want to include in the report.
<img width="380" alt="Screenshot 2024-03-21 at 1 00 12 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/4a238a75-769f-4e2d-9934-8b922ba24f99">

* You can also change the report style.
<img width="478" alt="Screenshot 2024-03-21 at 1 02 16 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/bc1626f8-c028-4aea-b03b-81ee33728ad8">

* Gallery is a collection of uploaded images from submitted surveys.
* From the download section you can choose an export file type and configure advanced options.
<img width="685" alt="Screenshot 2024-03-21 at 1 03 04 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/85a49c0c-ffa4-47ae-8516-c12adb131b4f">

* In map, you can change the basemap (4 options), whether to display as points or heat map, and you can customize the marker colors. You can also add an overlay file, which is added as a layer to display on the map.
<img width="949" alt="Screenshot 2024-03-21 at 1 05 27 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/b8d23345-3b01-45f7-8b9f-5a02c451172c">


## Leaflet - Web Tier [03/21/24 45 mins]

* Created github repo 'lowylori/leaflet'
* Create a new file called 'samplemap.html'
* set up doctype html
* In the head section, link to leaflet css file and the leaflet JS file.
* Create a div to hold the map
* style the map div to have a set height
![image](https://github.com/lowylori/technicallogs/assets/49323685/3e75a75c-76c7-4345-be90-66849778b2a7)



* make a script tag below the map div
* initate the map and set the center point and zoom level
![image](https://github.com/lowylori/technicallogs/assets/49323685/1ddd5ec6-2b7b-405e-860d-f27844161116)

* add a open streets map tile layer to the map
![image](https://github.com/lowylori/technicallogs/assets/49323685/847e4adb-aeb4-4be4-8cc7-637c5364e1e0)

* Check out your layer by going to the github page
![image](https://github.com/lowylori/technicallogs/assets/49323685/d463ff59-1b0b-4bd9-8d5c-0f37f79b8851)

* Make a copy of the html sample map. Use it for the next example to add markers.

### Add Marker
* I made some small changes first to the set up of the sample map. I configured the map options seperately and changed the center location to Southern Africa Wildlife College.
* I used those map options to initalize the map
![image](https://github.com/lowylori/technicallogs/assets/49323685/b0b7e70c-34ed-46e9-a9a0-316531e7fa89)

* I also made the layer set up more clear. First created a new osm tile layer then added it to the map. Now ready to add the marker.
* Create a new marker with location and add to the map.
![image](https://github.com/lowylori/technicallogs/assets/49323685/d4c2f235-0b80-43eb-94e1-0a2bd179e6b8)

* Check out your map
![image](https://github.com/lowylori/technicallogs/assets/49323685/4e070818-7829-4994-99f6-47d3a134be12)

* Decide if you like it. I'm not a fan of this tile layer for this area. I'm going to change mine
![image](https://github.com/lowylori/technicallogs/assets/49323685/69a71536-9d1c-4dd5-9c24-de4a56a60d2d)

* New tile layer
![image](https://github.com/lowylori/technicallogs/assets/49323685/b8d89447-b25b-43f1-ab78-a6d00fc790ab)

* Customization of marker settings: using the var markerOptions, you can set a title, whether the marker is clickable and draggable, additionally you can add a custom marker icon.
* You can bind a popup to a marker. Now when you click on the marker, a message will pop up. Adding the title attribute to the markerOptions setting will give a message when you hover over the point.
![image](https://github.com/lowylori/technicallogs/assets/49323685/513a1f8e-afc1-4b93-a73f-0cf9db4aa906)


## Creating a survey on Survey123 Connect [03/21/24 20mins]

Need to create a survey for the next tast (task managment with microsoft flow)
* Install survey123 connect, if you don't already have it on your desktop.
* Sign into your organization account.
* Click create new survey in the top left corner
* Set a title and choose a template. Click create survey
![image](https://github.com/lowylori/technicallogs/assets/49323685/d4d8fe7f-36a2-4cdb-b7b9-2285d799b551)

* An Excel spredsheet and preview will open up in survey123
* Use the spreadsheet to create survey questions using the type, name and label column. Set any additional fields that you find necessary, ie 
![image](https://github.com/lowylori/technicallogs/assets/49323685/075a3cc4-a67e-4b9b-94f0-222f1efda144)

* This survey can be modified further to include more info such as contact, attachment etc.
* Click publish on the left panel
![image](https://github.com/lowylori/technicallogs/assets/49323685/4f409aec-ccb3-4ac0-a9f9-a51a56eacf54)


## Task Management Solutions [03/21/24 80mins]

* Need to explore alternatives to Workforce. Looking for a task managment system thats easy to use, possibly free with many users, can maybe connect with the AGOL ecosystem (although not a requirement)

### Tasks by Planner and To Do (Application in Microsoft Teams)
* Sign into Teams on your Application
* Select the apps option in the left panel
* Search for 'tasks by planner and to do'
* Click add
* Open up the application within teams. Along the left pannel, there are several options. 
<img width="650" alt="Screenshot 2024-03-21 at 8 21 56 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/c276e29d-2360-4b49-a029-232b9a526476">

* In the Assigned to me option, select 'Create a list'
* Input a name and choose where to create in. You have the option to select a premade team.
* if you want to be able to assign tasks to others, you have to use a team.
* Click Create
* Once you create the list, you can start creating tasks and assigning it to members of the team

<img width="804" alt="Screenshot 2024-03-21 at 8 41 04 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/11dd2422-4c12-4ec8-91da-e5ffd426ab0e">

* You can click the task to configure more options such as importance, label, progress, start date, due date, a checklist, attachment and comments. You can also assign a task to multiple people.
<img width="771" alt="Screenshot 2024-03-21 at 8 42 22 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/96dff346-6f76-43bd-a343-3ff443fb5167">

* Once tasks are created you can view them as a list, board, chart or schedule. 
<img width="1048" alt="Screenshot 2024-03-21 at 8 50 02 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/7b804dac-4106-473d-bddb-f985d19d7cdb">

* Board View
<img width="837" alt="Screenshot 2024-03-21 at 8 51 07 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/834a226e-d2b0-4262-85e8-61a08e0a0938">

* Chart View
<img width="829" alt="Screenshot 2024-03-21 at 8 56 25 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/ef42b386-7f10-4a0f-a4dd-3988b36b237e">

### Flow (Microsoft 365)

Flow enables you to generate a customized workflow. Connects to Survey123. There is an option for email connectors based on set conditions. IE. IF priority level = high, send email.

* Sign into your Microsoft 365 account
* In apps, search for Flow
* Select new flow, and choose 'automate cloud flow'
<img width="925" alt="Screenshot 2024-03-21 at 9 19 24 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/c89f680c-b84f-45ef-bf06-0c8bf2b425f3">

* Enter a name and choose the flow's trigger to be 'Survey123', when a survey response is submitted.
<img width="902" alt="Screenshot 2024-03-21 at 9 20 15 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/8db08fab-bedf-4b8b-b8c1-e545151aa5d8">

* You have to sign into your AGOL account to use this flow. You will be prompted to connect to AGOL and allow access.
* Once its connected, you can configure the parameters. You can decide what info is included and choose your premade survey stored in your AGOL account using survey123. Collapse the panel when you've completed the parameters.
<img width="589" alt="Screenshot 2024-03-21 at 9 22 15 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/391fdc68-ec69-45c7-81aa-8960caf0c071">

* Now you can add conditions and logic
* This step will depend on the configuration of your survey. I had to go back, because my survey didn't have a priority level and I wanted to configure that.
* I set a condition based off the response on priority level = high
<img width="621" alt="Screenshot 2024-03-21 at 10 51 29 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/a05de207-c8eb-4869-aeea-7fae6baa551b">

* If this condition evaluates to True, then it will create a task.
<img width="647" alt="Screenshot 2024-03-21 at 10 52 38 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/27c121da-5e07-4ae7-8e9d-f88833c6ecd5">

* There are a lot more planner options you can use from this interface. For the sake of testing, I kept this flow very simple. I plan to build on it later.
<img width="597" alt="Screenshot 2024-03-21 at 10 54 18 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/87ea6e91-c93a-4558-816e-fefd782650bc">

* Hit save at the bottom of the page. Now that its set up, we can test it.
* Click the test button in the top right corner, select manual test.
* Open survey123, and complete the survey with the priority level set to high.
* switch back to Flow and check the result.
* Test ran successfully
<img width="1186" alt="Screenshot 2024-03-21 at 10 58 49 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/52056785-e93f-477a-8af4-ba9440f66c1f">

* Although it says that test was successful, more testing is required.

