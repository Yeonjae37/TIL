## Internet
방대한 네트워크, 네트워크 인프라. \
TCP/IP 기반의 네트워크가 세계적으로 확대되어 연결된 네트워크들의 네트워크. \
인터넷에 연결되어 있다면, 컴퓨터는 다른 컴퓨터와 통신이 가능하다. \
이때, 데이터는 다양한 프로토콜에 따라서 주고받을 수 있다. \
(프로토콜은 통신할 때 지켜야 하는 규칙을 의미함)

## Web
Web은 Internet의 일부! \
Web은 인터넷을 통해 데이터를 얻는 방법이다.\
인터넷 계층 위에 설계된 데이터 공유 모델. \
Web은 Http Protocol을 사용함.

## Web Protocol

## IP / MAC / ARP
IP(Internet Protocol)는 각각의 패킷을 IP 주소와 MAC 주소를 통해 상대방에게 전달하는 역할을 한다. \
**IP 주소** : 각 노드에 부여된 주소를 가리킨다. \
**MAC 주소** : 각 네트워크 카드(NIC)에 할당된 고유의 주소를 말한다. \
**ARP** : 유동적인 IP 주소를 고유 주소인 MAC 주소로 변환하여 목적지를 찾아간다.

IP의 정보는 패킷 혹은 데이터그램이라고 하는 덩어리로 나뉘어져 전송되게 되는데\
이 과정에서 데이터가 제대로 전달되었는지, 데이터의 순서가 올바른지 보장하지 않는 특징이 있다. \
따라서 IP의 특징을 **비신뢰성(unreliability)** 과 **비연결성(connectionlessness)** 이라고 말한다. \
현재 인터넷에서 사용하고 있는 표준 프로토콜은 IPv4(xxx.xxx.xxx.xxx)이지만 고갈 문제로 \
IPv6가 대중화 될 것이라고 예상하고 있다.

TCP/IP는 패킷 통신 방식의 인터넷 프로토콜인 IP와 전송 조절 프로토콜인 TCP로 이루어져 있다. \
TCP는 IP 통신을 기반으로 작동하므로 따로 생각하기 보다는 하나의 흐름!!

## TCP / UDP

### TCP
위의 IP 문제를 보완하기 위한 목적을 가진 프로토콜. \
데이터의 전송 여부, 순서를 보장하기 위해 정보 전달을 통제한다고 하여 전송 제어 프로토콜 (Transmisson Control Protocol)을 줄여 TCP라고 함. 

**3 - Way Handshake**
1. 상대에게 통신을 하고 싶다는 메시지를 보낸다. (SYN)
2. 상대는 그 메시지에 대한 응답 + 나도 통신 준비가 되었다는 메시지를 보낸다. (SYN-ACK)
3. 2번에서 받은 메시지에 응답을 보낸다. (ACK)

위의 과정을 통해 나와 상대방의 통신 준비가 모두 마쳐진 상태를 유지하고 통신이 연결되어 있음을 보장하게 된다.

위와 같은 특징으로 아래와 같은 장점이 있다.
- 데이터를 안정적으로 전달
- 데이터를 순서대로 전달
- 데이터를 에러 없이 교환할 수 있도록 전달

클라이언트와 서버가 TCP 커넥션이 맺어지면 메시지가 절대 사라지거나 손상되지 않고, 순서가 뒤바뀔 일도 없는 안정성 있는 프로토콜이다.

### UDP
반면 UDP는 상대방이 데이터를 잘 받았든 말든 상관 안함. \
하지만 TCP보다 속도 good~! \
예를 들어 유튜브는 데이터가 잘 전달 되었는지보다 속도가 더 중요함. 따라서 서비스에 따라 사용하는 프로토콜이 다름.

## DNS
IP 주소는 숫자로 이루어져 있기 때문에 사람들이 기억하기 쉽지 않음. \
IP 주소를 이해하기 쉬운 일반적인 문자로 매핑해주는 시스템이 DNS. \
DNS는 도메인 주소를 IP 주소로 변환해주는 역할을 하기 때문에, 사용자는 도메인 이름을 입력하면 원하는 사이트에 접근할 수 있게 된다.












