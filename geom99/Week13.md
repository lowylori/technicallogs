# Week 13 Log
### Summary

Description: Exploring report generation using arcgis api for python with survey123. Trying Make software for automating excel spreadsheet workflow.

Date: April 4, 2024

Total Time: 3hrs

Reference Links: https://www.youtube.com/watch?v=dzAbLFVuWiw&t=1700s
https://github.com/Esri/Survey123-tools/blob/main/Work_with_Reports/create_reports_using_the_arcgis_api_for_python.ipynb

### Steps:
- [ ] Report generation with ArcGIS API for Python [60 mins]
- [ ] step 2
- [ ] step 3
- [ ] step 4

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

* We want to see our available templates (to use for our report). Use the report_templates method to create a list of templates. Print the title property of the template.
![image](https://github.com/lowylori/technicallogs/assets/49323685/affc8154-f184-4771-afb1-017678afdad6)




## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc
