# ArcGIS Server on Google Cloud Platform
### Summary

Description: Create a ArcGIS Server hosted on the Google Cloud Platform (GCP)

Date: March 7, 2024

Total Time: 20 mins

Reference Links: https://www.youtube.com/watch?v=dyFeyBX9jIY

### Steps:
- [ ] Create gmail account and get credits
- [ ] Create VM from image
- [ ] Firewall Rules
- [ ] Run from remote desktop
- [ ] Create a Web Map on ArcGIS Online using published Services
- [ ] publish a map service into your ArcGIS Server on your GCP VM

## Create gmail account and get credits [03/07/24 20 mins]

Sign up for a gmail account, creating an email address and password. 

Get and redeem organization credits. https://cloud.google.com/billing/docs/how-to/edu-grants#redeem

## Create VM from image [03/07/24 20 mins]

Navigate to console.cloud.google.com. Sign in to your gmail account

Select the project dropdown in the top left corner. Then select 'new project'. Set a name for this project.

Go to Compute Engine> VM instances and enable Compute Engine API.

Click 'Create Instance'. This will open the configuration for a new VM instance

<img width="995" alt="Screenshot 2024-03-14 at 7 47 51 PM" src="https://github.com/lowylori/technicallogs/assets/49323685/d8a5df55-8759-41b9-8ae2-66ac8bd67315">

Choose Region and zone (used default Iowa).
Set Machine configuration (used E2).
In firewall settings, allow for both HTTP and HTTPS traffic.

> [!NOTE]
> for Boot disk, used a custom image from arcgis-server-374520 for GEOM 99, which has ArcGIS server already installed.

Click 'Create'

## Firewall Rules

Create Firewall Rule by going to 'Set up firewall rules'. Set name and create the rule for TCP port 444



Set windows password from VM instances>under connect column. Set username to student and copy generated password

> [!NOTE]
> this password only shows once, make sure you copy into notepad.

## Create a Web Map on ArcGIS Online using published Services

Open ArcGIS Rest Services and access a published service.
![image](https://github.com/lowylori/technicallogs/assets/49323685/6b342953-9bc1-4edf-9d64-18c4e95c2efc)

Locate the desired Serivce you would like to use in a webmap. Along the 'View In' horizontal bar, select 'ArcGIS Online Map Viewer

![image](https://github.com/lowylori/technicallogs/assets/49323685/e36f6551-527f-4f73-b79e-c8038c55c260)

Sign into your account on AGOL in the new tab that opens. Save map.

## Publish a map service into your ArcGIS Server on your GCP VM


