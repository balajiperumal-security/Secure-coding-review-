"""INTENTIONALLY VULNERABLE TRAINING EXAMPLES. Never deploy these."""
import sqlite3
def vulnerable_login(connection, username, password):
    # SQL injection: untrusted input is concatenated into SQL.
    query="SELECT id FROM users WHERE username = '"+username+"' AND password = '"+password+"'"
    return connection.execute(query).fetchone()
def vulnerable_command(filename):
    # Command injection risk: untrusted text is passed to a shell.
    import os
    return os.system("cat "+filename)
def vulnerable_secret():
    # Hard-coded secret example; this value is fake.
    api_key="DEMO-NOT-A-REAL-KEY"
    return api_key
