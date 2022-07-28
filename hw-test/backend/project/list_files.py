from flask import jsonify, request
import os
import json
from project import myfunc

        

def list_files():
    #接收前端传来的信息
    data = json.loads(request.get_data(as_text=True))
    userid = data['userid']
    projectid = data['projectid']
    #根据前端信息检索目录
    basedir = os.path.abspath(os.path.dirname(__file__))
    uploadpath = 'upload\\'+userid+'\\'+projectid
    projectpath = os.path.join(basedir,uploadpath)
    
    return myfunc.list2tree(projectpath).toJSON()
    # return jsonify("hello")