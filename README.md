# FilOr

## Funcionamento

Utilizando uma janela de selecão de diretórios para que o usuário possa selecionar uma pasta par que os arquivos dela sejam organizados. O **_FilOr_** utiliza sub pastas criadas para organizar cada tipo de arquivo usando como base o tipo de extenção do mesmo, um exemplo seria da pasta de planilhas que dentro teriam arquivos com as extenções xlsx, xls, xlsm, etc..., dessa forma o FilOr consegue organizar pelo tipo e não por extenção do arquivo.
Ao final da execução do programa, ele abre um popup com uma menssagem dizendo "Todos os arquivos já foram organizado" e ao pressionar "Ok" ele o fecha. Se caso a janela de seleção de diretórios for fechada antes de selecionar algum, aparecerá um popup de aviso disendo "O sistema não pode encontrar o caminho especificado."

---

## Tecnologias usadas

Basicamente o FilOr foi feito com apenas as bibliotecas padrão do Python, sem a necessidade de instalar bibliotecas de terceiros. As bibliotecas usadas foram:

- **Tkinter** -> O tkinter foi utilizado para a criação da janela de seleção de diretório usando a função **askdirectory()** e para fazer os popups com o módulo messagebox com as funções **showinfo()** para o popup de finalização e **showwarning()** para o popup de alerta.

- **Os** -> A biblioteca "os" foi usada para identificar os arquivos dentro das pastas, separar o nome do arquivo da extenção dele, verificar a existencia de uma pasta que já pudesse ser utilizada para adicionar algum tipo de arquivo, criação de pastas não existentes para realizar a organização dos arquivos e reorganização de arquivos dentro de casa pasta especificada.

- **Time** -> A biblioteca "time" foi usada apenas para importar a função sleep, essa função foi usada para dar um pequeno atraso de 1,5 segundos(um segundo e meio) antes que fosse mostrada o popup de finalização do programa, pois o popup estava aparecendo assim que o código terminada de organizar os arquivos e não dps que os arquivos já estavam visiveis dentro de cada pasta. Com isso ficou mais claro para o usuário quando o programa realmente estava finalizado.

---

## Arquivos

- O arquivo *file_organizer.py* é um arquivo que guarda a função de organizar arquivos.
- O arquivo _main.py_ é usado para a criação da GUI para a interação do usuário.

---

## Futuras atualizações

- [ ] Adicionar uma tela de loading para que fique claro ao usuário que o programa ainda está em execução.
- [ ] Adicionar uma GUI para que o usuário possa interagir.
- [ ] Adicionar funções de adicionar e deletar extenções.
- [ ] Adicionar um BD para guardar as extenções já existentes e futuras.
- [ ] Adicionar funçoes para salvar configurações pré definidas pelo usuário.
- [ ] Adicionar função para criar apenas diretórios sem a necessidade de movimentar arquivos.
