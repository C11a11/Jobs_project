import sqlite3 as sq
import requests as req
with sq.connect('jobs.db') as connect:
    cursor = connect.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS vacancies(id INTEGER PRIMARY KEY AUTOINCREMENT,title TEXT,hours INTEGER,url TEXT)')
    query = {'text':'Junior DevOps','per_page' : 100}
    res = req.get('[https://api.hh.ru/vacancies](https://api.hh.ru/vacancies)',params = query)
    print(res.status_code)
    print(res.json())
