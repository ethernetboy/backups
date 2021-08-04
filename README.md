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
` /home/user/backupsw/<ip>`

* A variável <ip> deve ser substituída pelo ip do switch. Ex: 10.10.10.1

#### Configurações Requeridas

Para que ocorra a comunicação via Git, necessitamos adicionar dentro do diretório backupsw os repositório remoto, isso pode ser feito através dos comandos:

```bash 
$ git init
$ git remote add origin <url_do_git_usando_ssh>
```

* Toda a configuração foi feita com base em autentição com chaves então para o backup ser realizado no GIT devemos colocar a chave (privada) configurada préviamente no GIT. O nome da chave deve ser: id_rsa

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

    


 
    
    


    
    
    
   

