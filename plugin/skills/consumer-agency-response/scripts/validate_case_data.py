#!/usr/bin/env python3
"""Validate SpaceV consumer-agency response case JSON before Google Docs writes."""
from __future__ import annotations
import argparse, json, re
from pathlib import Path

FORBIDDEN_TERMS=("숙소","숙박","플랫폼","게스트","호스트","예약","체크인","체크아웃")
OUT_OF_SCOPE_TERMS=("카드사","토스페이먼츠","chargeback","pre-arbitration","reason code","issuer rebuttal")
PAYMENT_BREAKDOWN_TERMS=("임대료","관리비","청소비")
RISK_DETAIL_TERMS=("불법","무단 전대","전대차동의서","사용수익권")
EVIDENCE_GAP_TERMS=("확인되지 않았","확인되지 않습니다","미확인","제출 완료 여부","자료가 없음","기록이 없음")
CONDITIONAL_FULL_REFUND_PATTERNS=(
    re.compile(r"전액.{0,12}(?:환불|반환).{0,25}(?:가능|생각|검토|조건)"),
    re.compile(r"(?:민원|신고).{0,25}(?:안|취하|철회).{0,25}(?:전액|환불|반환)"),
)
POSITIVE_USAGE_REFUND_PATTERNS=(
    re.compile(r"당사.{0,50}(?:이용대금|임대료|관리비|청소비).{0,50}(?:환불|반환).{0,30}(?:하겠|할 예정|처리하|수용|하고자)"),
    re.compile(r"(?:이용대금|임대료).{0,40}(?:전액|일부).{0,20}(?:환불|반환).{0,20}(?:수용|처리)"),
)
STRONG_LANDLORD_REFUND_PATTERNS=(re.compile(r"임대인은.{0,50}(?:환불|반환).{0,30}(?:의사|동의|합의|하기로)"),)
REQUIRED_KEYS=("recipient","title","contract_period","product_name","section2_paragraphs","section3_paragraphs","content_guard","contract_source")

def clean_recipient(value:str)->str:
    value=value.strip()
    for suffix in ("담당자님","담당자"):
        if value.endswith(suffix): value=value[:-len(suffix)].strip()
    return value

def response_body(data:dict)->str:
    return "\n".join([str(data.get("title","")),*map(str,data.get("section2_paragraphs",[])),*map(str,data.get("section3_paragraphs",[]))])

def validate_contract_source(data:dict)->None:
    source=data.get("contract_source")
    if not isinstance(source,dict): raise ValueError("contract_source is required")
    if str(source.get("type","")).strip() not in {"payment_detail","user_explicit"}: raise ValueError("contract_source.type must be payment_detail or user_explicit")
    if source.get("confirmed") is not True: raise ValueError("contract_source.confirmed must be true")
    raw=str(source.get("raw_excerpt",""))
    if not raw.strip(): raise ValueError("contract_source.raw_excerpt is required")
    period=str(data.get("contract_period","")).strip(); product=str(data.get("product_name","")).strip()
    if period not in raw: raise ValueError("contract_period must be copied verbatim from contract_source.raw_excerpt")
    if product not in raw: raise ValueError("product_name must be copied verbatim from contract_source.raw_excerpt")

def validate(data:dict)->None:
    missing=[k for k in REQUIRED_KEYS if k not in data]
    if missing: raise ValueError("Missing required keys: "+", ".join(missing))
    if not clean_recipient(str(data["recipient"])): raise ValueError("recipient is empty")
    if not 2<=len(data["section2_paragraphs"])<=5: raise ValueError("section2_paragraphs must contain 2 to 5 paragraphs")
    if not 2<=len(data["section3_paragraphs"])<=4: raise ValueError("section3_paragraphs must contain 2 to 4 paragraphs")
    body_values=[str(data["title"]),*map(str,data["section2_paragraphs"]),*map(str,data["section3_paragraphs"])]
    for text in body_values:
        if not text.strip(): raise ValueError("Response paragraphs must not be empty")
        if "\n" in text or "\r" in text: raise ValueError("Each JSON paragraph must be one paragraph")
        found=[t for t in FORBIDDEN_TERMS if t in text]
        if found: raise ValueError("Forbidden terminology found: "+", ".join(found))
    lower="\n".join(body_values).lower()
    found=[t for t in OUT_OF_SCOPE_TERMS if t.lower() in lower]
    if found: raise ValueError("Out-of-scope card/chargeback terminology found: "+", ".join(found))
    extras=data.get("additional_contract_rows",[])
    if not isinstance(extras,list) or len(extras)>3: raise ValueError("additional_contract_rows must be a list of at most 3 approved rows")
    if extras and data.get("additional_contract_rows_approved") is not True: raise ValueError("Additional contract rows require explicit user approval")
    validate_contract_source(data)
    guard=data.get("content_guard")
    required_guard={"deposit_relevant","payment_breakdown_relevant","evidence_gap_material","risk_detail_level","suppress_conditional_landlord_statements"}
    if not isinstance(guard,dict) or not required_guard.issubset(guard): raise ValueError("content_guard is incomplete")
    body="\n".join([*map(str,data["section2_paragraphs"]),*map(str,data["section3_paragraphs"])])
    if guard.get("deposit_relevant") is False and "보증금" in body: raise ValueError("Deposit is not relevant")
    if guard.get("payment_breakdown_relevant") is False:
        used=[t for t in PAYMENT_BREAKDOWN_TERMS if t in body]
        if len(used)>=2 or "구성됩니다" in body: raise ValueError("Payment breakdown is not material")
    if guard.get("evidence_gap_material") is False and any(t in body for t in EVIDENCE_GAP_TERMS): raise ValueError("Non-material evidence-gap narration found")
    if guard.get("risk_detail_level")=="brief" and any(t in body for t in RISK_DETAIL_TERMS): raise ValueError("Risk topic is too detailed")
    if guard.get("suppress_conditional_landlord_statements") is True and any(p.search(body) for p in CONDITIONAL_FULL_REFUND_PATTERNS): raise ValueError("Conditional full-refund statement must be omitted")
    monetary_terms=("환불","반환","보상","수수료","이용대금","보증금","임대료")
    if any(t in body for t in monetary_terms):
        money=data.get("money_guard")
        if not isinstance(money,dict): raise ValueError("money_guard is required for monetary disputes")
        usage=money.get("spacev_usage_fee_refund") or {}
        section3="\n".join(map(str,data["section3_paragraphs"]))
        if not bool(usage.get("authorized",False)) and any(p.search(section3) for p in POSITIVE_USAGE_REFUND_PATTERNS): raise ValueError("Unauthorized SpaceV usage-fee refund language detected")
        landlord=money.get("landlord_refund") or {}
        if str(landlord.get("status","not_confirmed")) not in {"proposed","agreed","scheduled","completed"}:
            factual="\n".join(map(str,data["section2_paragraphs"]))+"\n"+section3
            if any(p.search(factual) for p in STRONG_LANDLORD_REFUND_PATTERNS): raise ValueError("Landlord refund language is stronger than money_guard status")
    seen=set()
    for text in [*map(str,data["section2_paragraphs"]),*map(str,data["section3_paragraphs"])]:
        key=re.sub(r"[\s,.;:·()\[\]{}'\"‘’“”]","",text)
        if key in seen: raise ValueError("Duplicate response paragraph detected")
        seen.add(key)

def main()->None:
    ap=argparse.ArgumentParser(); ap.add_argument("json_file",type=Path); args=ap.parse_args()
    data=json.loads(args.json_file.read_text(encoding="utf-8")); validate(data); print("OK")
if __name__=="__main__": main()
