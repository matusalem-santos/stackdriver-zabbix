# Objetivo

Monitorar os serviços da GCP pelo Zabbix consultando a API do Stackdriver

# Dependencias 

- Python 3.6 ou maior
- Pip3 21.0 ou maior (Caso esteja em uma versão menor, executar: **pip3 install --upgrade pip**)
- google-cloud-monitoring 1.1.0 (Executar: **pip3 install google-cloud-monitoring==1.1.0**)

# Referência 

- [Documentação Google](https://cloud.google.com/monitoring/api/metrics_gcp)

# Como utilizar 

- Criar um Service Account com a Role **Monitoring Admin** 

 <img src="http://i.imgur.com/OvUXE41.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

- Enviar o arquivo gerado com as credenciais do Service Account para a maquina do Zabbix no caminho: **/usr/lib/zabbix/externalscripts**
- Renomar o arquivo com as credenciais do Service Account para **service_acc_key.json**
- Enviar o script [stackdriver-zabbix.py](stackdriver-zabbix.py) para a maquina do Zabbix no caminho: **/usr/lib/zabbix/externalscripts**
- Dar permissão de execução no script **stackdriver-zabbix.py**
```bash
    sudo chmod +x /usr/lib/zabbix/externalscripts/stackdriver-zabbix.py
``` 
#### Parâmetros do script

| Posição | Nome | Obrigatório |
| ------- | ---- |:---------: |
| 1 | Project ID | Sim |
| 2 | Metric Type | Sim |
| 3 | Resource Label Key | Sim |
| 4 | Resource Label Value | Sim |
| 5 | Value type(**int64** ou **double**) | Sim |
| 6 | Period | Não |

- **Project ID** - ID do Projeto que será monitorado. Exemplo: 

 <img src="http://i.imgur.com/Jd3ndCf.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

- **Metric Type** - Um identificador para o tipo de métrica. Exemplo:

 <img src="http://i.imgur.com/Fn5j9Fh.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

- **Resource Label Key** - Um classificador para realizar um filtro. Exemplo: 

 <img src="http://i.imgur.com/jB79UgW.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

- **Resource Label Value** - Um valor do classificador para filtrar um único componente . Exemplo:

 <img src="http://i.imgur.com/eYZcrbF.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

- **Value Type** - O tipo do valor da métrica. Exemplo: **int64** ou **double**

 <img src="http://i.imgur.com/ujysdqK.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

- **Period** - O período determina o intervalo de tempo para o qual a agregação ocorre. Exemplo:

 <img src="http://i.imgur.com/fKj3XbE.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

#### Execução

- Executar o script **stackdriver-zabbix.py** passando os parâmetros:
```bash
    /usr/lib/zabbix/externalscripts/stackdriver-zabbix.py ProjectID MetricType ResourceLabelKey ResourceLabelValue ValueType(int64 ou double) Period(Opcional)
``` 
- Exemplo: 
```bash
    /usr/lib/zabbix/externalscripts/stackdriver-zabbix.py 'project-id' 'cloudsql.googleapis.com/database/cpu/utilization' 'database_id' 'project-id:db-prod-read-replica' 'double'
``` 

