import hashlib
import os,socket

def getMd5(data):
    """
    功能：获取MD5值
    参数：data，待处理数据
    返回值：dataMD5，data的MD5值（32位）
    """
    m = hashlib.md5()
    data = data.encode()
    m.update(data)
    dataMd5 = m.hexdigest()
    return dataMd5

def getFileMd5(filePath):
    """
    功能：获取单个接收文件的MD5值
    参数：filePath,文件绝对路径
    返回值：fileMD5，文件的MD5值（32位）
    """
    with open(filePath,"rb") as f:
        data = f.read()
    m = hashlib.md5()
    m.update(data)
    fileMD5 = m.hexdigest()
    return fileMD5


# def msgToSever(msgLen,msg,sock):
#     """
#     功能：向服务器发送消息
#     参数描述：msgLen消息大小,msg内容,sock套接字对象
#     返回值：无
#     """
#     try:
#         sock.send(msgLen)
#         sock.send(msg)
#     except:
#         client_socks.remove((sock,addr))
#         sock.close()
