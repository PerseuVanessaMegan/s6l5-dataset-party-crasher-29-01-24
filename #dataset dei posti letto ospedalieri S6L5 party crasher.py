#dataset dei posti letto ospedalieri 
#calcolo il totale per tipo di struttura e per tipo di regione
#calcolo anche la media, mediana, minimo, massimo del dataset
#importo prima le librerie e carico il file

import pandas as pd
import matplotlib.pyplot as plt


#importiamo il file csv
path="./Posti_letto_per_struttura_ospedaliera_2020.csv"
data=pd.read_csv(path, sep=";",encoding="ISO-8859-15")



#selezioniamo le colonne che mi servono per rispondere alla domanda: quanti posti letto per regione?
Colonne = ['Descrizione Regione' , 'Totale posti letto' ]
dataColonne = data[Colonne]
print(dataColonne.head())

#raggruppo e sommo
sommaPosti = dataColonne.groupby('Descrizione Regione')['Totale posti letto'].sum().reset_index()
print(sommaPosti)


#grafico
x = sommaPosti['Descrizione Regione']
y = sommaPosti['Totale posti letto']
plt.figure(figsize=(6,4))
plt.barh(x, y)
plt.title('Tot Posti letto per regione')
plt.xlabel('Posti letto')
plt.ylabel('Regione')
plt.show()




#calcolo il totale per tipo di struttura e per tipo di regione
posti_per_tipo_struttura = data.groupby(["Descrizione Regione" , "Descrizione tipo struttura"]) ["Totale posti letto"].sum().reset_index()
print(posti_per_tipo_struttura)
#calcolo la media per tipo di struttura e per regioni
media_tipo_struttura = data.groupby(["Descrizione tipo struttura", "Descrizione Regione"]) ["Totale posti letto"].mean().reset_index()
print(media_tipo_struttura)



#somma posti letto per disciplina
SommaPostiDisciplina = data.groupby(['Tipo di Disciplina'])['Totale posti letto'].sum().reset_index()
print(SommaPostiDisciplina)
plt.pie(SommaPostiDisciplina["Totale posti letto"],labels=SommaPostiDisciplina["Tipo di Disciplina"])
plt.show()


#massimo e minimo per regione
somma_Posti = data.groupby(['Descrizione Regione'])["Totale posti letto"].sum().sort_values(ascending=True)
max = somma_Posti[-1:]   #seleziono l'ultima riga per ottenere il massimo
min = somma_Posti[0:1]   #seleziono la prima per ottenere il minimo
print(min)
print(max)



#per trovare il numero dei posti letto suddivisi per regione e per tipo di disciplina:
posti_letto=data.loc[:,["Descrizione Regione","Tipo di Disciplina","Totale posti letto"]]
tabella_tipo_disciplina_regioni=posti_letto.groupby(["Descrizione Regione","Tipo di Disciplina"]).sum("Totale posti letto").reset_index()
print(tabella_tipo_disciplina_regioni)


#per trovare le discipline che hanno il numero più alto di posti letto in ogni regione:
regione_max=posti_letto.groupby(["Descrizione Regione","Tipo di Disciplina"]).sum().sort_values(by="Totale posti letto",ascending=False).reset_index()
print(regione_max.head())


#per trovare le discipline che hanno il numero più basso di posti letto in ogni regione:
print(regione_max.tail())

