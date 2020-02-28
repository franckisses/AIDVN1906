from selenium import webdriver

from selenium.webdriver import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

browser.switch_to.frame('iframeResult')

# 查找拖动的对象
drag = browser.find_element_by_css_selector('#draggable')
# 查找拖到那个位置
drop = browser.find_element_by_css_selector('#droppable')
print(drag)
print(drop)
action = ActionChains(browser)

#移动到指定位置
# action.drag_and_drop(drag,drop)

# 根据偏移量去移动
action.drag_and_drop_by_offset(drag,100,200)

action.perform()

