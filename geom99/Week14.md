# Week 14 Log
### Summary

Description: Completing final website, last minute fixes to power automate flow, final exam solution worklog.

Date: April 8, 2024

Total Time: 4hr 20 mins

Reference Links: https://support.esri.com/en-us/knowledge-base/how-to-reformat-the-arcgis-survey123-date-and-time-ques-000023954

### Steps:
- [x] Fix issues in Power Automate workflow [30 mins]
- [x] Work on Website [150 mins]
- [x] Complete a bunch of surveys to populate excel doc [20 mins]
- [x] Work on final exam solution [60 mins]

## Fix issues in Power Automate workflow [04/08/24 30 mins]

* My Power Automate flow was running well, except I had an issue with the way the date was showing up in the excel spreadsheet after its brought over as a feature attribute from the survey.
* This is a particularly important issue, since it will play a role in the report automation workflow that my team is also working on.
* This is how the date was showing up:
![image](https://github.com/lowylori/technicallogs/assets/49323685/86524396-ec2f-48bd-88ff-f3be4204b5bd)

* I need to check my survey to set the datatype as ESRI date (focusing on getting the date, as its more prioirity than time. However, both are relevant.
* Open Survey123 Connect and click on the survey
* select XLS Form to open up the excel spreadsheet
* I cahnged the type to be 'date' and set the esri field type to 'esriFieldTypeDateOnly'
![image](https://github.com/lowylori/technicallogs/assets/49323685/cc4f9d9f-0dd7-4e87-837a-0388d2f3e7d1)


* Republished the survey with my changes

* Opened Power Automate and re-ran my flow, but it gave me an error that it was expecting a type int for Date and instead got type string.
* I concluded that I should try the esri field type 'esriFieldTypeDate' instead.
* Opened Survey123 and switched the field type and republished the survey
![image](https://github.com/lowylori/technicallogs/assets/49323685/5c2c0fab-69dc-48c0-85bc-4f1a9fe0b119)

* Went back to the flow and it was still giving me the same error, and thinking I probably broke it, I recreated my workflow and saved as a new one.
* Ran the flow with the new field type, but still got the same result with the date showing up as a strange long interger- I also discovered an issue with this workflow.
  * The issue I found is that when an image isn't attached in a survey submission, the workflow fails because of the 'for each' loop thats generated to access the attachment URL for the survey
  ![image](https://github.com/lowylori/technicallogs/assets/49323685/eb3bb62f-b707-4f88-931c-05c5f9200115)

* As this is the only way that I know of, currently, to include the attachment url, it means I might have to make it a required question in the survey rather than optional
* I found an article that explains that Survey123 stores date and time in 'Epoch time' ie the number of seconds that occured since Jan 1, 1970, it needs to be converted to our time zone (although we will use a different timezone for the final solution for the client)
* After creating a new simple workflow, just checking for a high priority survey, I added a new action that occurs after a survey response is submitted
![image](https://github.com/lowylori/technicallogs/assets/49323685/6e45e424-9f1d-438b-97b0-d8cca50a31c4)


* the 'convert time zone' action uses a custom function uses the method 'addSeconds' with the arguments being Jan 1, 1970 and a reference to the survey resonse trigger using the name of the date field in the survey. See below:
  *  addSeconds('1970-1-1', Div(triggerBody()?['feature']?['attributes']?['reqDate'],1000))
* I entered the Source time zone as UTC Coordinated Universal time, Destination Times Zone and UTC Eastern time and set the time usit to short date pattern.

* Tested the workflow by submitting a survey response and got a real date

![image](https://github.com/lowylori/technicallogs/assets/49323685/49929106-c94e-4e6c-8de7-0ba3cb0eb1fc)

* Now that we know the date works, its a simple process to get the date and time (change in survey123) and use a date/time option for the set time unit in the convert time zone action.

## Work on Website [04/11/24 150 mins]

* Populated content in our thingswetried.html page

![image](https://github.com/lowylori/technicallogs/assets/49323685/dbb95b6c-6c44-4540-9bca-591bb60a0ba1)
![image](https://github.com/lowylori/technicallogs/assets/49323685/764d950b-d33a-401c-b136-02ee5e71f516)

* uploaded the images to the assets folder and added in the image tags for the page.

* Added content into our integratedmethod.html page
![image](https://github.com/lowylori/technicallogs/assets/49323685/cd4f0c2b-20f4-418b-b35a-20fac4275d5e)

* Added content to integratedsolution.html page

![image](https://github.com/lowylori/technicallogs/assets/49323685/3a81b5e4-4de4-480f-a688-684b9bbfe2bc)
![image](https://github.com/lowylori/technicallogs/assets/49323685/3a775d7e-24b6-4b6b-95f0-e6ecbcca6a96)
![image](https://github.com/lowylori/technicallogs/assets/49323685/369452d7-623f-4ed7-af3d-738320a63109)

* Spell checked website, using spell checker extension on VS code
* checked for css, html and javascript errors on the site
* got stuck fixing a particular html error, with the nested <ol> lists on the integrated solution page. We wanted to have a paragraph describing each list item below the list. there were a couple solutions we come up with, since <p> is not a child element of <ol>.
 * one option was to switch to a desciption list <dl> which allows you to write a descriptions for each point, however, you have to manually write the numbers for the list (ie 1., 2., etc)
 * another option was to use <br> within the list to break to the next line for a desription.
 * We ended up going with both solutions for two seperate parts, and then got an error for having <ol> as a child element of <ol>. This was silly and stumpted me for a while bc I knew that I should be able to nest lists. Finally realized that the nested ol needs to be inside and li element
This was how I was doing it: (look at code view)
<ol>
 <li>list item</li>
 <ol>
  <li>nested list item</li>
 </ol>
</ol>

But it should be like this:
<ol>
 <li>list item</li>
 <li>
  <ol>
   <li>nested list item</li>
  </ol
 </li>
</ol>

* we were up until about 2am fixing footer issues, where the page doesn't have enough content for the footer to sit at the bottom for a really large screen. To solve this we added a media query for large screens and increased the padding for the main content area to push the footer down. This was done for the 'thingswetried.html' page.
* centered images, checked out the size of images and how it looked with our formatting and resized and reuploaded on a trail and error basis - as they were screenshots and not a consistant size.
* general final touches on the website like responsive images, editing text, minor css changes. Double checked css doc for proper format and made sure we commented what we were doing with each selector.


## Complete a bunch of surveys to populate excel doc [04/11/24 20 mins]

Populated several surveys on survey123 with various responses to test the Power Automate workflow and populate the excel spreadsheet for report generating. 

## Work on final exam solution [04/12/24-04/15/24 60 mins]

### Understanding the project requirements:
* Issue: currently real estate agents need an easier/less expensive way to access surveyed boundries (parcel polygons) within administered by a local gov
* solution should not cost more than 36k to run and maintain
* local gov currently uses QGIS as a destop software but is open to commercial products
* no server infrastructure -> means that the server will have to be on cloud
* only support windows desktop machines
* Basemap
  * Aerial imagery
* Operational Layers:
  * there are about 4,000 parcel polygon records
    * these need to be updated weekly
  * Roads, Parks & address points
    * Update every 2 months
* If there are any monthly/yearly costs associated with the solution, the realestate agents will have to pay
 * If realestate agents must pay, the data needs to be secured with authentification to access.

### Design:

Web Tier:
* Idea: a cutom web application created using leaflet javascript API, users need to sign in to access the web application data. End users can view the map and select the area they would like to download and export it as subset of the map (PDF?, JPEG?, PNG?)
* Map contains an aerial basemap with the parcels, roads, parks and address point operational layers that can be toggled on/off.
* Seach feature to allow real estate agents to find parel by address point 

Middle Tier:
* This is where expense will incur... we need a server to serve the layers to the web tier, however, the local government does not have the infrastructure to support a server. This means we will need to host the server on the cloud, which involves using a virtual machine that will cost $$.

Data Tier:
* we know we have multiple various vector based shape files that need to be accessed from a middle tier to serve to the web tier. We want a free geospatial DB, that is compatible with the chosen middle tier solution.

Desktop software:
* We know they currently use QGIS and they don't have any GIS experts, so the process from getting the data from QGIS onto a database and published to a server needs to relatively simple.

Final solution: https://docs.qgiscloud.com/en/#

Middle tier took the most amount of thought b/c this is where we can control the expense of maintaining the solution. Ultimately it also dictated what spatial DB i could use and how the web tier will connect. I explored ArcGIS Server (too expensive) and Geoserver hosted on Amazon cloud service (geoserver is free but ur paying for cloud). However, the most streamlined solution was using QGIS cloud pro. Heres why:

* The local government is already using QGIS, and are likely familiar with some of its basic functionality
* data managment - the cloud provides a PostgresSQL db expended with PostGIS spatial component. Can have multiple databases and can be managed with pgAdmin or even within QGIS DB manager
  * The workflow is simple for brining the data into the db. It can be done directly in QGIS. Get the data from your pc > QGIS cloud postgres db by using the QGIS Cloud plugin. Usinging load data tab,  select the local layers you want to upload. can edit the db schema as desired.
  * limitation: pro comes with 500 mb of storage - additional storage is available though from 20 eu a month for 1 gb = 1.5gb. Should be more than enough for the needs of this project, as it is just shp files.
* Web maps/Web services
  * create webmaps within qgis desktop and publish to the qgis cloud server easily
  * maps and data can be shared using ogc compatible web services. WMS, WFS.
* Cusomizable web client application that allows you to print maps from the web app. Print layouts can be pre-created. also there is security in the qgis cloud pro which would require users to sign in to access the web application via a qgis cloud free account.

Here is a breakdown of the components:

Web tier: 
* Using QGIS Cloud web client which allows you to view a webmap with the layers published to the QGIS cloud.
* Features:
  * Turn off/on map layers
  * adjust extent
  * adjust transparency of a payer
  * seach - defined custom SQL search queries that can be configued to use in the web cient ie. we can use the address shape file to define a search query for real estate agents to quickly locate a parcel.
  * printing map layouts - the pring layouts created is QGIS projects are available in the web map as well. These can be manually set up in QGIS to get an offical local goverment look.
    * Then, using the print fuction within the web client, you can select an extent and pring using the pregenerated layout
  * ability to use either google or bing sateillite base maps - although you may not use google in a print map (copyright)
  * ability to adjust the appearence for the web client using CSS logic
  * access security - because this will solution will not be free to maintain, real estate offices will need to register for accounts and pay an annual fee. BC this solution will cost somewhere btwn 1140-1488/yr, an annual fee of about $30 from 50 offices will cover them. Thats pretty cheap
  * 

