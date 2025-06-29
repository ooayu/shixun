import os
import re

def natural_sort_key(s):
    """自然排序键函数，使 '1.jpg', '2.jpg', '10.jpg' 正确排序"""
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def rename_images_from_text(image_folder, text_file, output_extension=None):
    """
    根据文本文件内容批量修改图片文件名，顺序与 Windows 资源管理器一致
    :param image_folder: 图片文件夹路径
    :param text_file: 文本文件路径（每行一个新文件名，不带扩展名）
    :param output_extension: 输出扩展名（如 ".jpg"），默认保持原扩展名
    """
    try:
        # 读取文本文件（跳过空行）
        with open(text_file, "r", encoding="utf-8") as f:
            new_names = [line.strip() for line in f if line.strip()]
        
        # 获取图片文件列表（按 Windows 资源管理器顺序排序）
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]
        image_files.sort(key=natural_sort_key)  # 自然排序（模拟 Windows 资源管理器）

        # 检查数量是否匹配（如果数量不匹配，直接报错退出）
        if len(new_names) != len(image_files):
            raise ValueError(f"错误：文本文件有 {len(new_names)} 个名称，但图片有 {len(image_files)} 个！")

        # 批量重命名
        for old_name, new_name in zip(image_files, new_names):
            old_path = os.path.join(image_folder, old_name)
            
            # 确定输出扩展名（默认保持原扩展名）
            if output_extension is None:
                ext = os.path.splitext(old_name)[1].lower()
            else:
                ext = output_extension if output_extension.startswith(".") else f".{output_extension}"
            
            new_path = os.path.join(image_folder, f"{new_name}{ext}")

            # 重命名并打印结果
            os.rename(old_path, new_path)
            print(f"重命名: {old_name} → {new_name}{ext}")

        print("✅ 所有文件重命名完成！")

    except FileNotFoundError:
        print("错误：文件不存在！请检查路径是否正确。")
    except Exception as e:
        print(f"错误: {str(e)}")

# ===== 使用示例 =====
if __name__ == "__main__":
    IMAGE_FOLDER = r"D:\Python_work\作业\新建文件夹"  # 图片文件夹路径
    TEXT_FILE = r"D:\Python_work\作业\新建文本文档.txt"    # 文本文件路径（每行一个新名称）
    
    rename_images_from_text(
        image_folder=IMAGE_FOLDER,
        text_file=TEXT_FILE,
        output_extension=".png"  # 可选：强制输出为 .jpg（默认保持原扩展名）
    )