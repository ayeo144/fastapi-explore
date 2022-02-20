"""
Initialises the main App class and then creates the database.
"""

from app.app import App

app = App()
app.create_db()
