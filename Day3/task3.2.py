import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 论文标题列表
papers = [
    "Coal and Gangue Recognition, Segmentation and Localization Method Based on Visual Information",
    "Small Target Detection Algorithm for UAV Aerial Images Based on YOLOv11",
    "AA-GM-YOLO: A Machining Chip Monitoring Method Based on Improved YOLO",
    "Lightweight Defect Detection Method for Transmission Lines",
    "Clothing Size Measurement Method Based on Keypoint Detection",
    "Research on Small Target Detection Algorithm Based on YOLO"
]

# 配置WebDriver
def init_driver():
    ua = UserAgent()
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={ua.random}")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    
    # 隐藏自动化特征
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': '''
            Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
            window.scrollTo = function() {};  // 禁用滚动检测
        '''
    })
    return driver

driver = init_driver()

def handle_captcha():
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
    try:
        driver.get("https://scholar.google.com")
        if "sorry" in driver.current_url.lower():
            handle_captcha()

        # 搜索论文
        try:
            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "q"))
            )
            search_box.clear()
            search_box.send_keys(title)
            search_box.send_keys(Keys.RETURN)
            time.sleep(random.uniform(3, 5))

            if "sorry" in driver.current_url.lower():
                handle_captcha()

            # 获取第一条结果的BibTeX
            try:
                # 直接定位到BibTeX链接（可能在结果页或详情页）
                bibtex_link = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "exportcitation")]'))
                )
                bibtex_link.click()
                time.sleep(2)

                # 切换到BibTeX窗口
                driver.switch_to.window(driver.window_handles[-1])
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                bibtex = soup.find("pre").get_text().strip()

                # 输出结果
                print("\n" + "="*80)
                print(f"论文标题: {title}")
                print("-"*80)
                print(bibtex)
                print("="*80)

                return bibtex

            except TimeoutException:
                # 如果直接链接未找到，尝试进入详情页
                driver.switch_to.window(driver.window_handles[0])
                first_result = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".gs_ri"))
                )
                first_result.click()
                time.sleep(3)

                # 在详情页中找引用链接
                driver.switch_to.window(driver.window_handles[-1])
                cite_link = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "引用"))
                )
                cite_link.click()
                time.sleep(2)

                # 在引用弹窗中找BibTeX
                bibtex_link = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "BibTeX"))
                )
                bibtex_link.click()
                time.sleep(2)

                # 提取BibTeX
                driver.switch_to.window(driver.window_handles[-1])
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                bibtex = soup.find("pre").get_text().strip()

                print("\n" + "="*80)
                print(f"论文标题: {title}")
                print("-"*80)
                print(bibtex)
                print("="*80)

                return bibtex

            finally:
                # 关闭所有额外窗口
                while len(driver.window_handles) > 1:
                    driver.switch_to.window(driver.window_handles[-1])
                    driver.close()
                driver.switch_to.window(driver.window_handles[0])

        except TimeoutException:
            print(f"[错误] 搜索超时: {title}")
            return None

    except Exception as e:
        print(f"[错误] 处理 {title} 时异常: {str(e)}")
        return None

def main():
    try:
        print("="*80)
        print("谷歌学术BibTeX引用爬取工具".center(68))
        print("="*80)
        
        for paper in papers:
            print(f"[处理中] 正在获取: {paper}")
            search_and_get_bibtex(paper)
            time.sleep(random.uniform(5, 10))
            
        print("\n" + "="*80)
        print("所有论文的BibTeX引用已输出完成".center(64))
        print("="*80)
        
    finally:
        driver.quit()

if __name__ == "__main__":
    main()