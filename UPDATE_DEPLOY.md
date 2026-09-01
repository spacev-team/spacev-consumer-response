# v1.5.2 빠른 업데이트 배포

## GitHub에서 변경 파일 덮어쓰기

저장소: `https://github.com/spacev-team/spacev-consumer-response`

1. 저장소에서 `Add file > Upload files`
2. 이 업데이트 패키지의 **내용물**을 저장소 루트에 드래그
3. 같은 이름 파일은 변경된 파일로 반영
4. Commit message: `Fix Google Docs output and response wording v1.5.2`
5. Commit changes

## ChatGPT에 즉시 반영

관리자에게 아래만 요청:

`Workspace settings > Plugins > Marketplaces > SpaceV marketplace > Sync now`

그 뒤 Plugin 상세에서 v1.5.2과 Required apps의 Google Drive를 확인한다.

## 테스트

업데이트 후 새 대화에서 다음을 확인한다.

- 결과가 Word가 아니라 `docs.google.com/document/...` 링크인지
- SpaceV 로고가 있는지
- `CS 지원금/CS 보상`이 없는지
- 쟁점과 무관한 보증금이 없는지
- 이용대금 총액+임대료/관리비/청소비 세부 나열이 없는지
- `회신일 현재 ... 확인되지 않았습니다` 문단이 없는지


### v1.5.2 즉시 배포
1. 이 저장소 루트에 v1.5.2 파일을 덮어쓴다.
2. 커밋 메시지: `Hotfix Google Docs execution contract v1.5.2`
3. ChatGPT Workspace Marketplace에서 Sync now를 실행한다.
4. 새 채팅에서 Plugin을 다시 호출해 테스트한다.
5. 결과가 Google Docs 링크가 아니면 배포 성공으로 보지 않는다.


## v1.5.2 format-fidelity hotfix

This release adds a launch-blocking native-copy gate. A document that merely looks similar is rejected. The plugin must successfully native-copy the exact canonical Google Doc and prove that the positioned SpaceV logo, title styling, fixed table widths, and footer rule survived before it writes case content or returns a link. If native copy is unavailable in the runtime, the plugin stops instead of creating a replacement document.

Recommended commit message: `Reject reconstructed Docs; require native template clone v1.5.2`
