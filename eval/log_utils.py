"""Utility for structured experiment logging.

Appends dict records to a CSV (creating header if missing) with stable column ordering.
"""
from __future__ import annotations
import csv
import os
import time
from datetime import datetime, timezone
from typing import Dict, Iterable, List, Sequence

# Canonical ordered field names (extend cautiously to preserve downstream parsers)
FIELD_ORDER: List[str] = [
    "run_id",
    "timestamp",
    "task",
    "model",
    "prompt_hash",
    "temperature",
    "input_tokens",
    "output_tokens",
    "latency_ms",
    "score_relevance",
    "score_factuality",
    "notes",
    "error_type",
    "error_message",
]

DEFAULT_LOG_PATH = os.path.join(
    os.path.dirname(__file__), "experiment_log.csv")


def _normalize_row(row: Dict) -> Dict:
    """Ensure all expected keys exist (fill missing with empty string)."""
    normalized = {k: row.get(k, "") for k in FIELD_ORDER}
    return normalized


def _generate_run_id(prefix: str = "run") -> str:
    return f"{prefix}-{int(time.time()*1000)}"


def log_run(row: Dict, path: str = DEFAULT_LOG_PATH, auto_id: bool = True) -> str:
    """Append a single experiment record.

    Args:
        row: Dict containing experiment fields (subset allowed).
        path: Destination CSV path.
        auto_id: Generate run_id if missing.
    Returns:
        The run_id used for the record.
    """
    if auto_id and not row.get("run_id"):
        row["run_id"] = _generate_run_id()
    if not row.get("timestamp"):
        row["timestamp"] = datetime.now(timezone.utc).isoformat()

    normalized = _normalize_row(row)
    file_exists = os.path.exists(path)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELD_ORDER)
        if not file_exists:
            writer.writeheader()
        writer.writerow(normalized)
    return normalized["run_id"]


if __name__ == "__main__":  # Simple smoke test
    rid = log_run({
        "task": "smoke_test",
        "model": "openai:gpt-4o-mini",
        "prompt_hash": "demo123",
        "temperature": 0.0,
        "input_tokens": 42,
        "output_tokens": 17,
        "latency_ms": 123.4,
        "score_relevance": 1.0,
        "score_factuality": 1.0,
        "notes": "initial sanity"
    })
    print(f"Logged run {rid} -> {DEFAULT_LOG_PATH}")
