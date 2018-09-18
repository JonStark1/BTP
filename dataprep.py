# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 12:14:40 2018

@author: Asuspc
"""

from pandas import DataFrame
import json
import csv
class User:
    def __init__(self, _answers = [], _downvotes = -1, _questions = [], _rep = -1, _upvotes = -1, _views = -1, _Name = -1):
        self.answers = _answers.copy()
        self.downvotes = _downvotes
        self.questions = _questions.copy()
        self.rep = _rep
        self.upvotes = _upvotes
        self.views = _views
        self.name = _Name
    def add_answer(self, answer):
        self.answers.append(answer)
    def add_question(self, question):
        self.questions.append(question)
    def add_rep(self, rep1):
        self.rep = self.rep + rep1
    def set_rep(self, rep1):
        self.rep = rep1
    def add_downvotes(self, d):
        self.downvotes = self.downvotes + d
    def set_downvotes(self, d):
        self.downvotes = d
    def add_upvotes(self, d):
        self.upvotes = self.upvotes + d
    def set_upvotes(self, d):
        self.upvotes = d
    def add_views(self, d):
        self.views = self.views + d
    def set_views(self, d):
        self.views = d
    def set_name(self, Name):
        self.name = Name

class Question:
    def __init__(self,acc = -1,ans = [], b = "$",c = [],c_date = "$",d = [],f_count = -1, r = [],s = -1,t = [], title_ = "$",userid = -1, viewcount = -1):
        self.accepted_answer = acc
        self.answers = ans.copy()
        self.body = b
        self.comments = c.copy()
        self.creation_date = (c_date + '.')[:-1]
        self.dups = d.copy()
        self.fav_count = f_count
        self.related = r.copy()
        self.score = s
        self.tags = t.copy()
        self.title = (title_ + '.')[:-1]
        self.user_id = userid
        self.view_count = viewcount
    def set_accepted_answer(self,a):
        self.accepted_answer = a
    def add_answer(self,ans):
        self.answers.append(ans)
    def set_body(self,b):
        self.body = (b+'.')[:-1]
    def add_comment(self,c):
        self.comments.append(c)
    def set_creation_date(self,c):
        self.creation_date = (c+'.')[:-1]
    def add_dups(self,d):
        self.dups.append(d)
    def set_fav_count(self,f):
        self.fav_count = f
    def add_related(self,r):
        self.related.append(r)
    def set_score(self,s):
        self.score = s
    def add_tag(self,t):
        self.tags.append(t)
    def set_title(self,t):
        self.title = (t+'.')[:-1]
    def set_user(self, u):
        self.user_id = u
    def set_view_count(self,v):
        self.view_count = v

class Answer:
    def __init__(self,b = "$",c = [],p = -1,s = -1,u = -1):
        self.body = (b+'.')[:-1]
        self.comments = c.copy()
        self.parent_id = p
        self.score = s
        self.user_id = u
    def set_body(self,b):
        self.body = (b+'.')[:-1]
    def add_comment(self,s):
        self.comments.append(s)
    def set_parent_id(self,p):
        self.parent_id = p
    def set_score(self,s):
        self.score = s
    def set_user_id(self,u):
        self.user_id = u
    
def data_preparation():
    file_path_users="C:/Users/Asuspc/Documents/BTP/SmartQDataset/cqadupstack/android/android_users.json"
    file_path_questions="C:/Users/Asuspc/Documents/BTP/SmartQDataset/cqadupstack/android/android_questions.json"
    file_path_answers="C:/Users/Asuspc/Documents/BTP/SmartQDataset/cqadupstack/android/android_answers.json"
    file_path_comments = "C:/Users/Asuspc/Documents/BTP/SmartQDataset/cqadupstack/android/android_comments.json"
    with open(file_path_users) as f:
        data_users = json.load(f)
    with open(file_path_questions) as f:
        data_questions = json.load(f)
    with open(file_path_answers) as f:
        data_answers = json.load(f)
    with open(file_path_comments) as f:
        data_comments = json.load(f)
    data_users=json.dumps(data_users)
    data_users=json.loads(data_users)
    data_questions=json.dumps(data_questions)
    data_questions=json.loads(data_questions)
    data_answers=json.dumps(data_answers)
    data_answers=json.loads(data_answers)
    data_comments=json.dumps(data_comments)
    data_comments=json.loads(data_comments)
    df_users=DataFrame(data_users)
    df_questions=DataFrame(data_questions)
    df_answers=DataFrame(data_answers)
    df_comments = DataFrame(data_comments)
    df_users
    df_users.loc['badges','1']
    #removing unwanted columns
    #df_answers=df_answers.drop(['creationdate'],axis=1)
    print(df_questions.head())
    print(df_answers.head())
    df_comments.head()
    df_users.ix[0]
    
data_preparation()
