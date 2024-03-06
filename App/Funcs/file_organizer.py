import os
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from time import sleep

def fileOrganizer():
  try:
    path = askdirectory(title='Abrir Pasta')

    file_list = os.listdir(path)


    locations = {
        'imagens': ['.png','.jpeg','.jpg','.bmp'],
        'planilhas': ['.xlsx','.xlsm','.xlsb','.sltx','.xltm','.xls','.csv'],
        'documentos': ['.doc','.docx','.pdf','.txt'],
        'compactados': ['.zip','.rar','.7z','.tar','.tar.gz'],
        'executaveis': ['.exe','.bat','.msi'],
        'audios': ['.mp3','.wav','.flac','.aac','.aiff'],
        'videos': ['.avi','.wmv','.mov','.qt','.mk  v','.mp4'],
    }


    for file in file_list:
        name, extensions = os.path.splitext(f'{path}/{file.lower()}')
        
        for folder in locations:
            if extensions in locations[folder]:
                if not os.path.exists(f'{path}/{folder}'):
                    os.mkdir(f'{path}/{folder}')
                    
                os.rename(f'{path}/{file}', f'{path}/{folder}/{file.lower()}')

    sleep(1.5)
    messagebox.showinfo('File Organizer','Todos os arquivos foram organizados.')

  except: 
    messagebox.showwarning('File organizer','O sistema não pode encontarar o caminho especeficado')




if __name__ == "__main__":
    fileOrganizer()