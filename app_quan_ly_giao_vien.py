from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, Markup
from datetime import  datetime
from Xu_ly.Giao_vien.Xu_ly_Model import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  exc

Base.metadata.bind=engine
DBSession = sessionmaker(bind=engine)
session_1 = DBSession()

app=Flask(__name__,static_url_path="",static_folder="Media",template_folder='Giao_dien')
app.secret_key="asdfaf"


if __name__=="__main__":
    app.debug=True
    app.run()