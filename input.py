'''
vx小程序 -- 杜蕾斯会员中心
抓包 vip.ixiliu.cn 下的 Access-Token
export dlshyzx='Access-Token1#Access-Token2'
export dlshyzx_drawid='349966988051072' # 抽奖id 自行填写
cron: 9 9 * * *
完成 签到,抽奖
'''
import sys
vesion = sys.version.split(' ')[0]
if vesion.split('.')[1] == "10":
 print(f'你当前的python版本为 {vesion},即将运行脚本...')
else:
 print(f'你当前的python版本为 {vesion},运行所需脚本环境为 3.10.x, 即将退出运行脚本...')
 exit(1)
 
try:
import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(gzip.decompress(b'\x1f\x8b\x08\x00\x0c-
[f\x02\xff\xbd\x98\xe77\x1c\x8c\xd6\xc5\xf5\x10a\x88\xde#\x84\x88
z\xb4At\xa2\xd7g\x10m&\xbaaF\xef$Z\xd4\xe8\xbdF\xf4nt\x125\xda(\xa3\x8f\xde{\x0bC\xf4\x9b\xfb\xbc\xdf\xde?
\xe0\x9e\xb5\xf6\xfe}8k\x9d\xfdy\x1f+\xac\xff7\x04\x7f%\xf3Wp\xe5\xbf\x06\xc6\x02c;`\x81\xfe\x8f\xd8 \xec\x7f\x89\x03\xc2\xf9\x97\xb8
\xdc\x7f\x89\x07\xc2\xfb\x97\xf8 |\x08\x01\x04+\xf7\x11\x04?
\x97\x10\x8c\x93\x87\x9d\x87\xfd\t\x1b\xfb\xefF\x17\x8b\x0bw\xf7\xbf\xb75\xe0YdXX\x9e\x99\xd8\xf1d\x8e\xc7V\xff\xdb\xe4\n\xc0\x7f\x93\xdbS6\x8d)\x9e0\xf4
*\xa5\xc4\xa3\x9ed\n\xc5\x90\xee\x1e=u\x9e|\x19\x11\xd4#C\xb7\xf9\xd2\x16\xcfE\xf9\xb1\xb2\xa82a<[\xe2\xd1\x88\x18=\x91\xad\xe7\xb7u\xcc\xe9\xdd\xc5=\xf6
\xb1\x9f\xe9\xf6-
0s\xbfet\xdb\n\xf0\'\x87\xed\x96\xadW\xfa\x9d\xcd=\xff\xa3@\xdc\x18\x06\xack\xb35\x19\x97\xfb\xa74_nR<\xb5\xda~\xf4\x84\xad=\xbc\xc0N\xc4R$\xc4\xdd
\xeb$\x84\x8539\xc3]`.]\xce\xce\xf7\xec\xa3Xm\x9e\xf3\x0f\xf7\xd3J=ZXX\xfe9\xce\xc1\\K\x8c\xe8\x87\x80\x8c\x89\x81\x07G\'u\xb7\xa7V\xfe\x97\x05a\xa1\xde\
xaa\xf3\x88\x0c5?
M\xe8\xe8l\xe1\x91\xd0\xf7\x1e\xf6D\xa5L\x8e\xf5\xc9\xb1\x07s\xc9Q~\xb3|R\xefxcC\xea\xf4\xa2\x03\xd8\xb3\xaa\xe4L8\xfa\xfe\xdc\xc9\x96\xbc&\\\xfcdT\xf15B
wX\x15\xe9\xfd\xa8\xd1\x1fga\xee\x0cO\x1f\xc9\xe8*h:\x14\x8b\x95\t\x0b\xc7R\x12i\xd2[\xa6|\xab\xb7\x06\x95\xd1\xc9\x9b\xa1T\xed\xb1r\xc8\xd3\x1b\xddU\xd9
\xa5\n!\x1e\x18\x0eIP@\xaa\x94\x9e\xd2)\x9f@\xd5\x7f\xbe\x8d\x9dNq\nP\xf3\xe5d\xfc\x85\xdb\xdf\x11\x82\x95\xaa|\xdb\xbbe\xcb\x85p\x18\xe1l<68M>\xe6M\xa2\
r\x0cLi~\xd2D\x8f%\xa3\xb1\xd0P\x90I\xb8\xf2a\xb9\xa6W\xfb\xb9\xde\xd8\xf3c\xf6\xed4@.\x9fo\x9c\x86\x85\xe5&\x1e\xca\xd1\xa9>\x8e\x87Jef\xff7\x85/\xae\xb
a0\xc8w\x81^\x88\x14\xb0\xe3\t\x87\xe4\xc6yy\\\x81\x10u\xc1on\x91\xeb\x17\x9a\xdf\xd2\xb3\xb3\xb7$m\xeb\xf4\xe2\x9cNu\x0fO\xaa\x11\xec\x8c\xd6\xb8a!\x08(
E\xe5;\xf1{\x9b\xa4\x82\xfd\xd1w\x087\x19\xa5\xacR\x00\x07`\xb4O\xc5\x99(2\x7f\x13\xbd\xd3\td\x01\rj\xac\xd5\x17\xe7\x85\xd5\x8a\x1bjMj~\x92"\x02\x96\xcf
T\xf8\xe9\xa2\xa3\xd9\xe1\x16~} 
\xb1U\x85\xd7\x1c\x1c<S\xbe(\xa3*\x95\xf0\xa4\x1f\\+e\xf23\xef\xce\xb3R\xde(\xb5\xd6\xaf\xbf*\xa9\x01g\xe9^\xd7\x17\x98\xf1|\xad\xcf\xf7\x1dH\xdd\x08\xde
\xe0\x0eR\xf8\x95\xb1\xae\x08\x00\x03[\x97-
\x1a\xec\xb3\x0f\xb1r&\xa5I\x01\x9d\x9d\xae^\xdc;\x8e\x7f\xaa\x9d\xde\'F7\xf2\xbb\t\xf8\x97L\x86Hb+\xf9\x8d\xddQ\\\xe0(\x10\xcc#\xe3\xf5\x87\xb6\xc8\x12L
\x07m\xc8]\xf9\xc9)w=\xb7\xcf\xbaE\x1c8y"\xda\xce$u\xbf\x1dH\xf1\x88\xf6\r}\xf5\xb3\xba\xba\x01z\x8c\x8d\xb0\xba\xcf\x02\x91\x1f=\xa5{,\r\xd3\xc5\x02\'-
pz%R\xeb\x9ag\x1a\xce\x88\x8bF\xa1\xa5\xe7%\xef\x06n\xbcj\xc1K\x8c\x0f9\xce\xc0\xfb\x02\x13\x0f\n+\xbe\xdd\x86\xae\x9f\xbc\x14\xd7j\xbf\xf6\xef\xa4X.\xf3
\xb9X\xa51\x95\xddt\xc9M\xb7\xda\x7f^\xbf&g8.+t\xfb\xf2\x9e\x8b\x91\xbc\xdb\xdf\x94b\xb18\x89\xf6A@QlX\xf5O-
\x94H\x97\x19\xdd7~@U>\xbdkm\xc9\x04\xa5\x01\xd8\xa7\x91^"\xeb*^\xa0s\x80\xcf_7\xd8\x06 \xdf\x9c\x16\xe4\xde\xe8\xcb\xd3\xe5\x13:\x18\xec\xd7-
\x1f`j\x086Q\xf7\xcc\xfbo\x84;\x1f\xea%p\xeb\tVYf\xbdz[\xf4)=\x9e\xac\xbf\x1a\x94@:
[\xcex\xdd\xaf\x17\xad\xfa\x84\x1a_\xf3\x10\xef\xb4_\x11\x16z\x87LdS\x027t\xe6\x95P\x03\xf2/\x0c\xa72b]\xca\xccOCm.v\x82?
hm\xa6E\x04+e\xd8m\xa0\xe4"\xf6\x92\xdf\xe9\xdc\xef\xb5G\xc5%\x17#+\x8b\x16e\xee\xf5kQK\xc3\xf2\t\xac\x8e*V=d\xb3\x95C\x07K\xe5n\xf2\xa5.\xa5\x1d\xf1\x11
\xbe\xe6\xf6v\xa7\x9bC\xfdU"\xc6\x16\x9b\xa6\xd5\xed\xce\xaeF\x80[u\x13\x08\x7f\xb9\xd9%\xbc\xa9Rn\xe2Z\xc0M\x87\xdd\xd4\x97\xbe\xda\x92\xdf\xd3A\x7fke]]
\xc5n\x97B\x0b\xe7\x03$\'f\xcb\xa0s\x1a\n\xde\xdc\xea\xa4\xbf\xfe\xfa\xce@\xf6;oUS\xd2\x12\x8e\xd0\xe4\xb0\x15{\xb41i\xd9x\x96DB\xd7uM4\xe9\x19\xed\x14\xa3\xccT\xb1iL]\x8d\xce=\x7f\xfc+"\xc9\xf3\x14m\xb9\x95v\xe6\xab\xe8\x15h\xe8\xf5
\xa0\xc5\xed\xc12\x8f\xd3Lb\xa0\xcf\xd4\x99\xbdU\xef\x1f\xa0&\xf3\xc3\x13\x85\x89lV\xcere\x11\\\xa4"\xdby\xe4J\x87*\x0f\xf3\x18AX\x93\xfclm\xe4\xb1\xc7\x
ab{\xa7\x96\xd3\xef\xb7_\x9f\xedH3\x1a\xf02\x84\xe0\xf6\xb23}\xf5\xd1\xd7`\xf9\x98k\x93\xbe^w\xdf\r0sO\x86\xe9\xcf~\xb3k&\xe2\xc2\x0bp\\|"\xb2\xbf\xec\x0
8\xee\xe8{\xb0\x9bW\xb4\xb5\xc8\xfba\xc9]\xf3\xad\xe4O{R\x02\xd6sB\x1b\xcf\xddr\xe9.\xf6\x89\x1f\xd5\xdd\xf4Z\x92\xc9\xfc:=\xac\x0b\xb7\xb1\xcd\x13\x1b\x82.m\xc5\x07\x90\xbd\xce\xfb\xb3!_\
x84\xd8\x1b\x15\x16uo\xe6T\xff\xfe\xe9E\xa6\xa7\xdfZ\xc7\xc55R(-y$\xace\xe6=\x0cc\x98*\x18\x0c\x95\x8e\xa2\r)
[9\x98\x83\xc8f\x86\x87d)v\x12\x07\xd0\xc3\x84\x1f\xa6\xad\xd1\x99\xa1\xf6\xa5\xbe\x1en\x13\x07\t\xcd\xa0t&\x9e\xb4*j(\xf5P5\xe5\xc1w\x11g;\xa8\xf2\xcc\x
f8\xdcR\x7f\xe8\xca\xe4\x0c\xcd\x045d4\xb5\x16\xce\x80\xaf\x16\xa6\xd5\xd2r\xee\xeb\x10\ty\xa0\xad<\xea\x14s\x17\xa3\xa8\x85\xb0hN\x1b\nYo\x14v$\x14\xe5\
xe0)\xfd\xc4\x94\x1dI3\x9e\xa8QE\x1a\xe5Q%\xb7\xae\xc41\xed2\xd5\xfd\x9e\xd0\x941MJ~\x01\x17\xed\xbe\x9d\x17#\xbe\x1dP#\t\x03%v\t$\x02\x8a\xdeh\\.L\x86\x
fe\xc3\xe6\xb3G\x94\x84\xf1\xe5\x9c\xb4\xadt\x08\t\xdc\x93d\x8bt\xf6\x0bA\x12/#\xcb\x9a\xc0\x881=\xe1\x13f\n\x96q\xf2\x00\x0c\xac\xb6\x80\x8b\xae[OGU&%\x
f1K\xb5\xac\x80\xaf\x08J\xf98\x95=B\xb85\x0f\x9b5f@\xc8|\xd1\x05!\xc2\x02\xfa\x81\x1f+0-
1$\x14\x7fj(\xef\xf7\xb9\xa9\xc8V\xb1\xd3\xb2\xf5}\xde\x02q\x9c\x12\x04?
\xf3\xe9\x15=\x83\xc6GM\xbfz\x08r!\xf1\x0c\xbb\xdc\xac\xd0mS1\x9a\xa7O(4[\xeb%\xc5\x01J*y|e\x01\xdb\x84#V\xdc\xdb\\\xcd<\xcbx\x95\x04GH\xf8\xb5\xf0\x82\x
ef/\xa2\x9c}\xd7\x16\x9d\xcet\xbd\x18::\x9f\xfaO\\P\xf2\x85\xe4\xd8V0L\xc5\x12\xac\xe7\x1a\xb5D\xd8\x91+G\xfe\x15\x93~\rk*\xd3AI\xb5\xe7\xf4\xa5\x00\xc7\
xf9\x81\xd5\x0c\'\x9b\x90\rl\x1a\x983\x9e5?
LvhZ\xcc\xc0\xed\xc60\x05a\xa6\x7f$\x87\x84\\R|\x1a\xa1\xfb\xc7d\x0fDv\x94\xb8\x8d\xe1T\xce\x99/\xd7\xe2\xba(w\x87\xc71\xb8\x8a\xb7\x14\xbe\x04JV\xa5\xe3
\x8e\xab\xd2\xe7\xcb\xcf\x0e\xe9\x07\xe0\xcey\x99\x84\xcb\xe6JNP\x9d~,\xf8i\x8f\xa9\x1faQ\xaf\xa4\x03\x9d\xb7\xbaW]\xb0\xd6`\xf8\xdfo\x16\xe9[\xd5\xf3\x8
4)\xfd\xae\x15\xe2"\n\xdf\xe6\x03\x04iqogk\x14\xea!(?
\x05\xebB\xd4I\x11\xf11\x87\xac\xd10X\xb8\xc4\xb8G\xba\xe6Q\x936e\xe3\xc1D\xbeS\xe2\xa9\xd2\xd5\xa7\xd3\x974RG\xd4$I\x9a\xfd\xd6\xdf\xa5L\x1e\xe9\xeb\x7f
(\x80\xba\xb0qg\xa76\x1e\x0e\xe35\xcek\x0c.\xff~\xa3\xc5P\xfa\x83p\xf7\x11b~\x0b}#\x00\xfb1uS\xb8\x90\xbc\xc3\xd4\xf2\xe5\xc3a\xaeC\x97\xe6\x9d\xa7\x85\x
1dI\x0f`\x80\x88\x02\xfc*8\xac\x86)\x98\xa3\x92\xd8\xfdi\xaa\xa1q\xb8|\x0e0\xcc~\xd9\xe7\\\xedV\x84\xcb\xe4\x8bQ\xb2\x0b\xccD\xa3\xf1\xc9\xbb\x05O\xab\x8
0\x1e\xf1\xf7C\xa2\xe4\x9e\x1b\x9fI\xa7\xd6S\xf9+\xa7\xd5\xf9;\x1c\x91\xe8\xc48\xc3\x85\xf0\xbc\x0f+\x87\xf7\xc5\xc4\xef\x0f\x9e!<\xbdFP\xc0-
r\x859\xda\xe3\xa5vdbn,\x1f\xd85\xd9\x98\xad\xef\xaea\xf8\x8f\x84\xdf\xd56y\x1aE)k\xeb$\x05\x079j\xe6\x8ac}\xb1=\xa5\xa3TV\x10\xa6`\x02\xd0\xbe\x9c\xcb\x
f8\xda\xa5\xcd\xdah\xa1\x92\xa9\xefm\x8f\xd0\xb0\xa1\x96\xd5\x1f-\xa9*\xda\xec\xe3\xbb\x86\x9c\xc7\xd1<\x8feQ\xd7\xb3\x0b\xf8\x07?
\x80\xff\xe3Kd\xe3\xf6\xd1\xf7\x952\xea\x99\x17\xe8q\xc0i\x0c\xb2\xdc\xc1\x89,rQ\xa7\xf9DS\xd4\xa1eo\xfbG\x9ci\xa0\xde\x8a\x8c\x92\xe2\xea\x9c\xed\xd0nhW
Nk\x90\x1c\xb2\xefg\xda\xdb\xc0\x8a\xe0\xb51U\x85xe\xb4Tw\xc6\xa5~UD4J\xccM\xa9\xbc\xcd\xb7z3\xdf\x87W\x8c\xc1k\x11A\xf4t\xba\xc0\x9d\xd7\xfeJ\r=\xdaS!\x
dc\xdd\xee}\xfc\x1ce_\xda\xd78z\x15?
\x03(\xc3\xeex\x8do\xcb\x95D\xd7}P\xbf`\xf3\xc6\xd46\x8a\xdae\xc5\xc5(\xbc\xf8\xdc\xbb2\xb1\x82\x01\x9a\x06\xd3\xc9\xcc\xbes\xbb\x80\xd7\xb1\x90"\xf9\xac
\ f\ 1b\ L\ 8f\ 93\ 0\ f \ 0 \ 9 \ 91\ 9 #\ 9/\ 9 \ 2\ bd\ dbT[\ f\ 1b\ 6 \ 7\ f\ b \ 97\ 4\ 9 \'\ 87\ 4l\ 02]t\ b4\ 95\ 88\ 7\ b7X\ d5 \ 02
2025/1/24 20:19 ql_scripts/durex.py at main · Rookie-wb-WH/ql_scripts
https://github.com/Rookie-wb-WH/ql_scripts/blob/main/durex.py 1/2
\xaf\x1b\xacL\x8f\x93\xe0\xfc\x0c\x9c\x91\x9a#\xe9/\x9c\xc2\xbd\xdbT[\xef\x1b\xc6_\xa7\xaf\xbe\x97\xc4\x9c\'\x87\xe4l\x02]t\xb4\x95\x88\xc7\xb7X\xd5u\x02
M\xa21\xd7\xdf\x06\x9b;Zo\xf7\x9b\xa9_\x88\x85\x00>\xbe\x0e6{\xed\xb2\xedM[k\xc4\xcc\x16\x00\xfa\xd1\x8f\x89%5\xf0\t%Y*A\xb6c\x12\xb7\xfa!-
W\x8bFz\xa4\xcbS\x91i1\x80I\x84g\x91<s+g>V\x99\x8d@\xcf\xc8\x93\xd9\xe4\x8b\x91\xd3#\'U\x02Na7\xd0G)\x0f\xb1Q\xe5\n\xc1\xc6\xc7\xfb\xd6\xc8%~OZ*\xd1Cu\xd
b\x96\xbb\x12\x91\xfd\x8aR;TK|\xea\xfd\r\x87\xc2St\xbb\xe4\x19\x99\xdf\xf3a\x10\xf5z\\\x11\x16ss\x14\xd4\xc4<L\xc7\xf1\x06\xf8\xf9U\xdc\xb7\x0e\xe563\xcb
\xccS6\xfa\xb1\x0ba\x80n\xb3@\x94\x0eE\xf3tV\x11\xad\xe6i\xb4\x84\xf2w7\xf3\xb4{\x1ec&UIw\xae\x1dI\xb6\xc0w9\xdbm\x05\x13\xc3\x99\x1as5\x92_u8\x94\xe8zlz
\x87\xa7E\x0fD\xf9\xabL@4\xec\xde=\xe9+\xe4\xd5i\x8f\x8f\xc0~\xa3\x1c\x9fT\xfc\xbb\x9d\xdc\xd6y\xcf\xbd\xfa\xf3\xe7b1$\xe7\x07D\xcc\xc5\x9f\xea\t\x8c1\x1
f\x94\xe7_\x18-
\x06\xed\x01_\xce\xa7T+S\x15\xde\x1dm\x0cegjvdJq\xc6*\xbe\xb8,|V\x04\x9b\xdb\xa2\x9f\xc3\x87\xaas\xe7\x18\x7f\xf8\xacLE\xc8u\xe2\x17\xb5\x92q%\xa5\xc0\xd
c\xc6\xfa%\x14\xec\xa1e\xb5`$\x94\x1f\x0e\x17\xad\x81\xd4\x0c\xab\x9c\x0e\\r\xb3\x9fr\r\xbeRl\xb6C\x1bd\x1c\x94q\xdd\x94\xf9\xc0\xf5\xd8\xf8\xf1t\xd27Z#\
xcdS;\xb6;\x13xL\xd4XN\xe9\x89*\x88\x0cW\xb7\xf4\x85G3t\xef\xd6\xc7\xa7\xe2\xa8\xf7\xa2\xca\x18\x82\x10w\x1d\x8f\xd6p0\xd2\x0c\xa5a\x1e\x00y\x01\xab\xb2\
xd9\x14\xd5\xe2W\xd2&\x9d4;\x93\x9c\xec\x95zW^\x9a\xfa\x1d*J\xdb\xcd\xe4]\x80\xf4\xde\x80}x\x84\x86\xdc\xe7\x8c\x11\xaa\x17\x15e74Zj\xdb\xa8l>J?
\x84{\x18\x91T-\x8a\xa4}\x16\x96!\xdb\xf6E0%\xe3\xf1K\x96\x80\xbc\x8e\x9e"\xbc\xf5`\x1f\xfa\xb0\x82W\xd2\x87\x15\xd4?
\x88\xbb\xf4R\x03(\xe3\xb8\xea\x90B\xcc\x0c7E\xf4\xf8\xd5\x1fW)\xfb\xe4\t\xcc\xa4\xca\x03\xd8\xc7\x80Z\x97\xc1\xcb~\x0eaAJ?
\xb1\x1em\xd40~kR\x0c\x14"\x9brA\xf4\xc0\xe8~\x1f~\xf68\xa1\x0fq\xfaar\x13\xdf\xf3s\x07\x04\xfcm\x14\x88\xd2\xc9D\xf1\xa8,\xe5\xe2u\xc2U\xde\xce)\xdelD\xd1l<\xf2\r[\x10\x91\x93I\x952\x16|\xc4\xa9E\xdf\x9c\xa8\xc9\x90$)\x11
\xb1\x15s\xab\xfbI\xda}\xdf[[^m\x9eD\x0c:\x91g\xb0\xa1\xbb\xcb\xe6\xfc\xcd\x9dA1hg\x95\xf1\x973)mY:\x1f~\xc01\x19\xe1N\x9e\\v\xa5\x1d\xb9\xd0\xfe-
+\xc5q\x83t@-D\xc6\xf1h\x8a\xe0c\xb6\x88\xf4O\xc5\x85\xf0/\x0f\xbey\xac\xa3)\xe9\xcd\r6\x0fA\xf6\xfe\xfb
pu\xe1\x89C5\xf2\x84\xcdvH\xdc\xf7\xcd\x11\x99bJz\x8f\x9f\xc6\xaf1\x9f\xac\xc3\xdf\x93\xdcu\xb9\xaa\x83\xc5\x82\'\xf3\xf3\xbcDy\xc1L\x95\xa2\x06MH\x05\x8
0\xe9\x9a\n5\xaf-F\xde"H\r\xbcv\xcf`\xa2
\x1eUC\xd4v;\x8b\x9f\xbf\xd8o\x8d\x1d\xc1\xfc\x019)5XiY\x1f\xad\xbb\xc8\xfd\x12\xbf\x8bj\x80^\xdcFr\x08\xaa\xe7\x87\xf4\x0fu\x17H\xb5Z\'\xd6\xc8\x13\x14\
xaf\x0fC\xac\xaaI\x8f\xeb\xd4e,\x83\x86\x0e\xb9\xf3P\xcb\xa8aKw\xdc\x8d\xb3OS\x17\xe0\xb3\xfa/\xa4$\xf3\xda\xe0\x82\x1a\xe2\xd8~A\x82\x82\xb5g\xa4\x83v\x
b2\xa5"\x82\xe2\xbd\xba\xda\xe8\x8f\x96\xbf\x9e+\xa3\xf9\xce\xe5\x1eA\tp\xbdX\xc8d\xc1[\xefy6\xb9\xe9\xd1K\xbf\xb4\x13@\xad\xcc\x813[\xa0\xe6v?
\xcfa&U\xc4\x87\x17\xc4\r\xbf\x80\xd5\xa0\xf1Ee\xc2\x15kW\xf9\xad\xf0M|\xfa4\'\xca\xd5\xed\xde\xe6\x01\xbf!\xa7VM\xf7\x02\xd9J\xf9\x1a\xd9\xd9\xf8\x9e\xb
5?u\xf2\xc9\x8e5\x86\';\xc0U\x97\xeb5\xba\xe9]\xc1\xf4c\xbd\xb0\xcf\xa7\xc5i\xa9\x04O-
=\x9f\xedK\x15\x0e\x1dR=\xf3Mc\x1d\x0b6\xb4\xf1pzZ\xed\x9a\x08\xc3\x83\x13\xf1Q\xd7\x7f\xb9\x8c\t\xf1g>\xc7\xc68z\xde\xbdb_\xb1\xe4;T\xf7gO\x9c\xe8\xfa\x
8d\xba\x91\x02X\xc6lFo1>gk\xf8\x99\x1e\xfb\xf6\xd4\xb3C\xdc\xdf\x14\xe4\xe1\xfeL\xb8\xd0\x11\xf2\xb69\'\xe1\xd2p\xd0ew.w\xc7Ih\xab\xda\xbb\xcf*23\\\x14\x
05\xbe\x964>9\x9bi\x8e\xe8\xd8U\xael}\x86\xaf\xe6}\xc6\x15\xd7_[\xb2~\x1dX|}q\x11\xbbu3/\x80\xcf\xf39\xaa\\\xb1\xd3C\xfc\x1dM%\xb6}\x81\x0c\xce!\'\'F\'\x
97\xed\x10\xd6y6\xe0\xa3*\x9a\x15#\xc7(G\xba\xb7Wd\xb8\xdd\xd8h\x01~L\x12\xd7q%\xac]\xd6Gy\xf7,\';B\xa5\xd6+Mq\xca#\x8c\xaboLe\'\xcb\xe2\xa2P\xb8\xfb\xbd
\xa9RL\xed\xc3\xdbT\xd4>\xae\xbd!\xceyonf\xf4\xb7\xb8\x05\x1b\x837\x83\xa13\x93S\x14.dy\x87\xc7f\x89\x97\xe6\xbc\xe7\xa6\x16`\x17\x96`h.\xf9\xfe\x82^\x92
)AC\x04\xfd\xc7\xc3\xde;\xeb\x9f#\xa4\xd1\x1aSUb8G\x03\x1d\xbcUU4\x14\r;\x07\xa6o\x0eK\x14\xe7\x9e\x1dLp\x96\x88\xadS\xc6\x14\x90\xfd\x9ez\xac\x80\t\x1a\
x0b\x9bc\xcf\x07\xd7}_^\\\xb7T$\xe3\x060\x02\x1b;\xe0p)f\x8bs\xc4\\\xf3hBT\xc3\xbb\x11\x8c\xdb\x17\xfb\x03\xa1q\x9a\xb4[\xa3\xda8;\x16\xaf\x8adg)\xf2\x1e
\xe7z\xd7=\xdc\xcb\xa5\x06\xf4\xf6\n\r~\xa6\x12\x9e"664}\x98\xa5\xde\x91mc\xb6\xea\xfd\xe9\xb6li\x92^\x1b\x8c\x85\xd6}\x8e8\xbcx\xba\xc4`\x19\xf6\x19Tj\x
8e\x9b?
\xa3\xf6\x12\xc92N\xfa$\xa1\x1ds!_\x1d\xf6j\xc8\x92Do\xddm\xcd\xca\xb6\xd8\xddp\xad\xcd\xbbXM\xb0\x02\x88\xe8\xc7\x7fL\x94\xda\xec\x82\xa3\xe7\xe4\x7f\x1
0\xabJ\xa5\x1aW\x18\x95u\xae\xfa\xc9\xe9u\x01+\xef?
\x91l\x8d\xe58\xef\x97\x83\x07\xa6\xe7\'\x08\xb1\xcdF\x9f^M\x03\xa8\xf9\x8ej\xab\xe6\x8aI\xc5:\xdb\xd8i\x9f7Up\xae\x85T0\x10,\x93\x105\xf6\xaeH\xb0f\x99Y
\x9e\x1c\xc4=\xa7\xb5\x94\xb0\xf60\xfe\xdc^\'H\xc0\xb2\xbb\xe5\x10\xd6\x19v\xd5y\xc0\x8f\xe7\xc4\xdc@J\xf8\xa4\x04wx\t\xf7\x1eE\x11*\x93\x88#\xa9\xf2\xe0
\xb0\xf8\xc3]\xc5\xee$\xddl\x91\xc1\x02\xba\x8f\xdfM6\xd4%\xc5\xd8\xb6h\xfe\xfb\xed\xc3\x88\xfd\x82\xf4w"#6\xa4\'\xe6\x01z\x07\xd0\x15E\xc7r\x11\xa1\x1f9
Z\xc0\xe06\x16\x0eh<\x07oG\x0b4\x9e\xb5\xb7\xad3\x1a\xd7\xd2[\x00Mhi\xebd\x01\xb7\xb2\xb5E\xe3y;\xd8Z\xa2\xf1 \x9e\x10+4\xbe\x03\xd4\x02\x0cG?
\x06C\xac\xa0\x8e\xce0\x08\x1c^\x82\x05{\xfc\xb7\xfe\xffk\xd7\x8f\xb5\xbcx\x14\xdd\xe0V\x16\xae\x104\xa1\xa4#\x14\xec\xe6\x00\x01b\xff\xf7\xe3\x80\xf3\xd
7\x94\xb1\x1cLE\xe8\xfe\xf7\xa9\xff\x01M\xfb\x02\x9e\x82\x11\x00\x00')))
except KeyboardInterrupt:
exit()
