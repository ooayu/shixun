import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup

# 论文标题列表
papers = [
    "Coal and Gangue Recognition, Segmentation and Localization Method Based on Visual Information",
    "Small Target Detection Algorithm for UAV Aerial Images Based on YOLOv11",  # 修正为YOLOv11
    "AA-GM-YOLO: A Machining Chip Monitoring Method Based on Improved YOLO",
    "Lightweight Defect Detection Method for Transmission Lines",
    "Clothing Size Measurement Method Based on Keypoint Detection",
    "Research on Small Target Detection Algorithm Based on YOLO"
]

from selenium.webdriver.chrome.options import Options
# 配置Selenium WebDriver

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=options)
# 禁用webdriver标志（JavaScript检测）
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
})

def handle_captcha():
    """处理可能出现的验证码"""
    print("\n[警告] 检测到验证码，请在300秒内手动解决...")
    try:
        WebDriverWait(driver, 300).until(
            lambda d: "scholar.google.com" in d.current_url and "sorry" not in d.current_url.lower()
        )
        print("[成功] 验证码已解决，继续执行...")
    except TimeoutException:
        print("[错误] 等待验证码解决超时")
        driver.quit()
        exit(1)

def search_and_get_bibtex(title):
    """搜索论文并获取BibTex引用"""
    try:
        # 访问谷歌学术
        driver.get("https://scholar.google.com")
        
        # 检查验证码
        if "sorry" in driver.current_url.lower():
            handle_captcha()
        
        # 搜索论文
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.clear()
        search_box.send_keys(title)
        search_box.send_keys(Keys.RETURN)
        time.sleep(random.uniform(2, 4))
        
        # 再次检查验证码
        if "sorry" in driver.current_url.lower():
            handle_captcha()
        
        # 获取第一条结果
        try:
            first_result = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".gs_ri"))
            )
            first_result.click()
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(2)
            
            # 点击引用链接
            try:
                
                
                driver.get("https://scholar.google.com")
                time.sleep(random.uniform(2, 5))
 
                # 搜索论文
                search_box = driver.find_element(By.NAME, "q")
                search_box.send_keys(title)
                search_box.send_keys(Keys.RETURN)
                time.sleep(random.uniform(3, 7))
                # 处理验证码（手动）
                if "sorry" in driver.current_url.lower():
                    input("[警告] 检测到验证码，请手动解决后按回车继续...")

                # 获取BibTex
                try:
                    bibtex_link = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "BibTeX"))
                    )
                    bibtex_link.click()
                    time.sleep(2)
                    
                    # 切换到BibTex窗口并提取内容
                    driver.switch_to.window(driver.window_handles[-1])
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    bibtex = soup.find("pre").get_text().strip()
                    
                    # 格式化输出
                    print("\n" + "="*80)
                    print(f"论文标题: {title}")
                    print("-"*80)
                    print(bibtex)
                    print("="*80 + "\n")
                    
                    return bibtex
                    
                except TimeoutException:
                    print(f"[错误] 无法找到 {title} 的BibTeX链接")
                    return None
                    
            except TimeoutException:
                print(f"[错误] 无法找到 {title} 的引用链接")
                return None
                
        except TimeoutException:
            print(f"[错误] 未找到 {title} 的搜索结果")
            return None
            
        finally:
            # 关闭额外窗口
            if len(driver.window_handles) > 1:
                for handle in driver.window_handles[1:]:
                    driver.switch_to.window(handle)
                    driver.close()
                driver.switch_to.window(driver.window_handles[0])
    
    except Exception as e:
        print(f"[错误] 处理 {title} 时发生异常: {str(e)}")
        return None

def main():
    try:
        print("="*80)
        print("谷歌学术BibTeX引用爬取工具".center(68))
        print("="*80)
        
        for paper in papers:
            print(f"[处理中] 正在获取: {paper}")
            search_and_get_bibtex(paper)
            time.sleep(random.uniform(3, 7))  # 增加随机延迟
            
        print("\n" + "="*80)
        print("所有论文的BibTeX引用已输出完成".center(64))
        print("="*80)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()