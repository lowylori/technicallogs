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
- [ ] Work on final exam solution [60 mins]

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
This was how I was doing it:
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

## Work on final exam solution [03/12/24 60 mins]



