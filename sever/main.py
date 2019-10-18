import socket
import threading
import json
import pymysql

def msgToClient(msg):
    """
    功能：向客户端发送消息
    参数描述：msg，json消息内容
    返回值：无
    """
    print(msg)
    msg = json.dumps(msg)
    msgLen = "{:<15}".format(len(msg)).encode()
    try:
        sock.send(msgLen)
        sock.send(msg.encode())
    except:
        client_socks.remove((sock,addr))
        sock.close()

def recvJson(sock,msgLen):
    """
    功能：接收json数据
    参数：msgLen,待接收的json数据长度,sock,客户端地址
    返回值：jsonData,json数据
    """  
    if msgLen :
        recvSize = 0
        jsonData = b""
        while recvSize < msgLen:     # 接收json请求           
            tmpData = sock.recv(msgLen-recvSize)
            if not tmpData:
                break
            else:
                recvSize += len(tmpData)
                jsonData += tmpData
        
        jsonData = json.loads(jsonData.decode())
        return jsonData
        
def phoneLogin(phone,psw):
    """
    功能：手机号登录校验
    参数：phone,手机号,psw,密码MD5值大写32位
    返回值：rsp,响应消息
    """
    rsp = {	"op": 1,"error_code": 0}   # 0表示登录成功，1表示密码错误, 2表示没有该号码
    
    if phone:   # 查询手机号是否存在数据库
        if  phone and psw: # 数据库中有手机号和密码匹配
            rsp["error_code"] = 0
        else:
            rsp["error_code"] = 1
    else:
        rsp["error_code"] = 2   #没有该手机号
    return rsp



def client_chat(sock,addr):
    """
    功能：客户端线程函数
    参数：sock,addr 客户端地址
    """
    
    try:
        while True:
            print("已连接")
            msgLen = int(sock.recv(15).decode().strip()) # json请求长度
            req = recvJson(sock,msgLen)
            print(req)

            if req['op'] == 11:
                # 邮箱登录请求
                pass

            elif req['op'] == 12:
                # 手机号登录请求
                phone = req["args"]["uLogin"]
                psw = req["args"]["password"]
                rsp = phoneLogin(phone,psw)
                msgToClient(rsp)

            elif req['op'] == 2:
                # 注册请求
                pass

            elif req['op'] == 31:
                # 发送群聊消息请求
                print(req)
                pass

            elif req['op'] == 32:
                # 发送私聊请求
                pass

            # else:
            #     # 发送给其他所有在线的客户端
            #     for sock_tmp , addr_tmp in client_socks:
            #         if sock_tmp is not sock:
    except:
        pass
            
                


    # finally:
    #     client_socks.remove((sock,addr))
    #     sock.close()



sock_listen = socket.socket()
sock_listen.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
sock_listen.bind(("127.0.0.1",9999))
sock_listen.listen(5)

client_socks = []
while True:
    sock,addr = sock_listen.accept()
    client_socks.append((sock,addr))
    print(addr,"已连接！sock",sock)
    threading.Thread(target=client_chat,args=(sock,addr)).start()