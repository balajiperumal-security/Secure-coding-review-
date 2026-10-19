# Secure Coding Review Report

## Scope
Static educational review of three deliberately unsafe patterns and illustrative safer alternatives. This is not a full audit of a real application.

## Finding 1 — SQL injection (High)
**Unsafe pattern:** user input concatenated into SQL.
**Impact:** crafted input can alter query logic and potentially expose or change data.
**Fix:** parameterized SQL queries. Store password hashes, not plaintext passwords, and verify them with a maintained password-hashing library.

## Finding 2 — Command injection (High)
**Unsafe pattern:** untrusted input placed in a shell command.
**Impact:** special characters may cause unintended commands to run.
**Fix:** avoid shell invocation; use fixed argument lists with `shell=False` when subprocesses are needed. Restrict file access to an allowed directory and apply least privilege.

## Finding 3 — Hard-coded secret (High)
**Unsafe pattern:** a secret is embedded in source.
**Impact:** repository readers or leaked history may expose the secret.
**Fix:** use environment variables or a secrets manager; rotate exposed credentials and never commit secrets.

## Before/after
| Issue | Unsafe | Safer |
|---|---|---|
| SQL injection | String concatenation | Parameterized query |
| Command injection | User input in shell command | Avoid shell; fixed argument list |
| Path traversal | Trust arbitrary paths | Resolve and constrain path |
| Secret leakage | Key in source | Environment variable/secret manager |

## Validation
Python syntax checks were run on both examples. These snippets are teaching patterns, not production-ready authentication or storage code.
