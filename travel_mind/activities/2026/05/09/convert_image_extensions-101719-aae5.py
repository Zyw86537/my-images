import os
import argparse
from pathlib import Path

def convert_image_extensions(directory, target_extension='.jpg'):
    """
    将指定目录下所有图片文件的后缀名改为指定的扩展名
    
    Args:
        directory (str): 要处理的目录路径
        target_extension (str): 目标扩展名，默认为.jpg
    """
    # 支持的图片格式
    image_extensions = {'.png', '.jpeg', '.gif', '.bmp', '.tiff', '.webp', '.PNG', '.JPEG', '.GIF', '.BMP', '.TIFF', '.WEBP'}
    
    # 确保目标扩展名以点开头
    if not target_extension.startswith('.'):
        target_extension = '.' + target_extension
    
    converted_count = 0
    
    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # 只处理文件，跳过目录
        if os.path.isfile(file_path):
            # 获取文件扩展名
            _, extension = os.path.splitext(filename)
            
            # 检查是否为支持的图片格式
            if extension in image_extensions:
                # 构造新的文件名
                base_name = os.path.splitext(filename)[0]
                new_filename = base_name + target_extension
                new_file_path = os.path.join(directory, new_filename)
                
                # 重命名文件
                try:
                    os.rename(file_path, new_file_path)
                    print(f"已转换: {filename} -> {new_filename}")
                    converted_count += 1
                except Exception as e:
                    print(f"转换失败 {filename}: {str(e)}")
    
    print(f"\n总共转换了 {converted_count} 个文件")

def main():
    parser = argparse.ArgumentParser(description='将图片文件后缀名改为指定格式')
    parser.add_argument('directory', nargs='?', default='.', help='要处理的目录路径 (默认为当前目录)')
    parser.add_argument('-e', '--extension', default='.jpg', help='目标扩展名 (默认为 .jpg)')
    
    args = parser.parse_args()
    
    # 检查目录是否存在
    if not os.path.exists(args.directory):
        print(f"错误: 目录 '{args.directory}' 不存在")
        return
    
    if not os.path.isdir(args.directory):
        print(f"错误: '{args.directory}' 不是一个目录")
        return
    
    print(f"正在处理目录: {os.path.abspath(args.directory)}")
    print(f"目标扩展名: {args.extension}")
    print("-" * 40)
    
    convert_image_extensions(args.directory, args.extension)

if __name__ == '__main__':
    main()