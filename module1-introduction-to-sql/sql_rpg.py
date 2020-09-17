import sqlite3

connection = sqlite3.connect(r'C:\Users\keith\Desktop\GH\DS-Unit-3-Sprint-2-SQL-and-Databases\module1-introduction-to-sql\rpg_db.sqlite3')
print('connection:', connection)

cursor = connection.cursor()
print('cursor:', cursor)

# -- Total Characters Created
query = 'SELECT COUNT (character_id) as Total_Characters FROM charactercreator_character;'
result2 = cursor.execute(query).fetchone()
print ('Total Characters Created:',result2[0])

# --How many total items?
query = 'SELECT COUNT (item_id) as Total_Items FROM armory_item;'
result2 = cursor.execute(query).fetchone()
print ('total items:',result2[0])

# --How many items are weapons 
query = 'SELECT COUNT (item_ptr_id) as weapons FROM armory_weapon;'
result2 = cursor.execute(query).fetchone()
print ('total weapons:',result2[0])

# --How many items are not weapons
query = '''SELECT  (SELECT COUNT(item_id) FROM armory_item) - 
(SELECT COUNT(item_ptr_id) FROM armory_weapon)
AS Items_non_weapon;'''
result2 = cursor.execute(query).fetchone()
print ('total items that arent weapons:',result2[0])

# --How many items does each character have
query = '''SELECT COUNT (DISTINCT item_id)
FROM charactercreator_character as charr
JOIN charactercreator_character_inventory as char_inv
ON char_inv.character_id = charr.character_id
GROUP BY charr.character_id
LIMIT 20;'''
result2 = cursor.execute(query).fetchall()
print ('items each character has:',result2)

# --How many weapons does each character have?
query = '''SELECT COUNT (item_id) as character_weapons
FROM charactercreator_character_inventory as char_inv
JOIN armory_weapon as weapon
ON char_inv.item_id = weapon.item_ptr_id
GROUP BY char_inv.character_id
LIMIT 20;'''
result2 = cursor.execute(query).fetchall()
print ('weapons each character has:',result2)

# --Average items per character
query = '''SELECT AVG(items) as Average_Items
	FROM (
  SELECT
	  COUNT(item_id) as items
  FROM charactercreator_character_inventory
  GROUP BY character_id
) '''
result2 = cursor.execute(query).fetchall()
print ('Average items per character:',result2[0])

# --Average weapon per character
query = '''SELECT AVG(character_weapons)
FROM
(
SELECT COUNT (item_id) as character_weapons, character_id
FROM charactercreator_character_inventory as char_inv
JOIN armory_weapon as weapon
ON char_inv.item_id = weapon.item_ptr_id
GROUP BY char_inv.character_id
);
'''
result2 = cursor.execute(query).fetchall()
print ('Average weapon per character:',result2[0])

# --Characters per class
query = '''
SELECT  (
    SELECT COUNT(character_ptr_id)
    FROM   charactercreator_cleric
    ) AS 'Total Clerics',
    (
    SELECT COUNT(character_ptr_id)
    FROM   charactercreator_fighter
    ) AS 'Total Fighters',
    (
    SELECT COUNT(character_ptr_id)
    FROM   charactercreator_mage
    ) AS 'Total Mages',
    (
    SELECT COUNT(character_ptr_id)
    FROM   charactercreator_thief
    ) AS 'Total Thieves',
    (
    SELECT COUNT(mage_ptr_id)
    FROM   charactercreator_necromancer
    ) AS 'Total Necromancers';
'''
result2 = cursor.execute(query).fetchall()
print ('Characters per class:',result2)