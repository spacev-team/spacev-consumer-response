# v1.5.0 빠른 업데이트 배포

## GitHub에서 변경 파일 덮어쓰기

저장소: `https://github.com/spacev-team/spacev-consumer-response`

1. 저장소에서 `Add file > Upload files`
2. 이 업데이트 패키지의 **내용물**을 저장소 루트에 드래그
3. 같은 이름 파일은 변경된 파일로 반영
4. Commit message: `Fix Google Docs output and response wording v1.5.0`
5. Commit changes

## ChatGPT에 즉시 반영

관리자에게 아래만 요청:

`Workspace settings > Plugins > Marketplaces > SpaceV marketplace > Sync now`

그 뒤 Plugin 상세에서 v1.5.0과 Required apps의 Google Drive를 확인한다.

## 테스트

업데이트 후 새 대화에서 다음을 확인한다.

- 결과가 Word가 아니라 `docs.google.com/document/...` 링크인지
- SpaceV 로고가 있는지
- `CS 지원금/CS 보상`이 없는지
- 쟁점과 무관한 보증금이 없는지
- 이용대금 총액+임대료/관리비/청소비 세부 나열이 없는지
- `회신일 현재 ... 확인되지 않았습니다` 문단이 없는지
