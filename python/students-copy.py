# Your code goes here
import csv  
import re
import json
def getData(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = []
        for row in csv_reader:
            student = {"firstName": row[0], "lastName": row[1], "email": row[2], "birthDate": row[3], "degree": row[4], "role": row[5]}
            data.append(student)
    return data

def getDegrees(data):
    degrees={}
    for student in data:
        degrees[student['degree']] = "dummy" 
    return degrees.keys()

def userPerDegrees(degrees,data):
    userPerDegrees={}
    for item in degrees:
        userPerDegrees[item] = {}
    for student in data:
        if (student['role'] in userPerDegrees[student['degree']]) :
            userPerDegrees[student['degree']][student['role']] += 1
        else :
            userPerDegrees[student['degree']][student['role']] = 0    
    return userPerDegrees

if __name__ == "__main__":

    filename = 'students.csv'
    # Ecrivez une fonction permettant de récupérer toutes les lignes
    # du fichier CSV dans une list() `data`
    data = getData(filename)
    print(f'\nLe fichier brut contient {len(data)} lignes')

    # Les étudiants ont chacun un diplôme qui leur est attribué
    # La variable `degrees` contient la liste des diplômes
    degrees = getDegrees(data)
    print(f'\nLe fichier contient {len(degrees)} diplômes uniques')

    # # Donnez, dans un dict, pour chaque diplôme le nombre d'étudiant
    # # par catégorie d'utilisateur (student, alumni, ...)
    users_per_degree = userPerDegrees(degrees,data)
    print(f'\nLa répartition des diplômes est la suivante :')
    for degree in users_per_degree.keys():
        print(f' - {degree}, {users_per_degree[degree]} étudiants')

    # Enregistrez le dictionnaire dans un nouveau fichier `degree_count.json`
    with open("degree_count.json","w") as write_file: 
        json.dump(users_per_degree,write_file)
    print(f'\nFichier `degree_count.json` enregistré !')