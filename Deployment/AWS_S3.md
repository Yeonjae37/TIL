## AWS S3란?
: Simple Storage Service
일반적인 파일서버는 트래픽이 증가함에 따라 장비를 증설하는 작업을 해야 하는데 S3는 이를 대행함. 트래픽에 따른 시스템 문제는 걱정할 필요가 없고, 파일에 대한 접근 권한을 지정할 수 있어서 서비스를 호스팅 용도로 사용하는 것을 방지할 수 있음

## 특징
- 많은 사용자가 접속을 해도 이를 감당하기 위해서 시스템적인 작업을 하지 않아도 된다.
- 저장할 수 있는 파일 수의 제한이 없다.
- 최소 1바이트에서 최대 5TB의 데이터를 저장하고 서비스 할 수 있다.
- 파일에 인증을 붙여서 무단으로 엑세스 하지 못하도록 할 수 있다.
- HTTP와 BitTorrent 프로토콜을 지원한다.
- REST, SOAP 인터페이스를 제공한다.
- 데이터를 여러 시설에서 중복으로 저장해 데이터의 손실이 발생할 경우 자동으로 복원한다.
- 버전관리 기능을 통해서 사용자에 의한 실수도 복원이 가능하다.
- 정보의 중요도에 따라서 보호 수준을 차등 할 수 있고, 이에 따라 비용을 절감할 수 있다.

## 용어 정리
- 객체 - object, AWS는 S3에 저장된 데이터 하나 하나를 객체라고 명명하는데, 하나 하나의 파일이라고 생각하면 good~
- 버킷 - bucket, 객체가 파일이라면 버킷은 연관된 객체들을 그룹핑한 최상위 디렉토리 같은 느낌?? 버킷 단위로 지역(region)을 지정 할 수 있고, 또 버킷에 포함된 모든 객체에 대해서 일괄적으로 인증과 접속 제한을 걸 수 있음.
- 버전관리 - S3에 저장된 객체들의 변화를 저장. 예를들어 A라는 객체를 사용자가 삭제하거나 변경해도 각각의 변화를 모두 기록하기 때문에 실수 만회 가능
- RSS - Reduced Redundancy Storage의 약자로 일반 S3 객체에 비해서 데이터가 손실될 확률이 높은 형태의 저장 방식. 대신에 가력이 저렴하기 때문에 복원이 가능한 데이터, 이를테면 섬네일 이미지와 같은 것을 저장하는데 적합. 그럼에도 불구하고 물리적인 하드 디스크 대비 400배 가량 안전하다는 것이 아마존의 주장
- Glacier - 짱 저렴한 가격으로 데이터를 저장 할 수 있는 아마존 스토리지 서비스

