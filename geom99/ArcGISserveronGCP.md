# ArcGIS Server on Google Cloud Platform
### Summary

Description: Create a ArcGIS Server hosted on the Google Cloud Platform (GCP)

Date: March 7, 2024

Total Time: 20 mins

Reference Links: https://www.youtube.com/watch?v=dyFeyBX9jIY

### Steps:
- [x] Create gmail account and get credits [5 mins]
- [x] Create VM from image [20mins]
- [x] Firewall Rules [10 mins]
- [x] Run from remote desktop and Shutting down VM [5 mins]
- [x] Create a Web Map on ArcGIS Online using published Services [5 mins]
- [ ] Publish a map service into your ArcGIS Server on your GCP VM [15 mins]

## Create gmail account and get credits [03/07/24 5 mins]

* Sign up for a gmail account, creating an email address and password. 
* Get and redeem organization credits. https://cloud.google.com/billing/docs/how-to/edu-grants#redeem

## Create VM from image [03/07/24 20 mins]

* Navigate to console.cloud.google.com. Sign in to your gmail account
* Select the project dropdown in the top left corner. Then select 'new project'. Set a name for this project.
* Go to Compute Engine> VM instances and enable Compute Engine API.
* Click 'Create Instance'. This will open the configuration for a new VM instance

<img width="995" alt="Screenshot 2024-03-14 at 7 47 51 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/d8a5df55-8759-41b9-8ae2-66ac8bd67315">

* Choose Region and zone (used default Iowa).
* Set Machine configuration (used E2).
* In firewall settings, allow for both HTTP and HTTPS traffic.

> [!NOTE]
> for Boot disk, used a custom image from arcgis-server-374520 for GEOM 99, which has ArcGIS server already installed.

* Click 'Create'

* Once the VM has been created, set windows password from VM instances under the connect column. Set username to student and copy generated password.

> [!NOTE]
> this password only shows once, make sure you copy into notepad.

## Firewall Rules [03/08/24 10 mins]

* Create Firewall Rule by going to 'Set up firewall rules'. 
* Set name as flemingrdp444. Under targets, select all instances in the network. As the source filter, use IPv4 ranges and set the ip address or use no restriction (0.0.0.0/0).
* Under protocols and ports, select Specified protocols and ports. Enter port 444. This is the remote desktop protocol port.
* Click Create to finalize the settings

Set up a GCP Firewall rule to allow ArcGIS Server Management ports

* Create Firewall Rule by going to 'Set up firewall rules'. 
* Set name as flemingrdp444. Under targets, select all instances in the network. As the source filter, use IPv4 ranges and set the ip address or use no restriction (0.0.0.0/0).
* Under protocols and ports, select Specified protocols and ports. Enter ports 6443, 6080. Click create.

