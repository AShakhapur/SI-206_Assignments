import unittest
import sqlite3
import json
import os
# starter code

# Create Database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn


# Creates list of species ID's and numbers
def create_species_table(cur, conn):

    species = ["Rabbit",
    "Dog",
    "Cat",
    "Boa Constrictor",
    "Chinchilla",
    "Hamster",
    "Cobra",
    "Parrot",
    "Shark",
    "Goldfish",
    "Gerbil",
    "Llama",
    "Hare"
    ]

    cur.execute("DROP TABLE IF EXISTS Species")
    cur.execute("CREATE TABLE Species (id INTEGER PRIMARY KEY, title TEXT)")
    for i in range(len(species)):
        cur.execute("INSERT INTO Species (id,title) VALUES (?,?)",(i,species[i]))
    conn.commit()

# TASK 1
# CREATE TABLE FOR PATIENTS IN DATABASE
def create_patients_table(cur, conn):
    pets_json = json.load("pets.json")

    cur.execute("DROP TABLE IF EXISTS Species")
    cur.execute("CREATE TABLE Patients (pet_id INTEGER PRIMARY KEY, name TEXT, species_id INTEGER, age INTEGER, cuteness INTEGER, aggressiveness NUMBER)")
    conn.commit()
    


# ADD FLUFFLE TO THE TABLE
def add_fluffle(cur, conn):
    cur.execute("INSERT INTO Patients")
    cur.execute("VALUES (0, Fluffle, 0, 3, 90, 100)")
    conn.commit()
    

# TASK 2
# CODE TO ADD JSON TO THE TABLE
# ASSUME TABLE ALREADY EXISTS
def add_pets_from_json(filename, cur, conn):
    
    # WE GAVE YOU THIS TO READ IN DATA
    f = open(filename)
    file_data = f.read()
    f.close()
    json_data = json.loads(file_data)

    # THE REST IS UP TO YOU
    for i in range(len(json_data)):
        curr.execute("SELECT id FROM Species WHERE title = ?", json_data[i]['species'])
        my_species = int(cur.fetchone()[0])
        my_name = json_data[i]['name']
        my_age = int(json_data[i]['age'])
        my_cuteness = int(json_data[i]['cuteness'])
        my_aggressiveness = int(json_data[i]['aggressiveness'])
        my_pet_id = i+1
        cur.execute("INSERT INTO Patients (pet_id, name, species_id, age, cuteness, aggressiveness) VALUES (?, ?, ?, ?, ?, ?)",(my_pet_id, my_name, my_species, my_age, my_cuteness, my_aggressiveness))
    conn.commit()    


# TASK 3
# CODE TO OUTPUT NON-AGGRESSIVE PETS
def non_aggressive_pets(aggressiveness, cur, conn):
    pass

# TASK 4 (Optional)
# CODE TO PRINT OUT NUMBER OF PATIENTS OF EACH SPECIES
def number_of_each_species(cur, conn):
    pass


def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('animal_hospital.db')
    create_species_table(cur, conn)


    # YOUR TASKS
    
    
if __name__ == "__main__":
    main()

