"""Illustrative safer patterns; not a complete production application."""
import os, sqlite3
from pathlib import Path
def safe_user_lookup(connection: sqlite3.Connection, username: str):
    # Password hashes should be verified with a maintained password-hashing library.
    return connection.execute("SELECT id, password_hash FROM users WHERE username = ?", (username,)).fetchone()
def safe_read_file(filename: str, allowed_dir: str = "uploads") -> str:
    root=Path(allowed_dir).resolve()
    target=(root/filename).resolve()
    if target != root and root not in target.parents:
        raise ValueError("File path is outside permitted directory")
    if not target.is_file(): raise FileNotFoundError("File not found")
    return target.read_text(encoding="utf-8")
def load_api_key() -> str:
    value=os.environ.get("APP_API_KEY")
    if not value: raise RuntimeError("APP_API_KEY is not configured")
    return value
