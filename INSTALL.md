# SpaceV Consumer Response Plugin v1.5.0

## 필수 조건

- ChatGPT 워크스페이스에서 Plugins 사용 가능
- **Google Drive 앱 사용 가능**
- Google Docs 문서 읽기/복사/편집 권한 가능
- 기준 템플릿 문서에 접근 가능

이 버전은 `plugin/.app.json`에서 Google Drive 앱을 플러그인에 바인딩한다.

## 관리자 설정

1. Workspace settings > Plugins에서 `spacev-consumer-response`를 `Available`로 설정
2. Plugin 상세에서 **Required apps: Google Drive**가 표시되는지 확인
3. Workspace settings > Apps > Google Drive에서 대상 사용자가 Google Drive를 사용할 수 있게 설정
4. Google Drive의 문서 복사/생성/편집에 필요한 쓰기 동작을 허용
5. 업데이트 직후에는 `Workspace settings > Plugins > Marketplaces > 해당 marketplace > Sync now` 실행

## 사용

공문/민원 접수 내용 + 결제 상세 정보 + 계약메모 전체를 첨부한 뒤:

`소보원 답변서 작성해줘.`

정상 결과는 **SpaceV 로고가 포함된 네이티브 Google Docs 링크**다.

다음 결과는 실패로 본다.

- Word/DOCX/PDF 파일 생성
- Google Docs 양식을 빈 문서에서 재구성
- `CS 지원금`, `CS 보상` 같은 내부 용어 사용
- 쟁점과 무관한 이용대금 세부 구성 나열
- 불필요한 `회신일 현재 ~ 확인되지 않았습니다` 상태 문장
