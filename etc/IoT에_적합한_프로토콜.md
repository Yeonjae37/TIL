IoT 시스템 구성 목적
- 데이터 주체
- 데이터 흐름(방향)
- 데이터 양, 전송 주기

## 구조적 차이
HTTP : Server - Client 구조
MQTT : Publisher - Broker - Subscriber 구조. 양방향 통신 가능 -> 하나의 디바이스가 Subscriber, Publisher 둘 다 가능하다는 말.

## 연결 유지 방식 차이
HTTP : 데이터를 주고 받아야할 때, Client에서 연결을 위한 데이터를 주고 받은 후, 실제 데이터를 주고 받음. MQTT에 비해 데이터 트래픽이 큼.
MQTT : Broker와 Client가 계속 연결을 유지하고 있음. 연결을 유지하고 있다가 언제든 데이터를 주고 받을 수 있는 구조