![image](https://github.com/lowylori/technicallogs/assets/49323685/84a3f30a-a05c-4fca-aece-f9de0a67a792)

Setting a Windows Firewall Rile to allow ArcGIS Server Management ports

* log into remote desktop using your external IP address and username and password. Make sure your instance is running
* from the start menu, find 'Windows Defender Firewall'. Select advanced settings from the left panel to open this window.

![image](https://github.com/lowylori/technicallogs/assets/49323685/b36219b3-8a03-46b0-81af-d08f45d2854c)

* Select 'Inbound Rules from the left pannel, then 'New Rule...' from the right panel.
*  For rule type, select Port.
*  In potocol and ports chose TCP and enter the ports 6443 and 6080. Click next.

![image](https://github.com/lowylori/technicallogs/assets/49323685/850c0885-6860-41a0-b0d1-bae14a55649b)

* leave the default 'Allow the connection', click next.
* allow the rule to apply to domain, private and public. click next.
* on the last page, name the rile 'ArcGIS Server Admin Ports'

## Log in to Remote Desktop and Shut down a VM [03/07/24 5 mins]

Log in to Remote Desktio:
* From console.cloud.google go to Computing Engine> VM instances. Click the three dots on the far right for your VM and select start.
* once the VM is started, a new External IP will be generated. Copy this IP.
* From the windows start menu, search remote desktop. Open the application.
* paste your external ip address in, colon, port # (444)
* this will prompt for a username and password.

There are two options for shutting down a VM:
* From remote desktop, go to the start menu. Select the power button and click shut down.
* From console.cloud.google.com go to computing engine > VM instances. Click the three dots on the far right of your active VM. Choose the 'Stop' option.
  ![image](https://github.com/lowylori/technicallogs/assets/49323685/19aade44-55b6-4c2b-ae28-0b8926422339)


## Create a Web Map on ArcGIS Online using published Services [03/16/24 5 mins]

* Open ArcGIS Rest Services and access a published service.
![image](https://github.com/lowylori/technicallogs/assets/49323685/6b342953-9bc1-4edf-9d64-18c4e95c2efc)

* Locate the desired Serivce you would like to use in a webmap. Along the 'View In' horizontal bar, select 'ArcGIS Online Map Viewer
![image](https://github.com/lowylori/technicallogs/assets/49323685/e36f6551-527f-4f73-b79e-c8038c55c260)

* Sign into your account on AGOL in the new tab that opens. Save map to your AGOL account.
![image](https://github.com/lowylori/technicallogs/assets/49323685/a554022b-1a29-4148-9fe7-57e8022a9bf8)


## Publish a map service into your ArcGIS Server on your GCP VM

* Start your VM instance. Ensure your VM is running for the duration of this workflow. If the server is offline, you will not be able to publish
* Open ArcGIS Pro
* Create a map using a copy of the Canada.shp file which is also stored on the VM.

> [!NOTE]
> Ensure you know the location (filepath) of this file on your local computer and on your VM.

* Style the shapefile to suite your needs.
* Save Project
* Add new server connection by going to the insert panel along the top bar, selection the connections drop down
![image](https://github.com/lowylori/technicallogs/assets/49323685/36c0ae8d-d7ba-4bf0-a379-aff2b125a3cf)

* From the 'Add ArcGIS SErver Connection' window, for server URL, enter the external IP address, colon, 6443/arcgis. Enter the ArcGIS server username and log in
![image](https://github.com/lowylori/technicallogs/assets/49323685/874d8f95-b48e-44f4-80f8-e0b504d6bebe)

* The server connection should now show up in the catalog pane under servers
* Right click on the ArcGIS server from the catalog pane. Click Publish> Map Service
* This will open a window where you need to select the map you would like to publish. Use the Canada map we are working on.
* Give your map a fitting name, summary and tags. For data, use the 'Reference Registered data' option. Select a folder location.
![image](https://github.com/lowylori/technicallogs/assets/49323685/ea70dd5d-c91c-4ede-9259-b6d45cd9f17a)

  
* Click analyze at the bottom, this will show you if you have any errors or warnings. Address the following 2 errors:
![image](https://github.com/lowylori/technicallogs/assets/49323685/d5d7b9fd-5679-46d3-9417-9c16f11f1ab1)

* For the IDs not assigned, click the 3 dots beside it and choose the option that auto assigns IDs sequencially.
* To register data source for the server, select the 3 dots and click regester data source with server.
* Copy and paste you filepaths that point to where the canada.shp file is stored. Set a name. Click 'Create'
![image](https://github.com/lowylori/technicallogs/assets/49323685/e611fdb8-7ef4-4c68-860c-c56920400809)

* Now that your important errors and warnings have been resolved, you can reanalyze one last time and publish.

* After you get the confirmation that the Map Service was published, you can go to ArcGIS rest service to ensure your map is there.
![image](https://github.com/lowylori/technicallogs/assets/49323685/8e1f1075-1a1c-4731-bcb2-92c0c1454ed0)

* You can select to view in ArcGIS Map Viewer to see your published map.

  

