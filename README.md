# Web Crawler
>Bot web crowler criado com objetivo de coletar e armazenar especificações de hardware de máquinas oferecidas por serviços de cloud.

## Descrição
O objetivo do projeto é fazer um app que acesse o site da [Vultr](https://www.vultr.com/pricing/) e da [DigitalOcean](https://www.digitalocean.com/pricing/#droplet) via Scrapy, acesse os valores de **Memória**, **CPU**, **Armazenamento** e **Preço** de maneira limpa, salve esses dados em arquivos **.JSON** e **.CSV**.
Optei por escrever o output em formato JSON Lines pois não é uma boa prática fazer inserções num arquivo json que já foi finalizado, o formato jsonL é ideal para esse tipo de operação com incontáveis inserções. Como pode haver necessidade de usar os dados em uma API que recebe os dados em formato json tradicional, o programa converte o jsonl para json no fim da operação utilizando o **jq**.

## Features
* Acessa o site da Digital Ocean e exibe os dados no terminal
* Salva os dados em formato JSONL e CSV

## Dependências
```
Asn1crypto       0.24.0
Attrs            19.1.0
Automat          0.7.0  
Cffi             1.12.3
Constantly       15.1.0
Cryptography     2.6.1  
Cssselect        1.0.3  
Hyperlink        19.0.0
Idna             2.8    
Incremental      17.5.0
Jq               1.6.0
Lxml             4.3.3  
Parsel           1.5.1  
Pip              19.1.1
Pyasn1           0.4.5  
Pyasn1-modules   0.2.5  
Pycparser        2.19   
PyDispatcher     2.0.5  
PyHamcrest       1.9.0  
PyOpenSSL        19.0.0
Python           3.7.3
Queuelib         1.5.0  
Scrapy           1.6.0  
Service-identity 18.1.0
Setuptools       41.0.1
Six              1.12.0
Twisted          19.2.0
W3lib            1.20.0
Wheel            0.33.3
Zope.interface   4.6.0  
```
Este web crawler foi testado apenas em ambiente Linux (kernel 4.19.36-1).

## Instalação
Siga os seguintes passos:
1. Crie uma pasta para o app na sua máquina.
1. Instale o `jq`:
  * `sudo pacman -S jq` para distribuições Arch
  * `sudo apt install jq` para distribuições Debian
  * Para demais distribuições consultar as dependências oficiais ou baixar diretamente do [site oficial jq](https://stedolan.github.io/jq/download/)
1. Execute `virtualenv .venv` para criar um ambiente virtual e `source ./venv/bin/activate` para ativá-la.
1. Baixe o aplicativo rodando `git clone https://github.com/filipedeschamps/video-maker.git`.
1. Execute `pip install -r requirements.txt` para baixar as dependências.
1. Dê permissão de execução ao arquivo `main.py` rodando `sudo chmod 777 main.py`

Agora está tudo pronto para rodar o aplicativo, execute `./main.py`.

Sua saída será semelhante a essa:
![](https://raw.githubusercontent.com/tamercuba/Web-Crawler/master/static/output_print.png)
A saída também está salva nos arquivos `static/maquinas.jsonl` e `static/maquinas.csv`.

## Histórico de versões

* v0.4 - ATUAL
* [v0.3](https://github.com/tamercuba/Web-Crawler/tree/v0.2)
* [v0.2](https://github.com/tamercuba/Web-Crawler/tree/v0.2)
* [v0.1](https://github.com/tamercuba/Web-Crawler/tree/v0.1)

## Contato
* [LinkedIn](https://linkedin.com/in/tamercuba)
* [Facebook](https://www.fb.com/tamercuba)
* E-mail: `tamercuba@gmail.com`
