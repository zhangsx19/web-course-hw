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
        uploadpath = 'upload\\'+file_info['userid']
        uploadpath = os.path.join(basedir,uploadpath)
        file_path = os.path.join(uploadpath,f_name)
        data = {"code": 500, "msg": "上传失败！"}
        if not os.path.exists(uploadpath):
            os.makedirs(uploadpath)
            #print(os.path.exists(uploadpath))
        try:
            file_buffer.save(file_path)
            data.update({"code": 200, "msg": "上传成功！"})
        except FileNotFoundError as e:
            print(e)
        return jsonify(data)
    #el-upload have option request
    else:
        return jsonify("hello")


        