# Keep track of all the squirrels
## 1. Project description
This project is mainly used to track all the squirrels in the Central Park. It has two main applications, which are sightings and maps. 
It could import the 2018 Central Park Squirrel Census data and allow people to add, update, view squirrel data and export updated data. 

More specifically, for the application of sightings, it will show a table that lists all squirrel sightings with links to edit each.
When you click the unique link for each squirrel, you could update a particular sighting.
It also have a single link to the “add” sighting view which allows you to create a new sighting. (Fields supported are as follows:
Latitude, Longitude, Unique Squirrel ID, Shift, Date, Age, Primary Fur Color, Location, Specific Location, Running, Chasing,
 Climbing, Eating, Foraging, Other Activities, Kuks, Quaas, Moans, Tail flags, Tail twitches, Approaches, Indifferent, Runs from)
Finally, there is a general stats about the sightings. We pick five attributes and summary the statistics (including running, chasing, climbing, eating and foraging).

For the application of maps, it shows a map that displays the location of the squirrel sightings on an OpenStreets map.


## 2. Group name 
Project Group 83, Section 2

## 3. UNIs
UNIs: [lt2765, yh3207]

## 4. Project link
http://tools-lt.appspot.com/sightings

http://tools-lt.appspot.com/sightings/stats

http://tools-lt.appspot.com/map

## 5. Very very important
1. After deployment, the database becomes read only which means that you could see the view of edit and add but you could not click the submit button to change the data.
2. The squirrel id should be unique. However, in the database, some squirrel ids are the same (eg. "37E-PM-1006-03"). For these ids, you could not click the link of "http://tools-lt.appspot.com/sightings/uniqueid" Because one id related to two rows of data. If you want to get rid of this problem, you need to clean the data before importing.
