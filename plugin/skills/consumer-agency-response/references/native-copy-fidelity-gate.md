# Native Copy Fidelity Gate

This gate is launch-blocking. The canonical source is the blank native Google Doc `[답변서] 고정 양식`, document ID `1slSv_nu58ITcUz07pm-O1EVcSf1n7v7_viQ93cqaxHo`.

## 1. Preflight before drafting

Before drafting answer-letter prose, resolve and call a native Google Drive file-copy action for the canonical template document. A connected Google Drive app by itself is not proof that native copy is available.

Required runtime capabilities:

- Read the exact canonical Google Doc by document ID.
- Copy that Drive file natively.
- Read the copied Google Doc structure.
- Edit the copied Google Doc.

If native file copy is unavailable, stop. Do not create a blank Google Doc, use Google Docs direct-create, import DOCX, emit Markdown, or write a full answer letter in chat as a substitute.

## 2. Prove the destination is a real native clone

Immediately after native copy and before case-content mutation, verify all of the following.

- Destination document ID differs from `1slSv_nu58ITcUz07pm-O1EVcSf1n7v7_viQ93cqaxHo`.
- Exactly one document tab is present.
- `positionedObjects` is non-empty.
- SpaceV logo is a positioned image using `BEHIND_TEXT`, approximately 64.33pt wide and 19.87pt high.
- First document paragraph references the positioned logo object.
- `답 변 서` is centered, bold, and 29pt.
- Recipient area is a 1x1 table with a fixed width of approximately 447pt.
- Contract table is 2x2 with fixed widths of approximately 91.5pt and 362.25pt.
- Contract value cells are initially blank before current-case values are inserted.
- A horizontal rule exists immediately before the sender block.
- Sender block keeps 10pt field text, bold field labels, gray separators, and the email hyperlink.

If any invariant is missing, treat the file as a reconstructed imitation, not a clone. Do not repair or redraw the template; stop instead.

## 3. Mutation policy

Only change current-case text inside the copied document.

- Fill the existing blank document-number, recipient, contract-period, product-name, sender-date, and handler fields.
- Insert section 2 body immediately after `2. 민원 내용 및 확인 결과`.
- Insert section 3 body immediately after `3. 민원 관련 당사 입장 및 조치`.
- Apply normal body styling to inserted prose; do not overwrite heading styles.
- Do not recreate tables, images, page layout, paragraph widths, borders, or the footer structure.
- Never write to the canonical master document.

## 4. Final fidelity verification

After writing, read the native Google Doc again and verify:

- all clone invariants still pass;
- contract fields match locked source strings exactly;
- section 2 and 3 contain current-case prose;
- the master template ID was never edited;
- no blank-template placeholders that should be filled remain;
- no forbidden wording or irrelevant facts survived the content QA.

Return the Google Docs URL only after the post-edit check passes.

## Known bad reconstruction signature

Automatic failure:

- `positionedObjects` is null or empty;
- title is ordinary `NORMAL_TEXT` instead of retained 29pt centered bold title;
- contract columns are evenly distributed instead of fixed 91.5pt / 362.25pt;
- footer is plain body text without the original horizontal rule and field styling;
- document was created from scratch rather than copied from the fixed master.
