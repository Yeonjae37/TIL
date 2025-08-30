```bash
# nvm 설치
curl -o- <https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh> | bash
```

```bash
# 환경변수 설정
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \\. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \\. "$NVM_DIR/bash_completion"
```

```bash
# Node.js 설치
nvm install --lts
nvm install 23
node -v
npm -v
```

```bash
# helia-examples 클론
git clone <https://github.com/ipfs-examples/helia-examples.git>
```

```bash
# Helia 101 예제 실행
cd helia-101
npm install
npm run 101-basics
```

```bash
(base) yeonjae-jeong@jeong-yeonjaeui-MacBookAir helia-101 % npm run 101-basics

> helia-101@1.0.0 101-basics
> node 101-basics.js

Added README.md file: bafybeiglydzhxoceywymdh4lfrfpdmhgjyjnege6mdu4aap7wtd7qyelmq
add event unixfs:importer:progress:file:read { bytesRead: 15n, chunkSize: 15n, path: undefined }
add event blocks:put:providers:notify CID(bafkreife2klsil6kaxqhvmhgldpsvk5yutzm4i5bgjoq6fydefwtihnesa)
add event blocks:put:blockstore:put CID(bafkreife2klsil6kaxqhvmhgldpsvk5yutzm4i5bgjoq6fydefwtihnesa)
add event unixfs:importer:progress:file:write {
  bytesWritten: 15n,
  cid: CID(bafkreife2klsil6kaxqhvmhgldpsvk5yutzm4i5bgjoq6fydefwtihnesa),
  path: undefined
}
add event unixfs:importer:progress:file:layout {
  cid: CID(bafkreife2klsil6kaxqhvmhgldpsvk5yutzm4i5bgjoq6fydefwtihnesa),
  path: undefined
}
Added file: bafkreife2klsil6kaxqhvmhgldpsvk5yutzm4i5bgjoq6fydefwtihnesa
cat event blocks:get:blockstore:get CID(bafkreife2klsil6kaxqhvmhgldpsvk5yutzm4i5bgjoq6fydefwtihnesa)
cat event unixfs:exporter:progress:raw { bytesRead: 15n, totalBytes: 15n, fileSize: 15n }
Added file contents: Hello World 101

# Helia 노드 생성
# 파일 데이터를 블록으로 변환하고 CID 생성
# CID를 사용해 파일 내용 읽기
```