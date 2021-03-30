#!/usr/bin/python3

from google.cloud import monitoring_v3
from google.cloud.monitoring_v3 import query
import datetime
import sys
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('/usr/lib/zabbix/externalscripts/service_acc_key.json')

try:
    project_id=sys.argv[1]
    metric_type=sys.argv[2]
    resource_label_key= sys.argv[3]
    resource_label_value= sys.argv[4]
    value_type= sys.argv[5].lower()
    try:
        period=sys.argv[6]
    except:
        period=5
except:
    print("Usage: stackdriver-zabbix.py ProjectID MetricType ResourceLabelKey ResourceLabelValue ValueType(int64 or double) Period(Opcional) \n")
    print("Example: ./stackdriver-zabbix.py 'dialog-western-union' 'cloudsql.googleapis.com/database/cpu/utilization' 'database_id' 'dialog-western-union:cm-dial-carrefour-prod-read-replica' 'double'") 
    sys.exit()
client = monitoring_v3.MetricServiceClient(credentials=credentials)

def get_metric():
    query_result = query.Query(client,
                            project=project_id,
                            metric_type=metric_type,
                            minutes=period)
    values = []
    for result in query_result:
        if result.resource.labels[resource_label_key] == resource_label_value:
            for time_serie in result.points:
                if value_type == "int64":
                    values.append(time_serie.value.int64_value)
                    return  int(sum(values)/len(values))
                elif value_type == "double":
                    values.append(time_serie.value.double_value)
                    return "%0.4f" % (sum(values)/len(values))

print(get_metric())
