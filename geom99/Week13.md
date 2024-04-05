# Week 13 Log
### Summary

Description: Exploring report generation using arcgis api for python with survey123. Trying Make software for automating excel spreadsheet workflow.

Date: April 4, 2024

Total Time: 3hrs

Reference Links: https://www.youtube.com/watch?v=dzAbLFVuWiw&t=1700s
https://github.com/Esri/Survey123-tools/blob/main/Work_with_Reports/create_reports_using_the_arcgis_api_for_python.ipynb

### Steps:
- [ ] Report generation with ArcGIS API for Python [60 mins]
- [ ] Automate workflow with Make [90 mins]
- [ ] step 3

## Report generation with ArcGIS API for Python [04/04/24 60 mins]

We want to automate report generation as a scheduled task in jupyter notebook. First we have to create the notebook that accesses the survey using the item id, choose a report template and generate as a pdf. Then we will look into the steps to make this an scheduled task.

* Sign into AGOL account
* If you don't have a pre-existing survey, you will need to create one. I will be using the Parks and Grounds Request form from the Solution.
* Find the Item in AGOL content
* CLick top right, Manage in Survey123 website
![image](https://github.com/lowylori/technicallogs/assets/49323685/a59ef697-38ff-4b6d-bb54-287050fb024f)

* Under the data tab, select the report option. A panel will open up on the right, and there is an option to select a template. * Click Manage Template
![image](https://github.com/lowylori/technicallogs/assets/49323685/2c65ab5f-3b30-4fe9-b781-598cee12e41b)

* You can download a sample template, make modifications in Microsoft word, then upload them as a new template. We can go back to this step later to format the perfect report - for now, I will just senerate a sample template summary, which will give a general overview of the most recent entries.
* This is what it looks like in word
![image](https://github.com/lowylori/technicallogs/assets/49323685/cd48e3a3-126b-4b7c-8508-fa7e0a19cbdd)
* I changed the name of the report to be 'Summary Report'

### Notebook

* Moving into Notebook create a new notebook and hit save as, give it a name.
![image](https://github.com/lowylori/technicallogs/assets/49323685/70437820-8eb2-4bed-ad90-5e13c6baf4f8)

* Import the necessary modules and connect to your GIS
* define a variable to hold survey manager which allows admins of Survey123 to access data for their surveys
* use survey manager to access your survey by item number (go to the items page of your form)
![image](https://github.com/lowylori/technicallogs/assets/49323685/29632dad-3cd0-443b-81a1-3613fe922a11)

* We want to see our available templates (to use for our report). Use the report_templates method to create a list of templates. Print the titles property of the templates. Store your template in a var.
![image](https://github.com/lowylori/technicallogs/assets/49323685/c7e5fdc9-386f-4cfc-84d1-9960ab183fe4)

* If the template has invalid syntax it will result in an error when we generate the report. As a precaution, lets check template syntax using the check_template_syntax method.
![image](https://github.com/lowylori/technicallogs/assets/49323685/d5fd4cb0-9788-44a6-ac4c-37f03b581ae4)

* This resulted in type error. Refer to documentation on this method.
  * https://developers.arcgis.com/python/api-reference/arcgis.apps.survey123.html
* it is expecting timeplate_file which is a directory path to a template file
* since Survey is a child class of item, check item properties documentation
* I tried accessing a couple different properties but wasn't able to get it... going to move on and will come back to this later.
* save
* Check how much credits this will cost using the estimate method. Print result. This will only cost .5 credits
![image](https://github.com/lowylori/technicallogs/assets/49323685/5e2cae44-c1c5-4910-86dc-71041383a5a3)

* Optionally, you can create a sample report now, which doesn't consume any credits suing the create_sample_report method, however, this can be easily done in the survey123 manager app, so I don't feel this is necessary for us.
* Now we want to generate a report, they can be generated as a docx file or pdf (using output_format param) and can be downloaded locally or saved to your organization.
* Lets save to organization, because we want to see if we are able to schedule an email notification or something of that sort with the generated report.
* You need to provide a folder id argument in order to save to your content on your account.
* Where clauses can be provided her to filter by creation date etc
![image](https://github.com/lowylori/technicallogs/assets/49323685/8006ad7f-1c4b-43d5-aa48-91560d3554f0)

* Check content in your AGOL account to confirm report was created. Option to download the docx from here.
 ![image](https://github.com/lowylori/technicallogs/assets/49323685/9ed5e6e9-7947-4cf3-bad8-cb5ae7636f46)

* Download the report and check it out.
![image](https://github.com/lowylori/technicallogs/assets/49323685/faa02f6a-2195-44ce-a0fe-8c7f9bac3303)

* I know its not that interesting since I only have one record - however, the more records, the more credits it costs. 

### Scheduling a Notebook Task

* Unfortunately, from my organizational account, I'm not able to schedule a notebook task... however, I can see if its an option from the seperate developer account that I have.
* Turns out Notebooks isn't a feature on my dev account, so I will have to come back to this task after speaking to the organizational account admin.

## Automate Workflow with Make [04/04/24 60 mins]

* Register for a free account with Make
 * https://www.make.com/en/register?
* Verify account through email
* Once you're sign signed you're taken to a home dashboard page
<img width="1125" alt="Screenshot 2024-04-04 at 10 19 01 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/51c29ca2-e710-4fc4-ab72-e429c8936d5d">

* Hit the Create new Senario button
* Start with a trigger - search for survey123, when a survey is submitted
* you have to create a webhook to connect to your AGOL account
<img width="483" alt="Screenshot 2024-04-04 at 10 23 13 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/3e4811d2-e010-4bbe-b553-4bae1c108a9d">

* Once the webhook is initated, you'll be prompted to sign in to your AGOL account
<img width="836" alt="Screenshot 2024-04-04 at 10 25 06 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/6ae694d6-b01a-4179-92ee-3df4c3cec3ad">

* Now you can select the survey you'd like to link the trigger to and select the trigger event. I chose addData
* Setting up a conditional if statement is not very intuitvie on this platform, so I spend a bit of time trying to find it. After playing around a bit with some different flow controllers I found router.
* At first I was confused with router, because when you click on it, it doesn't give you options to set conditions, it just adds another route. However, theres a little tool wrench connected to each route that allows you to add a filter
<img width="531" alt="Screenshot 2024-04-04 at 11 09 43 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/d8804250-f539-4e86-a017-7deae8c808f8">

* When you click on the wrench, you can select 'Set up a filter'
* I set a label and created a condition based off the survey response to 'Set a priority level' which could be an interger value from 1 to 3 (inclusive)
<img width="463" alt="Screenshot 2024-04-04 at 11 15 59 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/3510e06a-fbf7-4270-870a-9bd1b3ca1b74">

* Now using the resulting route, search for Excel, choose add a table row as the action.
* You need to create a connection to microsoft by signing in to your account.
* From there you can select a workbook
* Then select the worksheet and the table within the worksheet (I selected the high priority table)
<img width="459" alt="Screenshot 2024-04-04 at 11 20 53 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/21c7322d-25c6-4f3d-a9c9-74ce2607b4c1">

* I got an error saying function tableRowFields finished with an error. Not sure what that means. Switching to another sheet and I still get the same error
* Turns out it had to do with the last cell I had selected in the excel workbook. Selecting the first row on all tables, column A seems to have resolved the error.
* Spoke to soon, turns out that didn't resolve the issue. Unfortunetly the documentation for excel on Make is very limited.
 * https://www.make.com/en/help/apps/productivity/microsoft-365-excel#build-microsoft-365-excel-scenarios


* Lets try setting up the next route. This filter condition checks that the priority lvl is set to 2 (Medium)
<img width="471" alt="Screenshot 2024-04-04 at 11 38 24 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/501bdd37-89bd-488e-8fc8-79fc70ef2be7">

* Search for Excel and lets try something different, this time select add a worksheet row. Choose a file, then a worksheet
<img width="452" alt="Screenshot 2024-04-04 at 11 43 07 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/79e5e5f3-86bf-49e4-865b-338ca02b0d86">

* Scroll down and you can find the header names. Using the survey response attributes, you can populate the columns.
* One perk of flow so far is that you can use the metadata from the survey (ie user email, without creating a 'for each' loop to iterate thorugh the survey which over complicates the flow (see geom99/Week12 Power automate)
* Not sure about how the image attachments will go through, its not showing up under the feature attributes, but there is an option for attachments, so we'll see what that is.

* I deleted the other router that was giving me errors to give this one a test go.
* Click the run once button and complete a survey with a medium priority level
* Looks like the test was a success.
<img width="691" alt="Screenshot 2024-04-04 at 11 53 36 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/399dc305-3fdd-41a1-bd4f-87066bce8eeb">

* Now go check the excel workbook. The row got inserted in, yay. The date doesn't look right, but I know that's because I didn't set the esri datatype correctly when I created the survey. Also, the attachment doesn't work unfortunately
<img width="1275" alt="Screenshot 2024-04-04 at 11 55 03 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/eb70c963-3b89-45c0-b0cf-6b7c8ea48bd9">

* I do like the user interface on this web app, I think using it is a lot easier and smoother than the experience on Power Automate, however being able to add the photo attachment is a key feature
<img width="332" alt="Screenshot 2024-04-05 at 12 05 45 AM" src="https://github.com/lowylori/technicallogs/assets/49323685/879cfd03-c38d-4c89-933a-6e5571fe44b2">

* After returning back to Make, I noticed there are now more options under attachments including an attachment URL. This will do for our purposes.
* Lets test it again with that update. Now when you click the url, the image opens up in a new tab.
<img width="1083" alt="Screenshot 2024-04-05 at 12 09 57 AM" src="https://github.com/lowylori/technicallogs/assets/49323685/548a6fc4-db67-4d80-9ff1-57fac03636e0">

* Feeling pretty good about this so far, so I'm going to complete the flow by populating the other priority levels.
* 

## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc
