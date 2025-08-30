```bash
brew install mosquitto
brew services start mosquitto
```

```bash
# Broker
(base) yeonjae-jeong@jeong-yeonjaeui-MacBookAir ~ % mosquitto
1734867444: mosquitto version 2.0.20 starting
1734867444: Using default config.
1734867444: Starting in local only mode. Connections will only be possible from clients running on this machine.
1734867444: Create a configuration file which defines a listener to allow remote access.
1734867444: For more details see <https://mosquitto.org/documentation/authentication-methods/>
1734867444: Opening ipv4 listen socket on port 1883.
1734867444: Opening ipv6 listen socket on port 1883.
1734867444: mosquitto version 2.0.20 running
1734867457: New connection from ::1:60033 on port 1883.
1734867457: New client connected from ::1:60033 as auto-5843C598-1B0D-6FFE-3E86-2C7D325D08BB (p2, c1, k60).
1734867462: New connection from ::1:60035 on port 1883.
1734867462: New client connected from ::1:60035 as auto-46F1C8FC-7E9E-67FC-859D-72DAAA13CAD7 (p2, c1, k60).
1734867462: Client auto-46F1C8FC-7E9E-67FC-859D-72DAAA13CAD7 disconnected.
```

```bash
# Publisher
(base) yeonjae-jeong@jeong-yeonjaeui-MacBookAir ~ % mosquitto_pub -h localhost -p 1883 -t test/topic -m 'Hello, Pokemon!!!'
```

```bash
# Subscriber
(base) yeonjae-jeong@jeong-yeonjaeui-MacBookAir ~ % mosquitto_sub -h localhost -p 1883 -t test/topic
Hello, Pokemon!!!
```

Publisher와 Subscriber의 실행 순서 중요
Subscriber가 먼저 실행된 후, Publisher가 실행되어야 메시지를 받기 가능
QoS 설정 추가