#!/usr/bin/env python3
"""Local dashboard server with progress persistence."""

from __future__ import annotations

import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse

TRACKER_DIR = Path(__file__).resolve().parent
REPO_ROOT = TRACKER_DIR.parent
STATE_FILE = TRACKER_DIR / "state.json"

DEFAULT_STATE: dict = {
    "currentWeek": 1,
    "hoursByWeek": {},
    "checklist": {},
    "completedWeeks": [],
    "completedCapstones": [],
    "mockInterviewsLogged": 0,
}


def load_json(path: Path) -> dict | list:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def load_state() -> dict:
    if STATE_FILE.exists():
        stored = load_json(STATE_FILE)
        if isinstance(stored, dict):
            merged = DEFAULT_STATE.copy()
            merged.update(stored)
            return merged
    return DEFAULT_STATE.copy()


def save_state(state: dict) -> None:
    with STATE_FILE.open("w", encoding="utf-8") as handle:
        json.dump(state, handle, indent=2)


def max_week() -> int:
    weeks = load_json(TRACKER_DIR / "weeks.json")
    return max(week["week"] for week in weeks["weeks"])


def apply_patch(state: dict, patch: dict) -> dict:
    if "setCurrentWeek" in patch:
        week = int(patch["setCurrentWeek"])
        state["currentWeek"] = max(1, min(week, max_week()))

    if "setHours" in patch:
        week = str(patch["setHours"]["week"])
        state.setdefault("hoursByWeek", {})[week] = float(patch["setHours"]["hours"])

    if "toggleItem" in patch:
        item = patch["toggleItem"]
        week = str(item["week"])
        item_id = item["id"]
        done = bool(item["done"])
        state.setdefault("checklist", {}).setdefault(week, {})[item_id] = done

    if "completeWeek" in patch:
        week = int(patch["completeWeek"])
        completed = state.setdefault("completedWeeks", [])
        if week not in completed:
            completed.append(week)
            completed.sort()
        if week % 4 == 0:
            month = week // 4
            capstones = state.setdefault("completedCapstones", [])
            if month not in capstones:
                capstones.append(month)
                capstones.sort()
        next_week = min(week + 1, max_week())
        state["currentWeek"] = next_week

    if "logMockInterview" in patch:
        state["mockInterviewsLogged"] = int(state.get("mockInterviewsLogged", 0)) + 1

    if "toggleCapstone" in patch:
        month = int(patch["toggleCapstone"]["month"])
        done = bool(patch["toggleCapstone"]["done"])
        capstones = state.setdefault("completedCapstones", [])
        if done and month not in capstones:
            capstones.append(month)
            capstones.sort()
        elif not done and month in capstones:
            capstones.remove(month)

    return state


def build_payload() -> dict:
    progress = load_json(TRACKER_DIR / "progress.json")
    weeks = load_json(TRACKER_DIR / "weeks.json")
    months = load_json(TRACKER_DIR / "months.json")
    questions_path = REPO_ROOT / "interview-prep" / "questions.json"
    interview_questions = load_json(questions_path) if questions_path.exists() else {"questions": []}
    state = load_state()
    return {
        **progress,
        "weeks": weeks["weeks"],
        "months": months["months"],
        "interviewQuestions": interview_questions.get("questions", []),
        "state": state,
    }


class DashboardHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(REPO_ROOT), **kwargs)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path in ("", "/"):
            self.send_response(302)
            self.send_header("Location", "/tracker/")
            self.end_headers()
            return
        if path == "/api/data":
            self._send_json(build_payload())
            return
        super().do_GET()

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if path != "/api/state":
            self.send_error(404)
            return

        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            patch = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON")
            return

        state = apply_patch(load_state(), patch)
        save_state(state)
        self._send_json({"ok": True, "state": state})

    def end_headers(self) -> None:
        if self.path.startswith("/tracker/") or self.path == "/api/data":
            self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def _send_json(self, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, fmt: str, *args) -> None:
        if os.environ.get("TRACKER_QUIET") != "1":
            super().log_message(fmt, *args)


def find_port(base: int = 8765, tries: int = 10) -> int:
    import socket

    for offset in range(tries):
        port = base + offset
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind(("", port))
                return port
            except OSError:
                continue
    raise SystemExit(
        f"No free port in range {base}-{base + tries - 1}. "
        f"Stop old servers: kill $(lsof -tiTCP:{base}-sTCP:LISTEN)"
    )


def main() -> None:
    base_port = int(os.environ.get("PORT", "8765"))
    port = find_port(base_port)
    url = f"http://localhost:{port}/tracker/"

    print("AI Systems / Agentic Ops roadmap dashboard")
    print(f"  {url}")
    print("")
    print("Progress saves to tracker/state.json automatically.")
    print("Press Ctrl+C to stop.")
    print("")

    if port != base_port:
        print(f"Note: port {base_port} was busy, using {port}.")
        print("")

    if os.environ.get("TRACKER_NO_OPEN") != "1":
        import subprocess

        subprocess.Popen(
            ["open", url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )

    server = HTTPServer(("", port), DashboardHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
        server.server_close()


if __name__ == "__main__":
    main()
