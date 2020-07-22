# Driver Ranking

## Install/Setup
* In order to run this application you will need Python3 installed on your system.
* No special packages are needed. 

## Running
```bash
python3 main.py --action [run_test|rankings]
```
* **run_test** will execute some basic test to make sure the systems works properly.
     * Some of the tests are based on the data available so if we change the data we need to change the test acceptance criteria too.
 * **rankings** will print the latest rankings. 

### Notes
* The idea behind the implementation is that, the rankings are going to be submitted to some sort of database.  
* The CSV files in the **data** folder are mimicking a possible data structure where we have 
    * Drivers
    * Rides storing the ride details/attributes
    * Relationship between the two 
* The ride application will send the ride/driver data to the DB.
* The *process_data* method will be called periodically to get the data and find the ranking.
* The latest rankings can be accessed from the *get_top_ten* method.