# SpaceV Internal Plugins

SpaceV 사내 ChatGPT Plugin 배포용 GitHub Marketplace 저장소입니다.

## 현재 포함 Plugin

- `spacev-consumer-response` v1.4.0
  - 한국소비자원·1372 등 국내 소비자기관 민원 답변서 작성
  - Word/DOCX를 최종 산출물로 사용하지 않음
  - SpaceV 로고가 포함된 고정 Google Docs 기준 문서를 네이티브 복사한 뒤 사건별 내용만 편집
  - Google Drive/Docs 접근 필요

## Marketplace 파일 위치

- ChatGPT/Codex가 읽는 marketplace: `.agents/plugins/marketplace.json`
- Claude Code가 읽는 marketplace: `.claude-plugin/marketplace.json`
- 두 파일 모두 같은 plugin 디렉토리(`./plugin`)를 가리킨다.

## ChatGPT 관리자 최초 Import

1. ChatGPT에서 `Workspace settings > Plugins`로 이동
2. `Add > Import marketplace` 선택
3. `Source`에 이 GitHub 저장소 URL 입력
4. 저장소 루트에 marketplace가 있으므로 `Path`는 비움
5. `Branch`는 비우면 기본 브랜치 사용
6. `Import marketplace` 실행 후 GitHub 권한 승인
7. Import 결과에서 `spacev-consumer-response`를 열고 Installation policy를 `Available`로 설정
8. Google Drive 사용 가능 여부 확인

`Available`은 사내 사용자가 필요할 때 직접 설치하는 방식이며 자동 설치가 아닙니다.

## 업데이트

Plugin 수정 시:

1. `plugin/.codex-plugin/plugin.json`의 version 변경
2. `plugin/.claude-plugin/plugin.json`의 version 변경
3. `.claude-plugin/marketplace.json`의 해당 plugin version 변경
4. 변경사항을 기본 브랜치에 push

`.agents/plugins/marketplace.json`은 version 필드가 없어 plugin 추가/삭제 시에만 수정한다.

ChatGPT Marketplace는 기본적으로 매일 동기화합니다. 즉시 반영이 필요하면 관리자가
`Workspace settings > Plugins > Marketplaces > 해당 marketplace > Sync now`를 실행합니다.

## 기존 ZIP Plugin을 GitHub 관리로 전환할 경우

기존에 Workspace에 동일 이름의 Plugin이 이미 있다면, 관리자 화면에서 그 Plugin의 ID를 확인한 뒤 marketplace의 해당 항목에 `pluginId`를 추가하면 기존 Plugin의 ID/공유/정책을 유지한 채 GitHub를 업데이트 소스로 전환할 수 있습니다.
