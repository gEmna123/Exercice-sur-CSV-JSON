import pandas as pd

def csv_to_json(csv_file):
    # Lire le fichier CSV avec pandas
    df = pd.read_csv(csv_file, encoding='latin1')

    # Créer un dictionnaire à partir du DataFrame
    data_dict = {}
    
    for index, row in df.iterrows():
        my_dict = {
            'Test 1': row['Test 1'],
            'Test 2': row['Test 2']
        }
        data_dict[row['Prenom et nom']] = my_dict

    print("====================")
    my_my_dict = {'test': data_dict}
    print(my_my_dict)

    # Convertir le DataFrame directement en JSON
    csv_rows = df.to_dict(orient='records')
    
    print("====================")
    data_dict = {'test': csv_rows}
    print(data_dict)

    # Convertir les dictionnaires en objets JSON
    y = pd.Series(my_my_dict).to_json()
    z = pd.Series(data_dict).to_json()

    print("====================")
    print(y)
    print(type(y))
    print("====================")
    print(z)
    print(type(z))

# Étape 1
csv_to_json("test.csv")
