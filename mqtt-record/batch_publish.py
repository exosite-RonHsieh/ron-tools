from paho.mqtt import client as mqtt
from datetime import datetime
import ssl
import json
import time
import random

# Set your product id and device token
product_id = "i51k2rkarveg00000"
device_token = "0ebf9c2a1af79fd2f5b2036941b8e4b47d4fcc74"
host = product_id + ".m2.exosite.io"
cert = "./trusted.crt"

def on_connect(client, userdata, flags, rc):
    timestamp = int(time.time())
    data1= random.randint(40, 60)
    data2= random.randint(1, 30)
    resource = "$resource.batch"
    config_io = [{"timestamp": timestamp, "values": {"config_io": '{"last_edited":"2019-10-15T18:00:00+09:00","channels":{"air_temp1":{"display_name":"空調機入口DB","description":"空調機入口DB","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"TEMPERATURE", "data_unit":"DEG_CELSIUS","min":-30.0, "max":80.0, "precision":1}},"air_temp2":{"display_name":"空調機出口DB","description":"空調機出口DB","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"TEMPERATURE", "data_unit":"DEG_CELSIUS","min":-30.0, "max":80.0, "precision":1}},"thermistor1":{"display_name":"冷却コイル入口水温","description":"冷却コイル入口水温","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"TEMPERATURE", "data_unit":"DEG_CELSIUS","min":0.0, "max":80.0, "precision":1}},"thermistor2":{"display_name":"冷却コイル出口水温","description":"冷却コイル出口水温","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"TEMPERATURE", "data_unit":"DEG_CELSIUS","min":0.0, "max":80.0, "precision":1}},"thermistor3":{"display_name":"加熱コイル入口水温","description":"加熱コイル入口水温","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"TEMPERATURE", "data_unit":"DEG_CELSIUS","min":0.0, "max":80.0, "precision":1}},"thermistor4":{"display_name":"加熱コイル出口水温","description":"加熱コイル出口水温","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"TEMPERATURE", "data_unit":"DEG_CELSIUS","min":0.0, "max":80.0, "precision":1}},"diff_press1":{"display_name":"フィルタ前後差圧","description":"フィルタ前後差圧","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"PRESSURE", "data_unit":"PASCAL","min":-2500, "max":2500, "precision":0}},"diff_press2":{"display_name":"コイル前後差圧","description":"コイル前後差圧","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"PRESSURE", "data_unit":"PASCAL","min":-2500, "max":2500, "precision":0}},"diff_press3":{"display_name":"SAファン前後差圧","description":"SAファン前後差圧","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"PRESSURE", "data_unit":"PASCAL","min":-2500, "max":2500, "precision":0}},"elec_current1":{"display_name":"SAモータ電流値","description":"SAモータ電流値","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"ELEC_CURRENT", "data_unit":"AMPERE","min":0.0, "max":250.0, "precision":1}},"air_flow1":{"display_name":"SAオリフィス差圧","description":" SAオリフィス差圧","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"PRESSURE", "data_unit":"PASCAL","min":-500.000, "max":500.000, "precision":3}},"air_humid1":{"display_name":"空調機入口相対湿度","description":"空調機入口相対湿度","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"NUMBER","min":0.0, "max":100.0, "precision":1}},"air_humid2":{"display_name":"空調機出口相対湿度","description":"空調機出口相対湿度","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"NUMBER","min":0.0, "max":100.0, "precision":1}},"air_speed1":{"display_name":"SA風速","description":"SA風速","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"VELOCITY", "data_unit":"METER_PER_SEC","min":0.000, "max":20.000, "precision":3}},"enthalpy1":{"display_name":"空調機入口エンタルピー","description":"空調機入口エンタルピー","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"NUMBER","min":-100.00, "max":100.00, "precision":2}},"enthalpy2":{"display_name":"空調機出口エンタルピー","description":"空調機出口エンタルピー","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"NUMBER","min":-100.00, "max":100.00, "precision":2}},"op_status":{"display_name":"運転状態値","description":"運転状態値","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"NUMBER","min":0, "max":1, "precision":0}},"op_time":{"display_name":"積算運転時間","description":"積算運転時間","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"NUMBER","min":0, "max":3600, "precision":0}},"op_status_str":{"display_name":"運転状態","description":"運転状態","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"STRING"}},"report_time":{"display_name":"最終報告時刻","description":"最終報告時刻","protocol_config":{"report_rate":60000, "sample_rate":10000, "timeout":180000},"properties":{"data_type":"STRING"}},"v_fail_rate":{"display_name":"SAファン状態スコア(振動)","description":"SAファン状態スコア(振動)","protocol_config":{"report_rate":60000, "sample_rate":60000, "timeout":180000},"properties":{"data_type":"NUMBER","min":0.0, "max":100.0, "precision":1}},"vibr_ave":{"display_name":"SAファン振動OA値(平均値)","description":"SAファン振動OA値(平均値)","protocol_config":{"report_rate":60000, "sample_rate":60000, "timeout":180000},"properties":{"data_type":"ACCELERATION", "data_unit":"METER_PER_SEC2","min":0.0, "max":100.0, "precision":1}},"vibr_max":{"display_name":"SAファン振動OA値(最大値)","description":"SAファン振動OA値(最大値)","protocol_config":{"report_rate":60000, "sample_rate":60000, "timeout":180000},"properties":{"data_type":"ACCELERATION", "data_unit":"METER_PER_SEC2","min":0.0, "max":100.0, "precision":1}},"vibr_min":{"display_name":"SAファン振動OA値(最小値)","description":"SAファン振動OA値(最小値)","protocol_config":{"report_rate":60000, "sample_rate":60000, "timeout":180000},"properties":{"data_type":"ACCELERATION", "data_unit":"METER_PER_SEC2","min":0.0, "max":100.0, "precision":1}},"vibr_dev":{"display_name":"SAファン振動OA値(分散値)","description":"SAファン振動OA値(分散値)","protocol_config":{"report_rate":60000, "sample_rate":60000, "timeout":180000},"properties":{"data_type":"NUMBER","min":0.0, "max":10000.0, "precision":1}}}}'}}]
    data_in_1 = [{"timestamp": timestamp, "values": {"data_in": '{"vibr_ave": %s,"vibr_max": %s,"vibr_min": %s,"vibr_dev": %s}'% (data1,data1,data1,data1)}}]
    data_in_2 = [{"timestamp": timestamp, "values": {"data_in": '{"air_temp1": %s,"air_temp2": %s,"thermistor1": %s,"thermistor2": %s,"thermistor3": %s,"thermistor4": %s,"diff_press1": %s,"diff_press2": %s,"diff_press3": %s,"elec_current1": %s,"air_flow1": %s,"air_humid1": %s,"air_humid2": %s,"air_speed1": %s,"enthalpy1": %s,"enthalpy2": %s,"op_status": %s,"op_time": %s,"op_status_str": %s,"report_time": %s,"v_fail_rate": %s}'% (data2, data2, data2, data2, data2, data2, data2, data2, data2, data2, data2, data2, data2, data2, data2, data2, data2, data2, data2, data2, data2)}}]

    client.publish(resource, json.dumps(config_io), qos=0)
    client.publish(resource, json.dumps(data_in_1), qos=0)
    client.publish(resource, json.dumps(data_in_2), qos=0)
    print ("publish down at " + datetime.now().strftime("%H:%M:%S"))
    client.disconnect()

def on_message(client, userdata, msg):
 print("Value set, previous was: ", msg.payload.decode())

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("DisConnected with error", rc)
        exit()

client = mqtt.Client(client_id="")
client.tls_set(
    ca_certs=cert,
    server_hostname=host,
    cert_reqs=ssl.CERT_NONE
)
client.tls_insecure_set(True)
client.username_pw_set("", device_token)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect(host, 443)
client.loop_forever()