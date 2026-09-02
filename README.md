# SpaceV Internal Plugins

SpaceV 사내 ChatGPT Plugin 배포용 GitHub Marketplace 저장소입니다.

## 현재 포함 Plugin

- `spacev-consumer-response` v1.5.3
  - 한국소비자원·1372 등 국내 소비자기관 민원 답변서 작성
  - Google Drive 앱 필수
  - 영구 마스터 Google Doc: `[답변서] 고정 양식`
  - 마스터 ID: `1slSv_nu58ITcUz07pm-O1EVcSf1n7v7_viQ93cqaxHo`
  - 마스터를 네이티브 복사한 뒤 사본의 빈 필드/본문만 사건별로 편집
  - 원본 수정, 템플릿 검색, 빈 문서 재구성, Word/DOCX/PDF/Markdown 우회 금지
  - `1. 계약 내용`은 기본적으로 계약기간·이용상품만 사용
  - 내부 `CS 지원금/CS 보상`, 불필요한 보증금·금액 세부·미확인 상태·방어 문장 제거

## 업데이트

저장소 기본 브랜치에 변경사항을 commit/push합니다. Marketplace가 자동 동기화되면 다음 주기에 반영되고, 즉시 반영하려면 관리자가 `Sync now`를 실행합니다.

권장 커밋 메시지:

`Use permanent blank Google Docs master template v1.5.3`

자세한 배포/테스트 절차는 `UPDATE_DEPLOY.md`를 참고합니다.
