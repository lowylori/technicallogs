# QGIS Geopackage To ArcGIS Online
### Summary

Description: Testing the process of publishing a geopackage on AGOL from a geopackage. Edit the geopackage in QGIS and overwrite the data. Connect a web map to the hosted feature layer and make sure the overwriting the data does not cause any errors for the webmap

Date:

Total Time:

Reference Links: https://www.youtube.com/watch?v=9ojA8u4nRag

### Steps:
- [x] Creating a Hosted Feature Layer in AGOL From a gpkg
- [ ] Edit a Single Layer Geopackage in QGIS
- [ ] Update Published Hosted Feature Layer in AGOL
- [ ] Edit a Multi Layer Geopackage in QGIS
- [ ] step 4

## Create a Hosted Feature Layer in AGOL From a gpkg  [05/13/24 20 mins]

### Single layer geopackage (simple)

* Have your single layer geopackage file ready to go

> [!WARNING]  
> Avoid the use of underscores in file and layer name.

* Open AGOL, sign in
* Drag and drop your file.gpkg in the content tab on AGOL
* Choose to add as a file.gpkg and as a hosted feature layer 
<img width="1096" alt="Screenshot 2024-05-13 at 7 08 25 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/1e8783a1-bbee-412c-bb6b-0d22da2caea7">

* Complete item metadata and continue. Once it finished processing you will have 2 items added to content, a geopackage and a feature layer.
<img width="772" alt="Screenshot 2024-05-13 at 7 13 11 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/06389f0d-aea4-4296-8603-6aafce4edb6d">

* Move onto the next step - Edit Geopackage in QGIS

### Multilayer geopackage 

* Create a new geopackage in QGIS

## Edit a Single Layer Geopackage in QGIS [00/00/24 time]

* Open up QGIS
* Under the layer tab, open the Data Source Manager. Find the tab that says Geopackage
* Select 'New' and browse your device for the gpkg
* Select 'Connect' and you will see the layers available within the gpkg

<img width="734" alt="Screenshot 2024-05-13 at 8 08 11 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/a8f705d3-da66-4b86-95e1-d1d4ec3c22aa">

* Make the required edits to the geopackage and close. You are ready to update on AGOL now.
* 

## Update (overwrite) Published Hosted Feature Layer in AGOL [00/00/24 time]

* With your newly edited gpkg ready to go, open AGOL and sign in
* located the hosted feature layer containing your geopkg data
* open the items page
* click update data, then select 'overwrite entire feature layer'

<img width="879" alt="Screenshot 2024-05-13 at 8 22 00 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/68995785-89ff-4875-bdb1-1295b19bafd6">

* Click next
* Browse for the gpkg file in your device

> [!WARNING]  
> File name and layer names must stay exactly the same as the origional upload

* A screen will come up that says 'overwriting'
* Once its successful, the items page will pop up with a message along the bottom of the screen. 
<img width="879" alt="Screenshot 2024-05-13 at 8 24 58 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/a0e7bead-a305-4fb5-8f55-305aabacc274">

* This time it was not successful, and the error msg is useless. :(

<img width="888" alt="Screenshot 2024-05-13 at 8 25 57 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/c6aafd91-1684-44a1-b8ac-b27aacb16400">

* When this fails, the hosted feature layer no longer works, and you get an error publishing the service 

### Troubleshooting

* Delete the failed hosted feature layer and geopkg items off AGOL
* Rename the geopkg on your device
* Open gpkg in QGIS
* Lets see if the issue is due to the GlobalID or ObjectID fields
* rename them as pictured below in layer properties. Save edits

<img width="612" alt="Screenshot 2024-05-13 at 8 40 10 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/b9b7d2d2-335c-4b88-9fde-039d2f9bbd86">

* Turns out QGIs doesnt like this

<img width="505" alt="Screenshot 2024-05-13 at 8 41 15 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/d8a17e78-a49f-426b-9f97-6c962fed422c">

* It also doesn't want you to change the name back either.

<img width="500" alt="Screenshot 2024-05-13 at 8 46 30 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/2c300b5a-d342-444e-992d-26b134116113">

* Maybe this is due to the fact that the data was created in an Esri environment and these fields are not editable?

* Lets delete the fields instead of renaming. Remove the layer and dont save the changes
* Use the delete field to delete the OBJECTID and GlobalID field.
<img width="491" alt="Screenshot 2024-05-13 at 9 07 20 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/e2e62413-f280-4c30-8bfe-6d163edc7ce8">

* Deleting the fields seemed to mess with the 'type' coloum and then QGIS crashed lol

<img width="269" alt="Screenshot 2024-05-13 at 9 11 11 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/6315d3ed-6ce2-455b-b494-cd546460d4b8">

* The objectID field was recreated when I reopened it.

<img width="314" alt="Screenshot 2024-05-13 at 9 12 47 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/5a26a36e-99ec-4925-920b-0dca723b5959">

* Lets try again in AGOL

<img width="890" alt="Screenshot 2024-05-13 at 9 19 48 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/48584f30-69f1-45e3-aab7-26109788dca6">

* Check out the helpful error msg at the bottom of the screen


## Task num [00/00/24 time]

Desc

## Task num [00/00/24 time]

Desc
