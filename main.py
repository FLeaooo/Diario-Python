import os
from pathlib import Path
from datetime import datetime
from datetime import timedelta
from ..att_private import caminho_diario

def qual_semana_ano():
    # Pega a data de hoje com o datetime
    current_date = datetime.now()
    # Recebe a da do ano em str 2023
    year_date = current_date.strftime('%Y')
    day_dmy = current_date.strftime('%d/%m/%Y')

    # A data da semana em str e %U considera o primeiro dia como sendo domingo
    week_date = current_date.strftime('%U')
    name_folder = f'Semana_{str(week_date)}-{str(year_date)}'
 
    # Domingo-03/12/2023 e Semana_49-2023
    return name_folder, day_dmy


def criar_pasta(path_folder_diario):
    # Ler todos os arquivos dentro da pasta
    item = os.listdir(path_folder_diario)
    # Funcao que recebe a string semana_49-2023
    name_folder, day_dmy = qual_semana_ano()

    # Recebe o caminho junto ao nome que a pasta deve ter
    path_folder_semana = os.path.join(path_folder_diario, name_folder)

    # Verifica se dentro da pasta ja tem esta semana criada
    if name_folder in item:
        print('Pasta da semana ja existe')
        return False
    # Caso nao tenha ele ira criar 
    else:
        
        # Cria a pasta
        os.makedirs(path_folder_semana, exist_ok=True)
        
        # Criar arquivos
        criar_paginas_semana(name_folder, day_dmy, path_folder_semana)
        
        
        print('Pasta da semana criada')
        return True


def criar_paginas_semana(name_folder, day_dmy, path_folder_semana):
    templ_day_path = r"C:\FernandoLeao\Programacao\Projetos\Cria_Diario\template_diario.txt"
    templ_week_path = r"C:\FernandoLeao\Programacao\Projetos\Cria_Diario\template_semana.txt"
    with open(templ_day_path, 'r') as file_day:
        templ_day_cont = file_day.read()
    with open(templ_week_path, 'r') as file_week:
        templ_week_cont = file_week.read()
    
    
    print(f"Date str {day_dmy}")  #Monday-04/12/2023
    print(f"name_folder {name_folder}")  #Semana_49-2023

    dict_semana = {
        0: name_folder,
        1: "Sunday",
        2: "Tuesday",
        3: "Wdnesday",
        4: "Thursday",
        5: "Wednesday",
        6: "Friday",
        7: "Saturday"
    }
    dia_semana = get_domingo(day_dmy)

    # Coloco o dia que eu recebi para domingo
    
    for i in range(8):
        if i == 0:
            path_arquivo = os.path.join(path_folder_semana, str(i) + name_folder + ".txt")
            conteudo_semana_recolocado = templ_week_cont.replace('X', dict_semana[i])
            with open(path_arquivo, "w") as file:
                file.write(conteudo_semana_recolocado)
        else:
            cabecalho_dia = f"{dict_semana[i]}-{dia_semana}"
            path_arquivo = os.path.join(path_folder_semana, str(i) + dict_semana[i] + ".txt")
            conteudo_dia_recolocado = templ_day_cont.replace('X', dict_semana[i])
            
            dia_semana_dt = datetime.strptime(dia_semana, "%d/%m/%Y")
            dia_semana_dt = dia_semana_dt + timedelta(days=1)
            dia_semana = dia_semana_dt.strftime("%d/%m/%Y")
            
            with open(path_arquivo, "w") as file:
                file.write(conteudo_dia_recolocado)
    

def get_domingo(data_recebida):
    data = datetime.strptime(data_recebida, "%d/%m/%Y")
    
    dia_semana = data.weekday() + 1

    domingo_previsto = data - timedelta(days=dia_semana)
        
    domingo_previsto = domingo_previsto.strftime("%d/%m/%Y")
    
    return domingo_previsto


path_folder_diario = caminho_diario

criar_pasta(path_folder_diario)
