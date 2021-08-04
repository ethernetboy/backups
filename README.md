## Script para Backup de Switches


### Description:

Este repositório contém o script para gerar arquivos de backup dos switches referenciados no arquivo cisco.txt.

### Setup

#### Pré Requisitos

Faça o download do projeto disponível neste repositório.

Para a execução do script é necessário a utilização do docker, que pode ser encontrado no link abaixo:

* docker: https://docs.docker.com/get-docker/


Todos os módulos necessários para a execução do projeto instalados a partir do arquivo `requirements.txt`.

#### Montando a imagem docker

Dentro do diretório do projeto execute:

```bash
$ docker build -t backup .
```


### Diretórios Locais

Para o correto armazenamento dos backups é necessário que tenhamos a estrutura de diretórios abaixo:
` /home/user/backupsw/sw_ip`

#### Configurações Requeridas

Para que ocorra a comunicação via Git, necessitamos adicionar dentro do diretório backupsw os comandos: git init / git remote add origin <url_do_git_usando_ssh>) e (chave ssh para acessar o repositório).

#### Executando o script via docker

Para a execução do script necessitamos executar o comando abaixo:
```bash
$ docker run -it -v /home/user/backupsw/:/var/backupsw/ backup
```

#### Futuras melhorias

Neste projeto ainda podemos adicionar os elementos abaixo para obter uma melhor experiênicia:

- Execução agendada via CRON.
- Criação automática de diretórios
- Auto-discover de novos switches.

    


 
    
    


    
    
    
   

