## Ideal Point

https://jungsoo-ai-study.tistory.com/55

## Vanishing Point

![session](ComputerVision/vanishingpoint.png)

: 카메라로 기찻길을 찍으면 두 철길의 영상 속 간격이 멀어질수록 좁아진다. 영상에서 두 줄을 연장했을 때 만나는 점이 vanishing point이다. 

하지만 위 사진을 보면 선로가 4개인 것을 확인할 수 있는데, 이 4개의 선로는 모두 한 점에서 만난다. 여기서 vanishing point의 중요한 성질 하나를 알 수 있다.

> 물리 공간에서 평행한 모든 직선들은 영상에서 모두 동일한 vanishing point를 갖는다.

물리공간에서 아무리 멀리 떨어진 직선일지라도 아무리 수가 많더라도, 서로 방향만 같다면 영상에서는 모두 동일한 하나의 소실점으로 수렴하게 된다.

-> Vanishing point는 물리공간에서 평향한 직선들이 영상에 투영되어 원근 효과(perspective effect)에 의해 마치 한 점에서 만나는 것처럼 보이는 현상이다.

https://dsaint31.tistory.com/742

같은 3D 방향으로 뻗는 평행선들은 서로 떨어져 있어도 한 카메라 영상에서 같은 소실점을 가진다.  여기서 같은 방향이라는 것은 실제 3D 공간에서 서로 평행하다는 뜻이다.
