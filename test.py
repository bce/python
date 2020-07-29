# -*- coding: UTF-8 -*-
import chardet
 
a = "\344\270\211\345\220\210\344\270\200"
fencoding = chardet.detect(a)  #这行可以判断当前字符串的格式，以便后面设置打印字符的字符编码
 
print(fencoding)
a = a.decode('utf-8')
print(a)
