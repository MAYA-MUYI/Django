import os

if __name__ == '__main__':
    print(os.getcwd())
    now_pwd = os.getcwd()
    print("now:", now_pwd)
    # print("1:",os.path.relpath("F:/ServerveManager/Pycharm/PyCharm 2018.2.2/files/oss_test1/MyFile.txt"))
    # print("*******************")
    # path = "..\static\cloud"
    # print("2:",os.path.abspath(path))
    # print("*******************")
    # os.chdir(os.path.abspath(path))
    # print("3:",os.getcwd())
    # print("*******************")
    # os.chdir(now_pwd)
    # print("start:",os.getcwd())
    # temp_path2 = "..\static\cloud"
    # os.chdir(os.path.abspath(temp_path2))
    # print("***************")
    # print("process:", os.getcwd())
    # os.chdir(now_pwd)
    # print("finally:", os.getcwd())
    dir_path = os.path.abspath('static/media')
    print("dir",dir_path)
    temp_path = "..\static"
    os.chdir(os.path.abspath(temp_path))
    print("change:",os.getcwd())
    os.chdir(now_pwd)
    print("after:", os.getcwd())
    temp = '..\static\cloud'
    os.chdir(os.path.abspath(temp))
    print("last:", os.getcwd())