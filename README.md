# Atividade de LNPG - Turma 2023.2

Atividade: Fazer um sistema para cadastrar e listar álbuns musicais

## Versão 1.0

- Criar uma tela de cadastro de informações do álbum. As seguintes informações são necessárias: nome do álbum, ano de lançamento, nome da banda/artista, álbum lançamento do artista (sim/não);

- Criar uma tela que liste todos os álbuns cadastrados na sua base de dados.

## Versão 2.0

- Criar uma tela de busca de álbuns pelo nome do artista. Basicamente, a tela terá um campo de texto e um botão de busca. O  nome digitado pelo usuário pode corresponder a parte do nome do  artista. Ex. O usuário digita “ME” e clica em buscar. O sistema retorna  os álbuns do “METALLICA”, “MEGADETH”, “LIMÃO COM MEL”, etc; 

-  Criar uma tela de busca de álbuns pelo ano do álbum. A tela terá um  radiobutton com as opções: “Anterior a”, “Posterior a”, “Igual a”. E uma  combobox com a listagem dos anos. Ex. Ao selecionar o radiobutton “Anterior a” e a opção de ano 2000. O sistema deve retornar todos os  álbuns cadastrados com ano até 2000 (2000 incluso). 


## Versão 3.0 

- O seu sistema está muito acoplado. As divisão em camadas (GUI x Regra de  Negócio x Acesso a Dados) não está clara. 

- Coloque TODO seu código dentro de funções e use o __main__ para iniciar a  execução do seu sistema (veja tutorial aqui) 

- Altere o seu sistema para que fique em 3 módulos Python separados (veja mais  sobre módulos aqui): gui.py, domain.py, db.py. Dentro de cada módulo deve conter apenas o código referente a sua funcionalidade. Ex. o módulo gui.py deve  ter o código referente a biblioteca tkinter. O módulo bd.py deve ter as funções para manipular arquivos. O módulo domain.py deve ter a regra de negócio. 

- **IMPORTANTE:** O módulo gui.py deve “conversar” com o módulo domain.py e o  módulo domain.py deve conversar com o módulo db.py. O módulo gui.py NÃO  pode conversar com db.py. Isso viola a divisão das camadas.  
39
