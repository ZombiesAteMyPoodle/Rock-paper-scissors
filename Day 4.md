## **Day 4**



### <u>List of new code</u>

- **Module**
- **Random**
- **Lists**
- **Split**







1. **Module** - Code which can be imported into current "module" making big projects more readable

   ```python
   import player_stats
   
   #player_stats.....
   #	This contains the code for all the players statistcics
   ```

   

2. **Random** - Module containing all the code needed to create random variables.

   ```python
   import random
   
   #once imported code can be written
   
   player_age = random.randint(25, 55)	#For type integer
   player_name = random.choice(names)  #For type string
   
   ```



3. **Lists** - Python name for an array

   ```python
   counties = ["West Sussex", "Kent", "Hampshire"]
   counties.append["Oxfordshire"] 										#Add 1 to list
   counties.extend["Devon", "Cornwall"]							#Add multiple to list
   
   print(counties[1]) 																#This will print Kent
   print(counties[-1])																#This will print Hampshire as -1 starts 																										#from the end
   ```

   
   
4. **Lists** - Nested lists

   ```python
   fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
   vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
   
   dirty_dozen = [fruits, vegetables]
    
   print(dirty_dozen[1][1])
   
   # The first bracketed number pertains to the array in the index
   # The second bracketed number pertains to the item in the array
   ```

   

5. **Split** - Split a string into parts

   ```python
   text = 'Richard, Peter, David'
   
   names = text.split(',')
   ```

   