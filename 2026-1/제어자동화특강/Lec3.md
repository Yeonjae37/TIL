pg.6
옛날에는 open-loop를 많이 사용했음.
**open loop란?** 
"모터를 이렇게 돌리면 로봇 팔이 30 degree까지 가겠지"라고 계산해서 30 degree 명령을 줌. 그런데 open-loop에서는 실제로 30degree에 도착했는지 확인하지 않음. 마찰이 예상보다 크거나 로봇 팔에 무거운 게 달려있으면 실제 위치는 달라질 수 있다.
**그래서 sensor를 사용해서 closed-loop control을 사용함.**
sensor가 실제 상태를 측정해서 다시 controller에게 알려줌. desired = 30 degree 인데 actual = 27 degree 라면 controller에서는 둘의 차이를 계산해서 error를 게산하고 모터를 조금 더 돌리라는 새로운 명령을 내릴 수 있게 된다. 

대표적인 sensor = Encoder
- revolute joint라면 joint angle $\theta$ , prismatic joint라면 displacement d 를 측정할 수 있다.
- force/torque sensor를 사용하면 end-effector가 얼마나 큰 힘을 가하고 있는지 측정할 수 있다.
- 