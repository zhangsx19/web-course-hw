from flask import request,jsonify
import os
from sqlalchemy import false
from werkzeug.utils import secure_filename

def upload_file():
    # 返回文件上传结果信息
    if request.method == 'POST':
        file_buffer = request.files['file']
        file_info = dict(request.form)
        f_name = secure_filename(file_buffer.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        uploadpath = 'upload\\'+file_info['userid']+'\\'+file_info['projectid']
        projectpath = os.path.join(basedir,uploadpath)
        if not os.path.exists(projectpath):
            os.makedirs(projectpath)
        file_path = os.path.join(projectpath,f_name)
        data = {"code": 500, "msg": "上传失败！"}
        try:
            file_buffer.save(file_path)
            data.update({"code": 200, "msg": "上传成功！"})
        except FileNotFoundError as e:
            print(e)
        return jsonify(data)
    #el-upload have option request
    else:
        return jsonify("hello")


        