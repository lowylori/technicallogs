# Title of Log
### Summary

Description: Finalize solution options. Modify survey to meet business needs, try using microsoft flow to automate excel spreadsheets. 
Explore 'made' software, similar to flow, determine which is easier to use for the client.


Date: Mar 25, 2024

Total Time: 3 hrs

Reference Links:

### Steps:
- [x] Update Survey on Survey 123 [30 mins]
- [ ] Microsoft Flow Automation Engine
- [ ] step 3
- [ ] step 4

## Task num Update Survey on Survey 123 [03/28/24 30 mins]

After working with the Survey123 webhook for microsoft flow, I realized that certain features may be more accessible depending on the datatype. I want to be able to extract the lat and long from the locaation point. With the location saved as an esripointz type, I cannot access it using flow. Additionally I want to allow for photo attachments.

* Current survey:

![image](https://github.com/lowylori/technicallogs/assets/49323685/5b7e4272-244a-490a-bc44-b45db9a5e55b)

### Modify the survey

* Open survey in Survery123 Connect
* modify the XLS Form to do the following
  * capture x, y, z of the geopoint in seperate columns to allow the data to be accessed by variable in Flow
  * created an image attachment field
  * changed the dataype for priority level to be an esriFieldTypeInterger, instead of string (previous mistake)
  * set 'General Inspection' to be the default value for reqType for language barriers in the event that the individual skips the question
![image](https://github.com/lowylori/technicallogs/assets/49323685/285b19ed-1848-4e8a-ac87-1664f0b87c62)

* Republish the form

### Test out the survey
* check out the survey in AGOL, open it in a browser window

![image](https://github.com/lowylori/technicallogs/assets/49323685/2aec6b55-a2de-4024-b2b5-20ac6241b1b8)

* submit the survey and go back to AGOL and find the Survey123 app. Open your survey and check out the data tab
* we can see that the x, y, and z are now being stored in separate fields.
![image](https://github.com/lowylori/technicallogs/assets/49323685/08214c2d-47e1-4683-b857-988bf41e8fd9)


## Microsoft Flow Power Automation [03/28/24 60 mins]

* Sign into your Microsoft 265 account, open app Microsoft Power Automate
* create new flow, give it a name, and set the trigger to Survey123: when a survey response is submitted
* connect to your AGOL account if not already connected. Sect the survey you want to use.
![image](https://github.com/lowylori/technicallogs/assets/49323685/5ead91a5-0934-404b-96fc-6550a3bfa34a)

* Click the pluss button to add an action, choose control> condition
![image](https://github.com/lowylori/technicallogs/assets/49323685/8428ea99-bd4b-4172-8139-e36951e9b82d)

* use the option to enter data from the previous step (survey) to populate the condition. The condition chosen was when priority level is set to 1
![image](https://github.com/lowylori/technicallogs/assets/49323685/136d0bee-26de-40cd-9829-6a71b56123a1)

* Add another condition for when the previous control evaluates to false, priority = 2
![image](https://github.com/lowylori/technicallogs/assets/49323685/006d64a4-5688-4527-b5ad-51e9af1a22df)

* follow the same steps above to add one last condition when the previous evaluates to false, and the new condition is when priority = 3. It should look like this:
![image](https://github.com/lowylori/technicallogs/assets/49323685/140739cd-cd1a-4d93-86df-8fb73ac73063)

* rename conditions for added clarity.
* for the first condition, lets set what happens when it evaluates to true
* click to add an action and evaluate the options using excel
![image](https://github.com/lowylori/technicallogs/assets/49323685/f7b233d0-4e9b-4e7e-a78b-ef5f31da7c94)

* Lets go outside of this application and create an online worksheet in excel to use for this automation.
* Create a new Workbook and add 3 sheets, rename sheets: High, Medium, Low. Give the worksheet a name and create headers.
![image](https://github.com/lowylori/technicallogs/assets/49323685/2cbc54c0-ba18-4630-bafc-d2db534477c3)



## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc
