import requests

url = "https://imdb-video.media-imdb.com/vi564184857/1434659607842-pgv4ql-1687965075039.mp4?Expires=1688112095&Signature=Tl90KC1v1gur07S7SYrdxKyf1Da1z5WXlBcKhFOfPhtcb82NRfnPLzm4RN2jA4-Xbpf69heMJBXxzsSHdARKpqnxe1YXl8X3cExQETlpgTlDRReRLj5-RSjkVtitcvdXmohVNYhAz7tECL4hwIuNPDoTyBASXwmxws79uVC31WH1aKpN4~QFrGbyDuXOq16U-C5aRxg~ukRt42mQB1MaKIXWPDnbXp4alikr69MAzrnzesX5INb4Ga5sqRMcSf8s-wpL8lv3z9zz0ucIhfMvd0KnwXZXHYTwRa2XbQk-HQbhQS0loklCx19nbHYC0ka-W07id0G7St30NxDe~HbYCw__&Key-Pair-Id=APKAIFLZBVQZ24NQH3KA"
file_path = "video.mp4"  # 保存视频的文件路径

response = requests.get(url, stream=True)

if response.status_code == 200:
    with open(file_path, 'wb') as file:
        # 分块下载
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)
    print("视频下载完成！")
else:
    print("视频下载失败。")
