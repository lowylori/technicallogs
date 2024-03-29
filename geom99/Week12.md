# Title of Log
### Summary

Description: Finalize solution options. Modify survey to meet business needs, try using microsoft flow to automate excel spreadsheets. 
Explore 'made' software, similar to flow, determine which is easier to use for the client.


Date: Mar 25, 2024

Total Time: 3 hrs

Reference Links:

### Steps:
- [x] Update Survey on Survey 123 [30 mins]
- [ ] Microsoft Flow Automation Engine [120 mins]
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


## Microsoft Flow Power Automation [03/28/24 120 mins]

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

* Back to Power Automate, in add an action for the first condition, choose 'Get worksheet' for Excel Onedrive

> [!WARNING]  
> You might need permissiongs from admin to make a connection to a workbook if you are using an organizational account. Admin permission was required for me, so I switched to my personal account and recreated the excel document
> ![image](https://github.com/lowylori/technicallogs/assets/49323685/0770b654-56a9-477c-a2ce-dffaa554446d)

* After recreating the excel document on my personal account, I was able to add it as a connection.
![image](https://github.com/lowylori/technicallogs/assets/49323685/62405662-4fdb-4a4e-8672-4ab69c705e99)

* Lets add a new action after you get the worksheet.
* Go into the Excel (onedrive) options and choose add row into a table

> [!NOTE]  
> Side note, I relalized you need a named 'table' to add a row to rather than a sheet name, so I went back to the excel spreadsheet and added table names for each of the sheets

 * In add row to table, select the workbook, table name and under advance parameters select the fields you want to populate with the survey data. Populate the fields with the corresponding data from the feature attributes of the survey.
![image](https://github.com/lowylori/technicallogs/assets/49323685/346d00c5-ff2e-42c4-a97f-c35b223833d9)

> [!NOTE]  
> Unable to access the date metadata, so I will have to go back and add that as a field in the survey later.

* save the sheet and lets test out high priority by making a survey submission. Click the little test tube button top right. Complete the survey with a high priority request.
![image](https://github.com/lowylori/technicallogs/assets/49323685/17c61a28-5e31-457e-9460-7aa6a3dc7b24)

* We can see the survery fell into the right conditions, hopefully it worked. Time to check the excel sheet. Looks like nothing was added :(
![image](https://github.com/lowylori/technicallogs/assets/49323685/3cec7942-035e-491e-bb7e-042acace12a0)

* Go back to Flow and see what went wrong. You can view the raw outputs to see if anything went wrong. Looking at the body section, it does look like all the data from the survey was correctly accessed. Lets check the settings.
![image](https://github.com/lowylori/technicallogs/assets/49323685/58753a03-b0a6-435b-9dc9-46d124bb9a6a)

* There doesn't seem to be ant issues. Lets try creating the medium priority level differently. We can use the update a row instead.
* Nevermind, update a row only lets you update one column at a time. I think perhaps the issues is that I had the other two conditions empty (incomplete) when I started testing?
* Lets delete the condition for low priority and build out two. I'm gonna leave out the 'get worksheets' option, because it seems that step isn't necessary.
* Set up add a row, same as before, but use table 'Medium'
![image](https://github.com/lowylori/technicallogs/assets/49323685/1efc2240-1109-4d91-966f-1273d69b3cb5)

* When attempting to save, I got an error for having duplicate names for triggers and action names. Went in and renamed everything...
![image](https://github.com/lowylori/technicallogs/assets/49323685/513cb725-f900-45c7-a74f-c58d1125e811)

* I got another weird error when I tried to save again that didnt really make sense. Since the 'For each 2a and 2b' mentioned in the error were the names of the loops I created for medium priority, I decided to delete those. After deleting it still gives me the same error. A tragic flaw of this system is that if there is an error, you are unable to save.
![image](https://github.com/lowylori/technicallogs/assets/49323685/9d7f72c4-ad64-4672-8c69-86fc24811200)

* Checked out the parameters for add row into a table high and realized there were some attributes I left blank accidentially. Apparently Flow doesn't like that. Added the values and flow was able to save successfully. I will try to test it again.
* Completed a survey and went to check the results

![image](https://github.com/lowylori/technicallogs/assets/49323685/5a7aa25c-8c26-4e28-9b21-3bcc0e5170c7)

* The message was that the branching conditions failed, and it does show that the prority = 1 condition evaluated to false. Checking the survey data however, shows the priority was set to 1.
![image](https://github.com/lowylori/technicallogs/assets/49323685/667c8e9c-5e0c-41a9-bb5b-e9396e437dd8)

* Lets  start fresh with a very simple flow. I think the issue might have something to do with using the dynamic data for meta information (ie attachment url and response ID), because these options seem to add a for each loop automatically when they are selected. I'm not sure why, but it might mean that i need to go back to my survey and make some more changes
* Lets do a new flow, when a survey response is submitted > select survey
* After its submitted we want to automatically add a row into a table. I set only 4 parameters.
![image](https://github.com/lowylori/technicallogs/assets/49323685/6ca62775-666a-420f-bc51-83ff32aa5ce4)

* Test says it ran successfully... turns out that the were all running fine, they were just being added in a random location on the excel file
![image](https://github.com/lowylori/technicallogs/assets/49323685/57d2ff95-b64e-4ba6-b1b0-2f021ec2ab45)

* I will have to investigate further on why that happened. It might have something to do with the way I formated the document




## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc
