
# Jama Software
Jama Software is the definitive system of record and action for product development. The company’s modern requirements and test management solution helps enterprises accelerate development time, mitigate risk, slash complexity and verify regulatory compliance. More than 600 product-centric organizations, including NASA, Boeing and Caterpillar use Jama to modernize their process for bringing complex products to market. The venture-backed company is headquartered in Portland, Oregon. For more information, visit [jamasoftware.com](http://jamasoftware.com).

Please visit [dev.jamasoftware.com](http://dev.jamasoftware.com) for additional resources and join the discussion in our community [community.jamasoftware.com](http://community.jamasoftware.com).

### Delete Items By DocumentKey
```Main.py``` is a script which extracts rows from a .csv file and deletes all items listed according to their documentKey values. 
The script will produce two output files: 
  - deleted_items.json lists all items that have been successfully deleted. 
  - ignored_items.json lists all items that have been ignored by the script. 

Items with names in the .csv file that do not match the name of the item retrieved by the API will be ignored by the script. 

Please note that this script is distrubuted as-is as an example and will likely require modification to work for your specific use-case.  This example omits error checking. Jama Support will not assist with the use or modification of the script.

### Before you begin
- Install Python 2.7 or higher and the requests library.  [Python](https://www.python.org/) and [Requests](http://docs.python-requests.org/en/latest/)

### Setup
1. As always, set up a test environment and project to test the script.

2. Place your .csv file in the same directory as the script.

3. Fill out the jamaconfig.py section of the script.  The necessary fields are:
  - ```username```
  - ```password```
  - ```base_url```
  - ```item_type``` - item type of items to be deleted
  - ```filename``` - .csv filename
  - ```documentKey_column``` - innteger value of documentKey column in your .csv file (starts at 1)
  - ```name_column``` - integer value of name column in your .csv file (starts at 1)

