-> 컴퓨터 본체를 보면, cpu와 램카드, 그래픽 카드, SSD, HDD가 다같이 장착되어 컴퓨터가 돌아감.

EC2 인스턴스가 연산에 관한 (CPU, 메모리 등) 처리를 한다고 하면, 데이터를 저장하는 역할(SSD, HDD)은 EBS가 함!

즉, **EBS는 클라우드에서 사용하는 가상 하드디스크(HDD)** 라고 볼 수 있음.
EBS는 AWS 클라우드의 Amazone EC2 인스턴스에 사용할 영구 블록 스토리지 볼륨을 제공함.

## EBS <-> EC2 연결 특징
EBS의 가장 큰 특징! EC2 인스턴스가 종료되어도 별개로 작동함. 
-> EBS는 네트워크로 별개로 연결된 서비스이기 때문!!

그래서 인스턴스의 처리 기능이 필요하지 않고 저장 장치 기능만 필요할때는, 인스턴스를 정지시켜도 EBS는 독립적으로 살아있기 때문에 스토리지 기능만 이용하는데 인스턴스의 추가 요금을 내지 않아도 됨

![ebs](../attachment/ebs.png)

![ebs](../attachment/ebs2.png)

![ebs](../attachment/ebs3.png)

: 네트워크로 연결되어 있기 때문에 다른 인스턴스와 재연결 가능, 

## EBS 볼륨(Volume)

EBS로 생성한 디스크 하나하나의 저장 단위
EBS 볼륨을 인스턴스에 연결한다는 말은 EC2에 물리적 하드 드라이브처럼 사용하겠다는 뜻
(윈도우에서 볼 수 있는 C드라이브, D드라이브는 각각 디스크이며 볼륨이라고 보면 됨!)

## EBS 볼륨 유형 타입
![ebs](../attachment/ebs4.png)
1. 범용(General Purpose of GP3) : SSD
2. 프로비저닝 된 IOPS(Provisioned IOPS or io2) : SSD
3. 쓰루풋 최적화(Throughput Optimized HDD or st1)
4. 콜드 HDD(SC1)
5. 마그네틱 (Standard)

하드의 성능은 용량과 MAX IOPS 수치를 보면 됨. IOPS 수치가 높을수록 데이터 통신이 빠름
일반적으로 범용타입 GP3를 선택하나, 요금을 아끼고 싶으면 마그네틱 선택