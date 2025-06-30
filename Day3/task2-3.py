import requests
from lxml import etree
import os
# 爬取下载图片
def one():
    url = "http://pic.netbian.com/"
    headers = {"User-Agent": "Mozilla/5.0"}  # 防止被反爬
    try:
        rs = requests.get(url, headers=headers)
        rs.encoding = "gbk"
        html = etree.HTML(rs.text)
        listImg = html.xpath("//ul[@class='clearfix']/li/a/span/img/@src")
        print("图片路径列表：", listImg)

        # 创建保存目录
        save_dir = r"d:\Python_work\picture"
        os.makedirs(save_dir, exist_ok=True)

        for idx, img_path in enumerate(listImg):
            # 拼接完整图片 URL（如果 src 是相对路径）
            if not img_path.startswith("http"):
                img_url = url.rstrip("/") + img_path  # 去掉 url 末尾的 / 再拼接
            else:
                img_url = img_path

            try:
                # 下载图片
                img_data = requests.get(img_url, headers=headers).content
                # 保存图片
                img_name = f"image_{idx}.jpg"  # 自定义文件名
                save_path = os.path.join(save_dir, img_name)
                with open(save_path, "wb") as f:
                    f.write(img_data)
                print(f"下载完毕: {img_name}")
            except Exception as e:
                print(f"下载失败 {img_url}: {e}")

    except Exception as e:
        print(f"请求失败: {e}")

if __name__ == "__main__":
    one()