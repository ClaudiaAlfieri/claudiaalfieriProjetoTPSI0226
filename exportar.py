import csv

def exportar_csv(filmes):
    if len(filmes) == 0:
        print("Nenhum filme registado.")
        return
    with open("pyflix_export.csv", "w", newline="", encoding="utf-8-sig") as ficheiro:
        writer = csv.writer(ficheiro, delimiter=";")
        writer.writerow(["id", "titulo", "tipo", "genero", "ano", "plataforma", "nota", "data_visualizacao", "comentario"]) 
        for filme in filmes:
            writer.writerow([filme["id"], filme["titulo"], filme["tipo"], filme["genero"], filme["ano"], filme["plataforma"], filme["nota"], filme["data_visualizacao"], filme["comentario"] ])
    print("Dados exportados com sucesso para pyflix_export.csv!")
            
            
