# Week 14 Log
### Summary

Description:

Date: April 8, 2024

Total Time:

Reference Links: https://support.esri.com/en-us/knowledge-base/how-to-reformat-the-arcgis-survey123-date-and-time-ques-000023954

### Steps:
- [x] Fix issues in Power Automate workflow [30 mins]
- [x] Work on Website [90 mins]
- [ ] step 3
- [ ] step 4

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

## Work on Website [04/11/24 90 mins]

* Populated content in our thingswetried.html page

![image](https://github.com/lowylori/technicallogs/assets/49323685/dbb95b6c-6c44-4540-9bca-591bb60a0ba1)
![image](https://github.com/lowylori/technicallogs/assets/49323685/764d950b-d33a-401c-b136-02ee5e71f516)

* uploaded the images to the assets folder and added in the image tags for the page.

* Added content into our integratedmethod.html page
![image](https://github.com/lowylori/technicallogs/assets/49323685/cd4f0c2b-20f4-418b-b35a-20fac4275d5e)


## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc
