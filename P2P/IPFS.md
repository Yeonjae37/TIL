InterPlanetaryFileSystem
-> 웹을 완벽하게 분산시키는 것을 목표로 함

P2P!!!

기존은  위치기반 주소지정 방식
-> 어디서 찾을 것인가?!
IPFS는 컨텐츠기반 주소지정 방식
-> 무엇을 찾을 것인가?!

<그래서 어떻게 저장이 되고, 어떻게 불러오는가?!>
파일들은 IPFS 개체에 저장됨
-> 한 개체당 256kb까지 저장 가능
그럼 사진이나 영상 같은 큰건? -> 여러 개의 IPFS 개체에 나눠져서 저장

IPFS는 컨텐츠 기반 주소지정을 사용하므로 한번 네트워크에 추가되면 변경 불가능 (블럭체인과 같은 불변성)

변경을 하고 싶다면?
Versioning 지원 중
'커밋 개체' 생성 -> 어떤 커밋이 이루어졌는지와 해당 파일이 담긴 IPFS 개체로의 링크를 담음
업데이트 하고 싶다면 그냥 업데이트 된 파일을 IPFS 네트워크에 추가시키기만 하면 된다.
그러면 소프트웨어는 새로운 커밋 개체를 생성하고,
이 새로운 커밋 개체는 이전에 제출된 커밋 개체와 링크를 형성함

단점 : IPFS 네트워크상에서 어떻게 해당 파일을 계속 유지해줄 것인가?!
캐시를 유지해줘야하는데 그걸 호스트하는 노드들이 오프라인이 된다면?
파일 다운로드 불가능해짐,,, (시더 없는 토렌트와 같아짐)

방안은?
Incentivize nodes -> 유저들이 파일 저장 및 유지에 대한 인센티브를 지불하거나
Proactively distribute files -> 적극적으로 파일들을 배포함으로써 네트워크 상에 특정 수 이상의 사본들이 존재하도록 하기
-> 파일 코인이 이것을 목표로 함!!!

파일코인: IPFS를 만든 그룹이 만든 코인
저장공간의 분산화 시장을 만드는 것을 목적으로 만들어진 IPFS 기반 블럭체인
하드 드라이브에 여분의 저장공간이 있다면 -> 그 공간을 다른 이들에게 임대함으로써 수익을 올리는 절차
노드들에게 인센티브로 지불하기 위해 만들어진 코인.
노드들은 가능한한 파일들을 온라인 상태로 유지하여야 보상을 받을 수 있음.

파일코인 시스템은 파일들을 다수의 노드들에 복제시켜서 다운로드 불가 상태가 되지 않도록 만듬


<IPFS는 어떻게 활용 가능한가?!!>
2017년 터키정부가 위키피디아 접속을 차단한 적이 있었음
-> 이때 IPFS 측 사람들이 이에 대응하여 위키피디아 터키 버전의 사본을 IPFS에 넣어버림
IPFS는 분산배포되어 있으므로 정부가 block할 수 있는 중앙 서버가 존재하지 않았기 때문

Dtube -> Youtube와 같은 느낌인데 IPFS를 이용해 완전하게 분산화 되어있음







