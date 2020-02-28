
from selenium import webdriver
import time 
browser =  webdriver.Chrome()


browser.get('https://i.qq.com/')

browser.switch_to.frame('login_frame')

browser.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
time.sleep(5)
# 填写用户名：
browser.find_element_by_xpath('//*[@id="u"]').send_keys('842549758')
# 填写密码：
browser.find_element_by_xpath('//*[@id="p"]').send_keys('842549758')
# 点击登陆
time.sleep(5)
browser.find_element_by_xpath('//*[@id="login_button"]').click()


/cap_union_new_getcapbysig?
aid=549000912&
captype=&
curenv=inner&
protocol=https&
clientype=2
&disturblevel=&apptype=2&noheader=&color=&showtype=embed&fb=1&theme=&lang=2052&ua=TW96aWxsYS81LjAgKE1hY2ludG9zaDsgSW50ZWwgTWFjIE9TIFggMTBfMTRfNikgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzgwLjAuMzk4Ny4xMjIgU2FmYXJpLzUzNy4zNg==&grayscale=1&subsid=3&sess=OcDPl20MMPSAAbkA5kMyAMu2dnHCIFgRR9ulO0gfl0R3dnLPaO2K1Fh-V9MvLdLchmcsQY2wFBEXlxtmDbCmqexyo-EF2Py_ulc-nQsipaDXrYcb2bKPNkmbcRAM6mtBM3RuS-kBplDYmmmfNiPegWV9cZaeCDy7zxr3I92YUWOGE0NVJzWysvqt_OIxzv3Nrck4pm9L9WU*&fwidth=0&sid=6798499577039931376&forcestyle=undefined&wxLang=&tcScale=1&noBorder=noborder&uid=1043363473%40qq.com&cap_cd=-h5McKflg8gSZ6Ivf2ETN-Q_jZhcANubXG9SgmT5n8qEkqnHkF5FfQ**&rnd=493307&TCapIframeLoadTime=294&prehandleLoadTime=78&createIframeStart=1582899032453&rand=22940423&websig=799aef64137066feb39a2e3ef2228cf3a6fddccb49a1df7bca6b0f1ce496600c6b8619b9f02d0428046229c72fe47c1d9ba85b38cadd8e0a967e92898bc3c5e8&vsig=c012Gbkwtk42yQ18LznBq-DzuMDUQDQZ1S-bqMwV2NoUVs9BDgtOKw635A-mGLz8gY06zY4_bjSmWw6zaJVKo379gnCLhiJOePqEuwHQug8QsrceP_9QIQBm5MJ2Bid1YTXjJYm5XiNRPNGxo2D6xs8IB2QC79SCD-MW7uBXvewvpZ-B29S_ab9Bw**&img_index=1、

