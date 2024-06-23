## 원격 저장소에 있는 자료를 로컬에 복제 (git clone)

`git clone [원격 저장소 링크]`
`git clone https://github.com/username/project.git`

위 명령어를 입력하면 원격 저장소에 있는 모든 파일과 폴더가 내 폴더에 복제됨.

만약 git clone을 한 후 "별칭"을 origin이 아닌 다른 이름으로 변경하고 싶다면 
cd 해당 폴더 -> clone이 완료된 해당 폴더로 이동한 후 
`git remote add [새로운 별칭] [원격 저장소 링크]

## 다른 branch에서 clone을 하고 싶을 때

`git clone -b [branch명] [원격 저장소 링크]`

git clone 명령어를 사용하여 Git 저장소를 복제할 때, 기본적으로 master 브랜치가 복제됨. 
하지만, git clone 명령어를 실행할 때 -b 옵션을 사용하여 다른 브랜치를 복제할 수 있음.