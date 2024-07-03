### JWT 토큰이란?
JWT(Json Web Token)은 Json 객체에 인증에 필요한 정보들을 담은 후 비밀키로 서명한 토큰으로, 인터넷 표준 인증 방식임. 
공식적으로 **인증(Authentication) & 권한허가(Authorization)** 방식으로 사용됨.

### JWT 프로세스
![[스크린샷 2024-06-23 오후 6.03.03.png]]

**JWT를 발급받기까지의 과정 (로그인 전)**
1. 사용자가 아이디와 비밀번호 혹은 소셜 로그인을 이용해 서버에 로그인 요청을 보냄.
2. 서버는 secret key를 사용해  json 객체를 암호화한 JWT 토큰을 발급함.
3. JWT를 헤더에 담아 클라이언트에 보냄.

**로그인 이후**
1. 클라이언트는 JWT를 로컬에 저장해놓음.
2. API 호출을 할 때마다 header에 JWT를 실어 보냄.
3. 서버는 헤더를 매번 확인하여 사용자가 신뢰할만한지 체크하고, 인증이 되면 API에 대한 응답을 보냄.

로그인 후에 왜 매번 JWT를 헤더에 넣어서 보내는가? 매번 인증 과정을 거쳐야하는 이유는 아래 HTTP의 특성 때문.
### HTTP의 특성
> Connectionless:  한 번 통신이 이뤄지고 난 후에 연결이 바로 끊어진다
> Stateless: 이전 상태를 유지/기억하지 않는다

위 특성으로 인해 화면을 이동하여 새로운 API를 요청하면 다시 신뢰할만한 사용자인지 인증하는 과정을 거쳐야한다.

매번 인증하는 과정이 귀찮!

따라서 인증된 사용자가 어느 정도 기간동안 재인증하지 않아도 되도록(로그인이 유지되도록) 만든 것이 Access Token

## JWT의 구조

![[스크린샷 2024-06-23 오후 6.21.23.png]]

**Header**
- alg: Signature에서 사용하는 알고리즘
	- RS256(공개키/개인키)
	- HS256(비밀키(대칭키))
- typ: 토큰 타입

**Payload**
사용자 정보의 한 조각인 클레임(claim)이 들어있음. (key-value)
- sub: 토큰 제목(subject)
- aud: 토큰 대상자(audience)
- iat: 토큰이 발급된 시각(issued at)
- exp: 토큰의 만료 시각(expired)

**Signature**
헤더와 페이로드의 문자열을 합친 후에, 헤더에서 선언한 알고리즘과 key를 이용해 암호한 값.

Header와 Payload는 단순히 Base64url로 인코딩되어있어 누구나 쉽게 복호화할 수 있으나, Signature는 key가 없으면 복호화 불가 (보안상 안전!)  --> header와 payload는 누구나 쉽게 확인할 수 있으니까 중요한 정보를 담으면 안되는구나~~


**위 과정은 전부 Only Access Token만 사용했을 때의 과정**
## With "Refresh Token"
Access Token만을 사용했을 때 보안 문제를 해결하기 위해 나온 Refresh Token

위와 같은 방식으로 진행했을 때의 문제점은 Access Token을 탈취 당했을 때.
유효기간이 긴 토큰 -> 그 시간동안 정보 탈취
유효기간이 짧은 토큰 -> 사용자가 로그인 여러 번 해야 하는 번거로움
이 문제를 해결하기 위해 나온 것이 Refresh Token

Refresh Token을 한 달, Access Token을 하루로 잡았다면 Access Token의 기간이 다 되어도 Refresh Token의 기간이 남아있기 때문에 사용자는 로그인 없이 다시 Access Token을 발급 받을 수 있음.
(RefreshToken 또한 기간이 만료되면 재로그인 필요)

Refresh Token은 Access Token을 다시 발급받기 위한 JWT
