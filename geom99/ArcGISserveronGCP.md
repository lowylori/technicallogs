# ArcGIS Server on Google Cloud Platform
### Summary

Description: Create a ArcGIS Server hosted on the Google Cloud Platform (GCP)

Date: March 7, 2024

Total Time: 20 mins

Reference Links: https://www.youtube.com/watch?v=dyFeyBX9jIY

### Steps:
- [ ] Create VM from image
- [ ] Firewall Rules
- [ ] step 3
- [ ] step 4

## Create VM from image [03/07/24 20 mins]

Navigate to console.cloud.google.com
Create a new project.
Go to Compute Engine>VM instances and enable Compute Engine API.
Click 'Create Instance'.
Choose Region and zone (used default Iowa).
Set Machine configuration  (used E2).
In firewall settings, allow for both HTTP and HTTPS traffic.

> [!NOTE]
> for Boot disk, used a custom image from arcgis-server-374520 for GEOM 99, which has ArcGIS server already installed

Click 'Create'

Create Firewall Rule by going to 'Set up firewall rules'. Set name and create the rule for TCP port 444

Set windows password from VM instances>under connect column. Set username to student and copy generated password

> [!NOTE]
> this password only shows once, make sure you copy into notepad.

