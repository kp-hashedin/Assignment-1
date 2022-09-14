# Assignment-1

## Steps to run project
1. clone the repository using following command. <br />
 ```git clone https://github.com/kp-hashedin/Assignment-1.git```
 
2. create virtual environment using following command in terminal.
 ```virtualenv venv```
 
3. Install dependencies using following command <br />
   ```pip install -r requirememts.txt```
4. Run application using  -
  ```uvicorn main:app --reload```
  
<b>Once application is up </b> <br />
Database health Check - http://localhost:8000/health

## Functionality
1. Add Metrics to a user.
2. Update a metric of a user.
3. Delete a particular metric of a user (username, key pair cannot be repeated).
4. Get all the metrics of a user.(filters supported: username, key, tags)
5. Get metrics of all the users by key name(filters supported: tags).
6. <b>Bulk API to accept a CSV file as input and add entries to the DB.</b> <br >

csv file - [link](https://amedeloitte-my.sharepoint.com/:x:/g/personal/kavpandey_deloitte_com/EY8_gs2BvHVEjIyRXxE-j2EBcV3V4iaA42bEMlHym06gDw?e=RbEBO8)
use this csv file, or can use any csv file with four fields i.e; <b> username, key, value, tag</b>

## Some Important points
1. Python 3.7+ version
2. Sqllite3 database

## Tech - Stack
1. Language - Python 
2. Database - sqllite3 '
3. ORM - SQLalchemy

## table structure
![alt text](https://github.com/kp-hashedin/Assignment-1/blob/main/Screenshot%20from%202022-09-12%2022-05-04.png)


Deployed link - https://xmi9jr.deta.dev/docs#/   <br />
DB operations not working(Couldn't find any referecne for deta deployement with database), for complete workflow need to isntall into local machine

Refer Demo - [DemoLink](https://amedeloitte-my.sharepoint.com/:v:/g/personal/kavpandey_deloitte_com/EWjLxB6G-sFOuZO4k1BDgbYBOAF7JATbBnUIg1xJ4nm-DA?e=UX6o4W) 🚀

