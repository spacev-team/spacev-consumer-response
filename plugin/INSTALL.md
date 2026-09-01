# SpaceV Consumer Response Plugin v1.4.0

## 필수 조건

- ChatGPT 워크스페이스에서 Plugins 사용 가능
- Google Drive 앱 사용 가능
- Google Docs 문서 읽기/복사/편집 권한 가능
- 기준 템플릿 문서에 접근 가능

## 관리자 설정

1. Workspace settings → Permissions & roles → 배포 대상 역할에서 **Use plugins** 활성화
2. 플러그인 소유자가 동료에게 직접 공유할 수 있도록 **Share plugins** 활성화
3. 전사 공개가 필요 없다면 **Publish plugins to workspace**는 끈 상태로 둬도 됨
4. Workspace settings → Apps → Google Drive에서 대상 사용자가 Google Drive를 사용할 수 있게 설정
5. Google Drive의 문서 복사/생성/편집 같은 필요한 쓰기 동작을 허용하고, 필요 시 중요 동작 승인 정책 유지

## 2명에게만 배포

1. 플러그인 소유자가 Plugins → Created by me에서 `삼삼엠투 소비자원 답변서` 선택
2. `•••` → **Share plugin**
3. **Only those invited** 선택
4. 사용할 직원 2명만 추가
5. Save
6. 직원은 Plugins → Shared with me에서 설치
7. 각 직원은 본인 회사 Google Drive 계정을 연결하고 기준 템플릿 문서에 접근 가능한지 확인

## 사용

공문/민원 접수 내용 + 결제 상세 정보 + 계약메모 전체를 첨부한 뒤:

`소보원 답변서 작성해줘.`

플러그인은 DOCX를 만들지 않고, 고정 Google Docs 템플릿을 네이티브 복사한 뒤 복제본만 편집하고 Google Docs 링크를 반환해야 한다.
