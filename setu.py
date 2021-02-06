import sys
import os
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from ui_setu import Ui_setu
import urllib.request
import json
import pyperclip
import traceback
import webbrowser
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
VER=4
VER_TYPE="Relese"
def get_record(url):
    req=urllib.request.Request(url=url,headers=headers) 
    resp = urllib.request.urlopen(req)
    ele_json = json.loads(resp.read())
    return ele_json
def md(s):
    try:
        os.mkdir(s)
        return True
    except:
        return False

class setu(QMainWindow, Ui_setu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.a1.triggered.connect(self.fget1)
        self.a2.triggered.connect(self.fget2)
        self.a3.triggered.connect(self.fget3)
        self.a4.triggered.connect(self.fget4)
        self.a5.triggered.connect(self.fget5)
        self.a6.triggered.connect(self.fget6)
        self.view.triggered.connect(self.fview)
        self.copy.triggered.connect(self.fcopy)
        self.copya.triggered.connect(self.fcopya)
        self.web.triggered.connect(self.fweb)
        self.web2.triggered.connect(self.fweb2)
        self.rsize.triggered.connect(self.frsize)
        self.rdir.triggered.connect(self.frdir)
        self.rset.triggered.connect(self.frset)
        self.favo.triggered.connect(self.ffavo)
        self.fava.triggered.connect(self.ffava)
        self.favc.triggered.connect(self.ffavc)
        self.favd.triggered.connect(self.ffavd)
        self.favr.triggered.connect(self.ffavr)
        self.sear.triggered.connect(self.fsear)
        self.uplog.triggered.connect(self.fuplog)
        self.about_this.triggered.connect(self.fabout_this)
        self.clears.triggered.connect(self.fclears)
        self.idel.triggered.connect(self.fidel)
        self.checku.triggered.connect(self.fchecku)
        self.opens.triggered.connect(self.fopens)
        self.hei="0"
        self.wid="0"
        self.lin=""
        self.f=""
        self.fromw=""
        self.dir="setu"
        self.size=0.5
        self.img_pix=None
        self.show()
    def keyPressEvent(self,event):
        print(event.key())
        if event.key()==16777218:  #Shift+Tab
            self.show_debug_information()
    def show_debug_information(self):
        de=f'''self.hei={self.hei}
self.wid={self.wid}
self.lin={self.lin}
self.f={self.f}
self.fromw={self.fromw}
self.dir={self.dir}
self.size={self.size}
self.img_pix={self.img_pix}'''
        a=QInputDialog.getText(self, '调试命令', de)
        s=a[0]
        if a[1]:
            try:
                exec(s)
            except:
                e=traceback.format_exc()
                QMessageBox.critical(self, "调试命令报错", e)
    def download_img(self,img_url):
        try:
            request = urllib.request.Request(img_url, headers=headers)
            response = urllib.request.urlopen(request)
            img_name =  os.path.basename(img_url)
            filename = self.dir+os.sep+img_name
            if (response.getcode() == 200):
                with open(filename, "wb") as f:
                    f.write(response.read())
                return (True,filename)
        except:
            return (False,traceback.format_exc())
    def fabout_this(self):
        html='''
<p><strong>关于 二次元图片</strong></p>
<p>作者：[熊熊糖果]</p><hr>
<p><a href="https://space.bilibili.com/478010346">哔哩哔哩</a></p>
<p><a href="https://shequ.codemao.cn/user/3819961">编程猫</a></p>
'''
        QMessageBox.about(self, "关于", html)
    def fuplog(self):
        html=f'''
<strong>更新日志</strong><br>
<p>当前版本: {VER_TYPE} {VER}</p>
<hr>
<p>新增功能：</p>
<p>1.检查更新</p>
<p>2.开源状态</p>
'''
        QMessageBox.about(self, "更新", html)
    def fget(self,url):
        try:
            j=get_record(url+"?return=json")
            self.lin=j["imgurl"]
            self.hei=j["height"]
            self.wid=j["width"]
            d=self.download_img(self.lin)
            self.f=d[1]
            self.img_pix = QPixmap(self.f)
            self.img_pix = self.img_pix.scaled(int(self.wid)*self.size, int(self.hei)*self.size, Qt.KeepAspectRatio)
            self.img.setPixmap(self.img_pix)
        except:
            e=traceback.format_exc()
            QMessageBox.critical(self, "获取图片失败", e)
    def fget1(self):
        self.fromw="http://www.dmoe.cc/random.php"
        self.fget(self.fromw)
    def fget2(self):
        self.fromw="https://api.dongmanxingkong.com/suijitupian/acg/1080p/index.php"
        self.fget(self.fromw)
    def fget3(self):
        self.fromw="https://api.ixiaowai.cn/api/api.php"
        self.fget(self.fromw)
    def fget4(self):
        self.fromw="https://api.mtyqx.cn/api/random.php"
        self.fget(self.fromw)
    def fget5(self):
        self.fromw="https://api.mtyqx.cn/tapi/random.php"
        self.fget(self.fromw)
    def fget6(self):
        self.fromw="https://cloud.qqshabi.cn/api/acg/api.php"
        self.fget(self.fromw)
    def fcopy(self):
        if self.lin:
            pyperclip.copy(self.lin)
            QMessageBox.information(self, "成功", f"已复制图片链接 : {self.lin}")
        else:
            QMessageBox.warning(self, "复制链接", f"请先获取图片再复制链接")
    def fcopya(self):
        if self.fromw:
            pyperclip.copy(self.fromw)
            QMessageBox.information(self, "成功", f"已复制API链接 : {self.fromw}")
        else:
            QMessageBox.warning(self, "复制API接口", f"请先获取图片再复制API接口")
    def fview(self):
        if self.f:
            QMessageBox.information(self, "图片信息", f"图片高度 : {self.hei}\n图片宽度 : {self.wid}\nAPI接口 : {self.fromw}\n图片链接 : {self.lin}\n本地地址 : {os.path.realpath(self.f)}")
        else:
            QMessageBox.warning(self, "图片信息", f"请先获取图片再查看信息")
    def fweb(self):
        if self.f:
            webbrowser.open("file://"+os.path.realpath(self.f))
        else:
            QMessageBox.warning(self, "打开图片", f"请先获取图片再打开")
    def fweb2(self):
        if self.lin:
            webbrowser.open(self.lin)
        else:
            QMessageBox.warning(self, "打开网页图片", f"请先获取图片再打开")
    def frsize(self):
        self.size=int(QInputDialog.getInt(self, '图片尺寸', '输入图片尺寸大小(1-10之间)\n1为最小,10为原图大小,默认为5',self.size*10,1,10,1)[0])/10
        if self.img_pix:
            self.img_pix = QPixmap(self.f)
            self.img_pix = self.img_pix.scaled(int(self.wid)*self.size, int(self.hei)*self.size, Qt.KeepAspectRatio)
            self.img.setPixmap(self.img_pix)
    def frdir(self):
        dir1= QFileDialog.getExistingDirectory(self, '选取保存位置', self.dir)
        if dir1:
            self.dir=dir1
    def frset(self):
        r=QMessageBox.question(self, "恢复默认设置", "确定要恢复默认设置吗?", QMessageBox.Yes | QMessageBox.No)
        if r==QMessageBox.Yes:
            self.dir="setu"
            self.size=0.5
            if self.img_pix:
                self.img_pix = QPixmap(self.f)
                self.img_pix = self.img_pix.scaled(int(self.wid)*self.size, int(self.hei)*self.size, Qt.KeepAspectRatio)
                self.img.setPixmap(self.img_pix)
    def fsear(self):
        if self.lin:
            webbrowser.open("https://saucenao.com/search.php?db=999&url="+self.lin)
        else:
            QMessageBox.warning(self, "搜索图片", f"请先获取图片再搜索")
    def ffavo(self):
        try:
            with open("setu_favourite.json","r")as f:
                fv=json.load(f)
        except:
            QMessageBox.warning(self, "打开收藏", f"你没有收藏过任何图片")
            return
        v_fv=list(fv.values())
        k_fv=list(fv.keys())
        c=QInputDialog.getItem(self, "打开收藏", '请选择一个收藏的图片', k_fv, 0, False)
        if c[1]:
            try:
                fs=fv[c[0]]
                self.f=fs[0]
                self.hei=fs[1]
                self.wid=fs[2]
                self.lin=fs[3]
                self.fromw=fs[4]
                self.img_pix = QPixmap(self.f)
                self.img_pix = self.img_pix.scaled(int(self.wid)*self.size, int(self.hei)*self.size, Qt.KeepAspectRatio)
                self.img.setPixmap(self.img_pix)
            except:
                e=traceback.format_exc()
                QMessageBox.critical(self, "打开收藏失败", e)
    def ffava(self):
        if self.f:
            a=QInputDialog.getText(self, '添加收藏', '输入收藏的名称')
            s=a[0]
            if a[1]:
                try:
                    with open("setu_favourite.json","r")as f:
                        b=json.load(f)
                except:
                    b={}
                b[s]=[os.path.realpath(self.f),self.hei,self.wid,self.lin,self.fromw]
                with open("setu_favourite.json","w")as f:
                    json.dump(b,f)
                QMessageBox.information(self, "成功", f"已添加到收藏 : {s}")
        else:
            QMessageBox.warning(self, "添加收藏", f"请先获取图片再收藏")
    def ffavc(self):
        r=QMessageBox.question(self, "清空收藏", "确定要清空收藏吗?\n此操作不可逆", QMessageBox.Yes | QMessageBox.No)
        if r==QMessageBox.Yes:
            try:
                os.remove("setu_favourite.json")
            except:
                pass
    def ffavd(self):
        try:
            with open("setu_favourite.json","r")as f:
                fv=json.load(f)
        except:
            QMessageBox.warning(self, "删除收藏", f"你没有收藏过任何图片")
            return
        v_fv=list(fv.values())
        k_fv=list(fv.keys())
        c=QInputDialog.getItem(self, "删除收藏", '请选择一个收藏的图片', k_fv, 0, False)
        if c[1]:
            s=c[0]
            fv.pop(s)
            with open("setu_favourite.json","w")as f:
                    json.dump(fv,f)
            QMessageBox.information(self, "成功", f"已删除收藏 : {s}")
    def fclears(self):
        r=QMessageBox.question(self, "清除缓存", "确定要清除缓存吗?\n将要删除收藏以外的全部图片\n此操作不可逆", QMessageBox.Yes | QMessageBox.No)
        if r==QMessageBox.Yes:
            i=os.listdir(self.dir)
            s=[]
            for e in i:
                s.append(os.path.realpath(self.dir+os.sep+e))
            try:
                with open("setu_favourite.json","r")as f:
                    fv=json.load(f)
                v_fv=list(fv.values())
                for y in v_fv:
                    s.remove(y[0])
                for a in s:
                    if ".jpg" not in a:
                        s.remove(a)
            except:
                pass
            for x in s:
                os.remove(x)
            if len(s)!=0:
                QMessageBox.information(self, "成功", f"已删除{len(s)}个文件")
            else:
                QMessageBox.warning(self, "提示", f"没有缓存可以删除")
    def fidel(self):
        if self.f:
            r=QMessageBox.question(self, "删除图片", "确定要删除这张图片吗?\n此操作不可逆", QMessageBox.Yes | QMessageBox.No)
            if r==QMessageBox.Yes:
                os.remove(self.f)
                self.img.clear()
                self.hei="0"
                self.wid="0"
                self.lin=""
                self.fromw=""
                self.img_pix=None
                self.f=""
        else:
            QMessageBox.warning(self, "删除图片", f"你还没有获取图片")
    def ffavr(self):
        try:
            with open("setu_favourite.json","r")as f:
                fv=json.load(f)
        except:
            QMessageBox.warning(self, "重命名收藏", f"你没有收藏过任何图片")
            return
        v_fv=list(fv.values())
        k_fv=list(fv.keys())
        c=QInputDialog.getItem(self, "重命名收藏", '请选择一个收藏的图片', k_fv, 0, False)
        if c[1]:
            cs=c[0]
            a=QInputDialog.getText(self, '重命名收藏', f'{cs}\n输入收藏的新名称')
            s=a[0]
            if a[1]:
                v=fv.get(cs)
                fv.pop(cs)
                fv[s]=v
                with open("setu_favourite.json","w")as f:
                        json.dump(fv,f)
                QMessageBox.information(self, "成功", f"已重命名收藏 : \n\n{cs}\n↓\n{s}")
    def fchecku(self):
        try:
            j=get_record("https://xxtg666h.oss-cn-shanghai.aliyuncs.com/prog/st/update.json")
            v=j["ver"]
            d=j["link"]
            t=j["type"]
            if VER<v:
                s="你的程序需要更新！"
            elif VER==v:
                s="你的程序已是最新版本。"
            else:
                s="你的程序是内测版本。"
            html=f'''<strong>{s}</strong>
<hr><p>当前版本：{VER_TYPE} {VER}</p>
<p>最新版本：{t} {v}</p>
<p>最新版下载：<a href='{d}'>点击下载</a></p>
'''
        except:
            s="无法连接到更新服务器。"
            html=f'''<strong>{s}</strong>
<hr><p>当前版本：{VER_TYPE} {VER}</p>
'''
        QMessageBox.about(self,"检查更新",html)
    def fopens(self):
        try:
            j=get_record("https://xxtg666h.oss-cn-shanghai.aliyuncs.com/prog/st/open.json")
            o=j["open"]
            d=j["down"]
            if o=="0":
                html="<p>开源状态：<strong>不开源</strong></p>"
            if o=="1":
                html=f"<p>开源状态：<strong>开源</strong></p><hr><p>源码地址：<a href='{d}'>{d}</a></p>"
        except:
            html="<p>开源状态：<strong>未知</strong></p>"
        QMessageBox.about(self,"开源",html)
if __name__ == "__main__":
    md("setu")
    app = QApplication(sys.argv)
    window = setu()
    sys.exit(app.exec_())
