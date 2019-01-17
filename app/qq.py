# 导入selenium工具
from selenium import webdriver

chrome_path = r"C:\Users\fanjianbo\Desktop\chrome\chromedriver.exe"
# 给浏览器加入无头操作，使得调取浏览器的时候不需要打开，只需要调用其内核即可
opt = webdriver.ChromeOptions()
opt.add_argument("--headless")

# 根据驱动所在的路径创建出一个浏览器对象
driver = webdriver.Chrome(options=opt)
# driver对象可以操作浏览器

driver.get("http://www.baidu.com/")

# 获取页面上的某个标签元素
btn = driver.find_element_by_link_text("新闻")
print(btn) # <selenium.webdriver.remote.webelement.WebElement (session="882d80ac23a0bae39f23620a15bf539d", element="0.8632697600782313-1")>
# 点击
# btn.click()

# 找到输入框
input = driver.find_element_by_id("kw")
input.send_keys("老王")
driver.find_element_by_id("su").click()

# 对于爬虫来说，更关注于做了某些操作以后，得到的页面源码
html = driver.page_source
with open("baidu.html",'w',encoding='utf-8') as fp:
    fp.write(html)

driver.quit()
