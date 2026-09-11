"""Dated run log: every read/write and anything that couldn't be fetched
gets recorded here so nothing goes stale silently."""
import datetime
import pathlib

LOG_DIR = pathlib.Path(__file__).parent / "logs"


class RunLog:
    def __init__(self, job_name: str):
        LOG_DIR.mkdir(exist_ok=True)
        today = datetime.date.today().isoformat()
        self.path = LOG_DIR / f"{today}-{job_name}.log"
        self._lines: list[str] = []

    def _write(self, level: str, msg: str):
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        line = f"[{ts}] {level}: {msg}"
        self._lines.append(line)
        with open(self.path, "a") as f:
            f.write(line + "\n")

    def info(self, msg: str):
        self._write("INFO", msg)

    def wrote(self, destination: str, summary: str):
        self._write("WROTE", f"{destination} — {summary}")

    def missing(self, what: str, reason: str):
        self._write("MISSING", f"{what} — {reason}")

    def error(self, msg: str):
        self._write("ERROR", msg)
