from codecs import encode
import srt
import os

# 对分开的字幕进行小时修正
# 01:00:01,760 --> 01:00:07,520
# 修改为
# 00:00:01,760 --> 00:00:07,520
def main():
    # 打开文件原来的文件,因为不是python文件的UTF-8编码，需要使用二进制方式打开
    a=open('001.srt',"r",encoding="UTF-8")
    a1=a. readlines()

    # 
    # 创建新文件写入
    b=open ('001_2.srt','wb')
    b1=[]
    for i in a1:
        # 把二进制的转为python能识别的字符
        # i=i1.decode("UTF-8")
        # 转换后的i1  = 每行都有空格和换行符=
        # 查看b1列表中第2个元素进行长度为31
        # 原数据为
        # 01:00:01,760 --> 01:00:07,520

        print(i)
        # 把转换好的字符进行判断
        # 当找到这行时匹配的字符长度时，
        # 进行二次判断  下标0的为0，下标18的为0
        # 两次判断为真的，进行更改数据再写入
        if len(i)==30:
            if i[0]=="0" and i[17]=="0":
                # 因为字符串不可修改
                # 所以需要拼接
                # print(i[2:17])  下标第17位不包括
                u=i[0]+"0"+i[2:17]+"00"+i[19:]
                print(u)
                print(len(u))
                b1.append(encode(u))
        else:
                b1.append(encode(i))

    # 写入文件
    b.writelines(b1)
    # 关闭文件
    b.close()
    a.close()

main()

# 有可能需要安装srt插件，一般不需要
# 1需要升级pip
# py -m pip install --upgrade pip
# 但是链接源被墙了
# 看下是不是使用了vpn，不能直接访问，违反了ssl协议
# 2需要指定源升级
# py -m pip install --upgrade pip -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
# 3安装稳定版本的srt   
# pip install -U srt
# 安装后显示版本[srt          3.5.2]
# 使用指定源方式安装
# pip install -U srt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com



