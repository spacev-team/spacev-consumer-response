# 배포용 강제 명령어

아래 문장은 플러그인 기본 프롬프트와 동일한 실행 계약이다. 사용자가 짧게 요청해도 이 규칙을 내부적으로 적용한다.

> 공문, 결제 상세 정보, 계약메모 전체를 검토해 소비자원 답변서를 작성해줘. 반드시 고정 Google Docs 템플릿 문서 ID `1m3rgfQz_GqcyuijmqmRHKQq_PZKqER4II7A5PylHIqM`를 직접 열고 네이티브 복사한 뒤 복사본만 편집해. Drive에서 템플릿을 검색하거나 다른 답변서를 고르지 마. 채팅 초안, Markdown 답변서, Word/DOCX/PDF 생성은 금지하고, Google Docs copy/edit가 불가능하면 다른 형식으로 대체하지 말고 중단해. `1. 계약 내용`은 기본적으로 계약기간과 이용상품만 넣고 결제 상세 원문을 그대로 사용해. `CS 지원금`, `CS 보상`은 쓰지 말고 회사의 실제 보상은 `민원인이 이용 과정에서 겪은 불편을 고려하여, 당사는 이용 수수료 ○○원을 현금으로 보상하였습니다.`처럼 풀어 써. 보증금·총 결제금액·세부 이용대금·실제 퇴실일은 민원 쟁점상 꼭 필요하고 사용자가 추가에 동의한 경우가 아니면 넣지 마. `회신일 현재`, 불필요한 `확인되지 않았습니다`, `당사가 보관하고 있지 않습니다`, `임의로 회수`, `전액 반환을 확정할 수 없습니다` 같은 불필요하게 방어적인 문장은 삭제해. 같은 사실은 한 번만 쓰고 한 문단은 1~2문장으로 작성해. 최종 채팅에는 완성된 `docs.google.com/document/` 링크만 제공해.


Mandatory format rule: before drafting, native-copy the exact canonical Google Doc. Do not direct-create or imitate the template. Verify the copied document retains the positioned SpaceV logo, 29pt centered bold title, 447pt recipient table, 91.5pt/362.25pt contract columns, and footer horizontal rule. If native copy is unavailable or any check fails, stop without returning a document.
