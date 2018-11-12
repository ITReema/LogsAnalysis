# Logs Analysis
print report based on database 

### Requirements <br>
1. [Python](https://www.python.org/downloads/)
2. [Vagrant](https://www.vagrantup.com/downloads.html) 
3. [Virtual Machine](https://www.virtualbox.org/wiki/Downloads)
3. [FSND virtual machine](https://github.com/udacity/fullstack-nanodegree-vm)

#### Once you get the above software installed, follow the following instructions:
```
cd vagrant
vagrant up
vagrant ssh
cd /vagrant
```
### Download and Load the Data <br>
“newsdata.sql” [Download](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

**To load the database:** <br>
```psql -d news -f newsdata.sql``` <br>
**To run the database:**<br>
```psql -d news``` <br>
**To explore the data**<br>
	```\dt ```	lists the tables that are available in the database<br>
	```\d table_name ```	shows the database schema for that particular table<br>
   ```\dv ```	shows the views in database<br>


#### Create Views <br>
Views were created to answer the third query in the project.<br>


```
CREATE VIEW errors AS 
SELECT date(time), COUNT(*) as error_requests 
FROM log 
WHERE status = '404 NOT FOUND' 
GROUP BY date(time);
 ```


```
CREATE VIEW total AS 
SELECT date(time), COUNT(*) AS total 
FROM log 
GROUP BY date(time);
```

```
CREATE VIEW rate AS 
SELECT TO_CHAR(total.date, 'FMMonth DD, YYYY') as date, (100.0 * errors.count / total.count) AS percentage 
from total, errors 
WHERE total.date = errors.date;
```
<br>

### References<br>
* [Udacity](https://classroom.udacity.com/nanodegrees/nd004-connect/parts/4237300b-ed78-4462-a353-a0bd14af33bc/modules/b632715b-7aae-4670-9137-bcd880561475/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/079be127-2d22-4c62-91a8-aa031e760eb0)
* [SQL](https://www.w3schools.com/sql/default.asp)
* [Oracle / PLSQL: TO_CHAR Function](https://www.techonthenet.com/oracle/functions/to_char.php)
