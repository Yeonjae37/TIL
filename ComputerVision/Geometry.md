# Euclidean Geometry (유클리드 기하학)

다음과 같은 기본 개념을 포함한다 
- Point (점) : 위치만을 가지며 크기가 없는 기본적인 단위
- Line (선) : 두 점을 잇는 직선으로, 무한히 뻗어 나가는 것
- Plane (면) : 이차원적인 확장으로, 무한히 확장되는 것
- Parallel lines (평행선) : 한 평면 내에서 서로 만나지 않는 두 직선
- Angle (각) : 두 직선이 한 점에서 만날 때 이루는 도형
- Triangle (삼각형) : 세 개의 변과 세 개의 각을 가진 도형
- Pythagorean theorem (피타고라스의 정리) : 직각삼각형에서 직각을 이루는 두 변의 제곱합이 빗변의 제곱과 같음

Euclidean Geometry에서 공간은 Curvature(곡률)이 0인 평평한 공간임.

### 평행선의 공리

| 임의의 직선 L과, 그 직선 위에 있지 않은 점 P가 주어졌을 때, 점 P를 지나고 직선 L과 만나지 않는 직선은 오직 하나 뿐이다.

여기서 Projective Geometry(사영 기하학)은 
평행선이 만나는 점(ideal point)을 도입하여, Euclidean Geometry의 평행 개념을 제거한 보다 일반적인 기하학이다.

# Projective Geometry
- 거리, 각도, 평행 개념이 없음
- 이 기하학에 평행선의 공리를 추가하면 Affine Geometry가 되고,
- 거리, 각도를 추가하면 Euclidean Geometry가 됨.
- 평행선의 공리(평행선이 1개)를 부정하는 경우가 Non-Euclidean Geometry이고,
	- 평행선이 무수히 많은 경우가 Hyperbolic Geometry
	- 평행선이 아예 없는 경우가 Ellipitic Geometry
- 사영 기하학에서는 모든 직선이 교차(ideal point에서) 한다고 가정한다.


두 평행한 직선은 유클리드 공간에서는 만나지 않지만, 사영 공간 $P^2$에서는 만난다. 이 때 만나는 점을 ideal point라고 한다.

### Ideal point (무한원점)
: "한 방향"을 점 하나로 나타낸 수학적 표현이다. 
- $y = 0$과 $y = 1$은 어디까지 뻗어도 만나지 못하는 두 개의 수평선이다. 다만 projective geometry에서는 이 둘이 수평 방향의 무한원점을 공유한다고 표현한다. 
- 동차좌표에서는 보통 3D 위치를 $[X : Y : Z : 1]$
- 방향을 나타내는 무한원점을 $[d_x : d_y : d_x : 0]$으로 쓴다. 마지막 값 0은 일반적인 3D 위치로 바꿀 수 없다는 표시이다.

> Projective Geometry는 평행선의 방향을 무한원점으로 표현하고, 카메라는 그 무한원점을 영상의 소실점으로 투영한다.
