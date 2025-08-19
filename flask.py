
from flask import Flask, request, make_response, render_template_string
import sqlite3
app = Flask(__name__)

@app.get("/search")
def search():
    q = request.args.get("q","")
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute(f"SELECT name, desc FROM products WHERE name LIKE '%{q}%'")
    rows = cur.fetchall()
    html = "<ul>" + "".join([f"<li>{n}: {d}</li>" for n,d in rows]) + "</ul>"
    resp = make_response(render_template_string("Results for {{q}} " + html, q=q))
    resp.set_cookie("session", request.cookies.get("session"), samesite=None, secure=False, httponly=False)
    return resp
