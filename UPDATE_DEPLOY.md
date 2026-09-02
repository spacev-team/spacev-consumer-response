# v1.5.3 빠른 업데이트 배포

저장소: `https://github.com/spacev-team/spacev-consumer-response`

## 핵심 변경

- 영구 마스터 템플릿을 과거 사건 문서에서 **`[답변서] 고정 양식`**으로 변경
- 고정 문서 ID: `1slSv_nu58ITcUz07pm-O1EVcSf1n7v7_viQ93cqaxHo`
- 직원은 고정 양식을 매번 첨부하지 않음
- Plugin이 고정 ID를 직접 읽고 native copy 후 사본만 편집
- 원본 `[답변서] 고정 양식` 직접 수정 금지
- 새 빈 Google Doc 생성·양식 흉내·DOCX/PDF/Markdown 우회 금지
- 사본에서 문서번호, 수신인, 제목, 계약기간, 이용상품, 2항, 3항, 발신부 빈 필드만 채움
- 편집 전후 SpaceV 로고·고정 표 너비·29pt 제목·하단 가로선/발신부 구조 검증

## GitHub 업데이트

1. 이 패키지의 **내용물**을 저장소 루트에 업로드해 덮어쓴다.
2. Commit message: `Use permanent blank Google Docs master template v1.5.3`
3. 즉시 반영이 필요하면 Workspace Marketplace에서 `Sync now`를 실행한다.
4. 자동 동기화를 기다리는 경우 다음 동기화 후 Plugin 버전 `1.5.3`을 확인한다.

## 테스트

직원 테스트 입력은 짧게 유지한다.

`@삼삼엠투 소비자원 답변서 공문, 결제 상세 정보, 계약메모 전체를 검토해서 답변서 작성해줘.`

성공 기준:

- 결과가 네이티브 Google Docs 링크
- 새 문서가 `[답변서] 고정 양식`의 사본
- 원본 마스터는 빈 상태 그대로 유지
- SpaceV 로고/제목/표/하단 발신부 서식 유지
- 계약기간·이용상품은 결제 상세 원문 그대로
- 채팅에 완성형 답변서 본문을 대신 출력하지 않음
