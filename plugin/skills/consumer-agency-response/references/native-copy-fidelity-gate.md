# Native Copy Fidelity Gate

This gate is launch-blocking. It exists to prevent a newly created Google Doc from merely imitating the canonical SpaceV template.

## 1. Preflight before drafting

Before source analysis or response drafting, attempt to resolve and call a native Google Drive file-copy action for the canonical template document. A connected Google Drive app by itself is not proof that native copy is available.

Required runtime capabilities:

- Read the exact canonical Google Doc by document ID.
- Copy that Drive file natively so the new file inherits the original native document structure.
- Read the copied Google Doc structure.
- Edit the copied Google Doc.

If a callable native file-copy action is unavailable, do not create anything. Do not use a blank Google Doc, Google Docs direct-create, a Documents/DOCX workflow, import conversion, Markdown, or chat text as a fallback. Stop with the fixed failure sentence from SKILL.md.

## 2. Prove the destination is a real native clone

Immediately after native copy and before any content mutation, read the copied document and verify every item below.

- Destination document ID is different from the canonical template ID.
- Exactly one document tab is present.
- `positionedObjects` is non-empty.
- The SpaceV logo is a positioned image using `BEHIND_TEXT`, approximately 64.33pt wide and 19.87pt high.
- The first document paragraph references the positioned logo object.
- The answer-letter title is centered, bold, and 29pt.
- The recipient area is a 1x1 table with a fixed column width of approximately 447pt.
- The contract table is 2x2 and uses fixed column widths of approximately 91.5pt and 362.25pt.
- A horizontal rule remains immediately before the sender/footer block.
- The footer keeps 10pt field text, bold field labels, gray separators, and the email hyperlink.

If any invariant is missing, treat the file as a reconstructed imitation, not a clone. Stop. Do not repair, redraw, restyle, insert a logo, or return that file.

## 3. Mutation policy

Only edit text inside the copied containers. Do not recreate tables, images, page layout, paragraph styles, widths, borders, or footer structure. Prefer exact text replacement or range replacement inside the existing copied paragraphs/cells.

Do not touch the logo object or rebuild the top area. Do not convert the copied file through DOCX or PDF.

## 4. Final fidelity verification

After all current-case text has been written, read the native Google Doc again and re-run the clone checks. Also confirm that no canonical-template case facts remain.

Return the Google Docs URL only if both the pre-edit and post-edit fidelity checks pass.

## Known bad reconstruction signature

The following pattern is an automatic failure and must never be accepted:

- `positionedObjects` is null or empty.
- The answer-letter title is ordinary `NORMAL_TEXT` rather than the retained 29pt centered bold title.
- The contract table columns are evenly distributed 50:50 rather than the original fixed widths.
- The footer is plain body text without the original horizontal rule and field styling.

A document can look similar in chat or PDF while still failing the native-template requirement. Visible similarity is not sufficient.
