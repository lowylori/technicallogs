# Week 10 Log - Collab Web Project
### Summary

Description: This log documents the workflow and exploration process for week 9 developing a web solution within the context of our project with Southern Africa Wildlife College.

Date: 03/06/24

Total Time: 3 hours

Reference Links: https://doc.arcgis.com/en/arcgis-solutions/latest/reference/introduction-to-parks-and-grounds-management.htm

AGOL Item Link: https://fleming.maps.arcgis.com/home/item.html?id=96ca4c6b35c840fab9f678c176bccefb  (organization shared only)

### Steps:
- [x] Map out the structure of our web solution [30 mins]
- [x] Explore AGOL Solutions [30 mins]
- [x] Parks and Ground Management Solution [30 mins]
- [x] Deploy Parks and Grounds Managment [90 mins]

## Map out the structure of our web solution [03/05/24 30 mins]

Created a flow chart to better understand the stucture of our web solution. The chart suffered several iterations and is still being developed. The idea was to understand how the various components of this solution will interact with eachother, and what AGOL apps can accomodate our business needs. See Figure below. 

![SAWCEnvirAssessmentFlow](https://github.com/lowylori/technicallogs/assets/49323685/7affe64f-90a5-4502-8718-192445bd0e21)

 * Found the internal requests and and public requests to be quite similar - may not need to have 2 seperate surveys for this.
 * there will need to be more than one dashboard, so everything doesn't get lumped together in a data vomit.
 * Need to consider who will be operating and managing each portion of this flow chart.
 * More time to consider how we can use FME alongside AGOL.


## Explore AGOL Solutions [03/07/24 30 mins]

Spent some time browsing through various AGOL solutions and seeing which ones were a good fit. Read the description and looked into the software that each solution utilized. Narrowed down to the following three options:
1. Parks and Ground Management
2. Citizen Problem Reporter
3. Conservation Easement Monitering

## Parks and Ground Management Solution [03/10/24 30 mins]

Watched the 20 min overview of the solution and read through the documentation. I came up with the following pro's and con's from this process.

Pros:
* Can submit both public and internal requests (forms are via survey123)
* Connected to field maps and has an active inventory for the grounds
* Management center contains an intuitive dashboard that allows you to view open requests and unassigned work
* You can create assignments directly from the management center and assign a task to maintenance staff
* Park assignments - video did not cover the maintenance assignment side of this solution -need to know more
* Uses workforce to assign tasks (an app our client was interested in)
* Workers receive the task and update it when its complete
* Dashboard to reflect workforce tasks as they are assigned, in progress and completed

Cons:
* Generating reports -  not a feature but an important requirement for our client
* Many layers to this solution, however, may be too complex for the client. Looking for simple and easy to use.

## Deploy Parks and Grounds Managment [03/10/24 90 minutes]

Generated a replica of the Solution by selecting the 'deploy now' option on my Fleming AGOL account. From there, I could see the solution was divided into 4 major sections:

<img width="891" alt="Screenshot 2024-03-14 at 9 45 39 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/18fc8c24-f22f-46cb-a2e5-59cc231ec050">

### 1. Parks and Grounds Request: This is the Survey and webmap that the public can use to create a request for maintenance or report problems. The survey is hosted through Survey123 and can be used on web or app.

 * Submitted a sample survey to test out the system
 * Survey can also be modified to add different fields via Survey123
  <img width="343" alt="Screenshot 2024-03-14 at 9 49 58 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/38c676e2-b4fe-46b3-b3c4-439a77e9056f">

 * Viewed the web map (Requests) to see that the request was added. You can view the survey as an entry in the attribute table.
<img width="1099" alt="Screenshot 2024-03-14 at 9 52 31 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/4c91546c-51cd-40ac-ac9c-4a55dcb2ee0a">

### 2. Parks and Grounds Inventory: ArcGIS Experience Builder app used by internal staff to create, update, and review parks and grounds assets.

 * created an asset within the Parks and Grounds Inventory. There is a variety of categories for assets. Each asset has a unique and standard symbol that can be easily interperted. This will be a useful time saver, so each asset doesn't need to be customized.
<img width="1006" alt="Screenshot 2024-03-14 at 10 05 31 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/7a2699fd-b493-4ab7-b93b-9f780a406ad9">
 
 * viewing the field map on Map Viewer. Mobile workers can use this Field Maps in the Field to create, edit and review assets. Creating new assets is easy - like filling out a form. You select the location and set the category, the asset type, and a few details ie. public, seasonal etc.
<img width="964" alt="Screenshot 2024-03-14 at 10 47 36 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/60081504-87d3-42d6-9bb7-3bdd6255996b">

 * Field map can be configured to suit business needs. You can modify the form (by category) and set different fields depending on what's important for the business. SAWC might need zone number included to allow for easy filtering.
 * you can also enable the map for offline use which allows it to be downloaded in apps that support offline workflows and used in locations without an internet connection (can be useful when network connection is unreliable.

<img width="764" alt="Screenshot 2024-03-14 at 10 50 16 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/42739ca8-cdc9-408b-aa2c-a18f43336e67">

### 3. Park Assignments: This is a group used in the Solutions Workforce Project. 

 * Contains the various web maps and layers that maintenance staff will need access to. This is where you would add members to the group and where you can add new items.

<img width="680" alt="Screenshot 2024-03-14 at 10 58 53 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/ab279621-f892-44f6-ba0d-3835afb6343c">

 * The Parks and Grounds Assignment Feature laayer is used to store assignments and workers for use in the Parks and Grounds Assignment Workforce project.

 * Internal staff also have access to submit internal requests for maintenance. For a better visual of the Park Assignment Group, I've attached a screenshot of the directory, so you can see what feature layers on on each web map.

<img width="430" alt="Screenshot 2024-03-14 at 11 04 35 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/993f1904-ae02-4d7d-876a-bdd1eb2c9c6f">

### 4. Parks and Grounds Management Center: An experience builder app used by ops and maintenance managers to manage requessts for services and create work assignments.

 * The app opens to a dashboard view which displays number of open requests and number of unassigned work. From here, you can click to manage either.
 * After that, you can select the request and view the details. This is the request we created earlier.

<img width="856" alt="Screenshot 2024-03-14 at 11 10 46 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/19f64adc-687c-48e7-b086-06e108ad2678">

 * Now you can click 'create assignment' and enter in the details. It allows you to select an assignment type, location, user, level of priority and due date. You can set a description and ass attachments to assist the worker. Since I have no workers yet, I left the assignment unassigned.

<img width="601" alt="Screenshot 2024-03-14 at 11 13 17 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/0a280b7a-1afd-4a99-ab5b-bcee35d8dc3c">

 * You can also configure the Parks and Grounds Management Center to suit the business needs.
   
<img width="1073" alt="Screenshot 2024-03-14 at 11 16 03 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/bea1b686-931d-4c7b-af0b-2cc0dc491cda">

 * Workers are adding within the app configuration.

<img width="827" alt="Screenshot 2024-03-14 at 11 20 20 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/e849f868-a610-4136-8ecd-0ab2f2c5c993">

 * You can go back and assign the task to someone. It allows you to see who is currently working via workforce.

<img width="599" alt="Screenshot 2024-03-14 at 11 22 15 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/9702c173-8d03-4446-93ab-9de821acf303">

 * Revisiting the Parks and Grounds Assignment Webmap from the workforce group, you can see now that the the assignment is it there, along with a symbology for status

<img width="1147" alt="Screenshot 2024-03-14 at 11 31 38 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/95c66f32-d71b-4c3b-8b86-ffa3a60fde43">

 * Download the workforce app. Sign in.
 * From within the mobile workforce app, you are able to view the assignment, start it, add notes and update the status.

![IMG_3522](https://github.com/lowylori/technicallogs/assets/49323685/6a0b3a31-8557-4a70-833a-cececb982c05)

![IMG_3523](https://github.com/lowylori/technicallogs/assets/49323685/b40d39e4-8a65-40da-bfdc-8138fc6d3811)


