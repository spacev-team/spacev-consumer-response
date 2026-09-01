# SpaceV Internal Plugins

SpaceV 사내 ChatGPT Plugin 배포용 GitHub Marketplace 저장소입니다.

## 현재 포함 Plugin

- `spacev-consumer-response` v1.5.0
  - 한국소비자원·1372 등 국내 소비자기관 민원 답변서 작성
  - **Google Drive 앱 필수 바인딩**
  - Word/DOCX/PDF를 최종 또는 중간 산출물로 사용하지 않음
  - SpaceV 로고가 포함된 고정 Google Docs 기준 문서를 네이티브 복사한 뒤 사건별 내용만 편집
  - 내부 용어 `CS 지원금/CS 보상` 외부 노출 금지
  - 쟁점과 무관한 보증금, 이용대금 세부 구성, `회신일 현재 ~ 확인되지 않음` 문장 제거

## ChatGPT 관리자 최초 Import

1. ChatGPT에서 `Workspace settings > Plugins`로 이동
2. `Add > Import marketplace` 선택
3. `Source`에 `https://github.com/spacev-team/spacev-consumer-response` 입력
4. 저장소 루트에 marketplace가 있으므로 `Path`는 비움
5. `Branch`는 비우면 기본 브랜치 사용
6. `Import marketplace` 실행 후 GitHub 권한 승인
7. Import 결과에서 `spacev-consumer-response`를 열고 Installation policy를 `Available`로 설정
8. Plugin 상세의 **required apps에서 Google Drive가 잡혀 있는지 확인**
9. Workspace settings > Apps > Google Drive에서 사용 대상과 문서 쓰기 동작을 허용

`Available`은 사내 사용자가 필요할 때 직접 설치하는 방식이며 자동 설치가 아닙니다.

## 업데이트

Plugin 수정 시 기본 브랜치에 변경사항을 commit/push한 뒤 관리자에게 `Sync now`를 요청합니다.

이번 버전에서 바뀌는 파일은 주로 다음입니다.

- `plugin/.codex-plugin/plugin.json`
- `plugin/.app.json`
- `plugin/skills/consumer-agency-response/**`
- `.claude-plugin/marketplace.json`

ChatGPT Marketplace는 기본적으로 매일 동기화합니다. 즉시 반영이 필요하면 관리자가
`Workspace settings > Plugins > Marketplaces > 해당 marketplace > Sync now`를 실행합니다.
