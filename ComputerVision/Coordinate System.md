
1. World Coordinates (월드 좌표계) :
	- $[x_w,  y_w,  z_w, 1]^T$
	- 카메라 외부에 존재하는 객체(object)의 위치를 전역적인 좌표계에서 나타낸 것
	- 편의를 위해 Camera Coordinates와 같은 axis와 origin을 사용하기도 함

2. Camera Coordinates (카메라 좌표계) : 
	- $[x_c, y_c, z_c, 1]^T$
	- 월드 좌표계에서 표현된 점을 카메라 중심을 원점으로 하는 좌표계로 변환한 것
	- 카메라 중심은 보통 optical center를 말함

3. Normalized Image Plane Coordinates (정규화 이미지 평면 좌표계) : 
	- $[x_n, y_n, 1]^T$
	-  카메라 앞 $z = 1$인 가상 영상면에 투영한 위치
	- 카메라 좌표계를 정규화된 이미지 평면으로 변환한 것
	- 일반적으로는 sensor coordinates에 intrinsic matrix K의 inverse를 곱해 얻음

4. Image Plane Coordinates
	- 초점거리 $f$ 만큼 떨어진 영상면 위의 위치

5. Sensor Coordinates (센서 좌표계)
	- 실제 이미지 센서 위에서 빛이 맺히는 위치

6. Pixel Coordinates 
	- $[u, v]$
	- 저장된 이미지에서의 열, 행 위치










