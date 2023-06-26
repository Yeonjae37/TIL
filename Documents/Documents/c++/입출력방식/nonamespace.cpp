#include <iostream>

namespace {
    // 이 함수는 이 파일 안에서만 사용할 수 있습니다.
    // 이는 마치 static int OnlyInThisFile() 과 동일합니다.
    int OnlyInThisFile() {}

    int only_in_this_file = 0;
}

int main() {
    OnlyInThisFile();
    only_in_this_file = 3;
}