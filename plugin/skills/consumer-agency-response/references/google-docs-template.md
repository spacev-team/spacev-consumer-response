# Google Docs 고정 템플릿

## 유일한 기준 문서

- 문서 ID: `1slSv_nu58ITcUz07pm-O1EVcSf1n7v7_viQ93cqaxHo`
- 기준 URL: `https://docs.google.com/document/d/1slSv_nu58ITcUz07pm-O1EVcSf1n7v7_viQ93cqaxHo`
- 사본 만들기 URL: `https://docs.google.com/document/d/1slSv_nu58ITcUz07pm-O1EVcSf1n7v7_viQ93cqaxHo/copy`
- 기준 문서 제목: `[답변서] 고정 양식`

이 문서는 소비자기관 답변서의 **영구 마스터 템플릿**이다. 과거 사건 답변서를 템플릿으로 사용하지 않는다. 파일명이나 키워드로 Drive를 검색하지 말고 위 document ID로 직접 접근한다.

원본은 비어 있는 고정 양식이므로 사건 사실을 재사용할 위험을 줄일 수 있다. **원본 자체에는 절대 사건 내용을 쓰지 않는다.** 반드시 네이티브 Google Drive `copy` 기능으로 사본을 만든 뒤 사본만 편집한다.

## 마스터 구조 지문

복제 전후에 아래 구조를 확인한다.

- 단일 탭 문서
- A4 페이지, Arial 11pt 기본 스타일
- 우측 상단 SpaceV 로고가 `positionedObject`로 존재
  - 크기 약 `64.33pt × 19.87pt`
  - `BEHIND_TEXT`
  - 첫 문단이 로고 positioned object를 참조
- `답 변 서` 제목
  - 가운데 정렬
  - Bold
  - 29pt
- 수신인 영역
  - 1행 × 1열 표
  - 열 너비 약 `447pt`
  - 기본 텍스트 `수신인 ㅣ 담당자님`
- 제목 기본 문구: `제목 : 임대목적물 이용 관련 민원 접수 건에 대한 회신`
- `1. 계약 내용`
  - 2행 × 2열 표
  - 열 너비 약 `91.5pt / 362.25pt`
  - 1행: `계약기간` / 빈 값
  - 2행: `이용상품` / 빈 값
- 본문 고정 순서
  1. `1. 계약 내용`
  2. `2. 민원 내용 및 확인 결과`
  3. `3. 민원 관련 당사 입장 및 조치`
- 하단 가로선 존재
- 하단 발신부
  - `발신일자 / 발신인 / 담당자 / 연락처 / 이메일`
  - 10pt 필드 텍스트
  - 필드명 Bold
  - 구분자 회색
  - 이메일 링크 유지

## 빈 양식 채우기 규칙

사본을 만든 뒤 **기존 구조를 재작성하지 않고 빈 필드와 본문만 채운다.**

1. 문서번호: `문서번호 ㅣ` 뒤의 빈 영역만 현재 문서번호로 채운다.
2. 수신인: `담당자님` 앞에 기관명 또는 확인된 담당자명을 넣는다. 담당자명이 없으면 `한국소비자원 담당자님`처럼 기관명 + 담당자님으로 작성한다.
3. 제목: 사건 쟁점을 반영해 제목 문구만 교체하되 기존 제목 스타일을 유지한다.
4. 계약기간: 계약 표의 우측 첫 번째 빈 셀에 `contract_period`를 그대로 삽입한다.
5. 이용상품: 계약 표의 우측 두 번째 빈 셀에 `product_name`을 그대로 삽입한다.
6. 2항 본문: `2. 민원 내용 및 확인 결과` 바로 아래에 현재 사건의 2항 문단만 삽입한다.
7. 3항 본문: `3. 민원 관련 당사 입장 및 조치` 바로 아래에 현재 사건의 3항 문단만 삽입한다.
8. 발신일자/담당자: 하단의 빈 값만 채우고 연락처·이메일·발신인·가로선 구조는 유지한다.

본문 삽입 시 새로 추가된 일반 문장은 템플릿의 기본 본문 스타일(Arial 11pt, 검정, Bold 아님)을 사용한다. 섹션 제목의 Bold/크기/간격은 변경하지 않는다.

## 원본 보호 하드스톱

- 대상 document ID가 마스터 ID `1slSv_nu58ITcUz07pm-O1EVcSf1n7v7_viQ93cqaxHo`와 같으면 **편집 금지**다.
- copy 결과의 새 document ID가 마스터 ID와 동일하면 실패다.
- 마스터 문서에 사건 텍스트를 직접 쓰지 않는다.
- 사본 생성 전에는 답변서 본문을 사용자 채팅에 출력하지 않는다.

## 산출물 하드스톱

- 최종 링크의 도메인은 `docs.google.com/document/`이어야 한다.
- `.docx`, `.doc`, `.pdf`, Markdown, 채팅 답변서로 대체하지 않는다.
- 빈 Google Doc을 새로 만들고 양식을 흉내 내지 않는다.
- 네이티브 copy 기능이 현재 런타임에서 없다면 중단한다.

## 최종 완성 체크

사본 편집 후 다음을 모두 만족해야 한다.

- 문서번호가 필요한 경우 채워져 있음
- 수신인이 `담당자님`만 남아 있지 않음
- 계약기간/이용상품 두 값이 모두 채워져 있음
- 2항과 3항 각각에 현재 사건 본문이 존재함
- 발신일자/담당자 등 필요한 발신 필드가 채워져 있음
- SpaceV 로고, 제목 스타일, 수신인 표, 계약 표 고정폭, 하단 가로선과 발신부 스타일이 그대로 유지됨
- 과거 사건 답변서의 이름·날짜·금액·문구를 템플릿 사실로 가져오지 않음

## Native-copy fidelity requirement

Before this workflow starts, apply `native-copy-fidelity-gate.md`. Native file copy must succeed and the copied document must pass the structural clone signature before any response prose is written to the document.
