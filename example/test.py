# 三种主要的 I/O类型分别为: 文本 I/O, 二进制 I/O 和 原始 I/O。这些是泛型类型，有很多种后端存储可以用在他们上面。
import io
import time
from datetime import datetime


def text_io():
    # TextIO
    f1 = open("myfile.txt", "r", encoding="utf-8")

    f2 = io.StringIO("some initial text data")


def bytes_io():
    # BufferedIOBase
    f1 = open("myfile.jpg", "rb")
    f2 = io.BytesIO(b"some initial binary data: \x00\x01")

    # flush()  这里的缓冲区，是os的读写缓冲区。
    # 刷新 流的写入缓冲区（如果适用）。这对只读和非阻塞流不起作用。

    # truncate(size=None, /)¶
    # 将流的大小调整为给定的 size 个字节（如果未指定 size 则调整至当前位置）。 
    # 当前的流位置不变。 这个调整操作可扩展或减小当前文件大小。 
    # 在扩展的情况下，新文件区域的内容取决于具体平台（在大多数系统上，额外的字节会填充为零）。 返回新的文件大小。


def raw_io():
    # 原始 I/O（也称为 非缓冲 I/O）通常用作二进制和文本流的低级构建块。用户代码直接操作原始流的用法非常罕见。不过，可以通过在禁用缓冲的情况下以二进制模式打开文件来创建原始流：
    f = open("myfile.jpg", "rb", buffering=0)


def test_buffer_enter():
    text = "this is test"
    f = open("./test_buffer.txt", "w", buffering=1)
    try:
        while True:
            t = datetime.now().strftime("%H:%M:%S")
            f.write(f"{text}--{t}--\n")
            time.sleep(1)
    finally:
        f.close()


def test_buffer_2bytes():
    text = "this is test 2bytes buffer" * 50
    f = open("./test_buffer.txt", "w", buffering=2)
    try:
        while True:
            t = datetime.now().strftime("%H:%M:%S")
            f.write(f"{text}--{t}--\n")
            time.sleep(0.1)
    finally:
        f.close()


def test_buffer_default():
    text = "this is test default buffer"
    f = open("./test_default_buffer.txt", "w")
    try:
        while True:
            t = datetime.now().strftime("%H:%M:%S")
            f.write(f"{text}--{t}--\n")
            time.sleep(0.1)
    finally:
        f.close()


if __name__ == "__main__":
    # test_buffer_enter()
    # test_buffer_2bytes()
    test_buffer_default()