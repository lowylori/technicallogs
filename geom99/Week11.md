# Week 11 Log
### Summary

Description: Exploring some open source solutions. 

Date: Mar 20/24

Total Time: 3 hrs

Reference Links: https://leafletjs.com/examples/quick-start/

### Steps:
- [x] KoboToolbox [30 mins]
- [ ] Leaflet Javascript API [45 mins]
- [ ] Data Tier (Map Tiles, GeoJSON)
- [ ] Automate with FME

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


## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc
