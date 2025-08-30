from os import system
from webbrowser import open

def title():
    '''标题'''
    print("┌──╮  ┌──  ┌──  ┌──╮  ╭──┐  ┌──  ┌──  ┬ ╭─              ")
    print("│  │  ├──  ├──  ├──╯  ╰──╮  ├──  ├──  ├─╯               ")
    print("└──╯  └──  └──  ┴     └──╯  └──  └──  ┴ ╰─   本地部署工具")


def downloed_ollamam():    
    '''进入powershell并下载ollama'''
    print("开始下载ollama")
    system('powershell.exe -Command "Invoke-WebRequest -Uri https://ollama.com/download/OllamaSetup.exe -OutFile C:/fcc/Downloads/OllamaSetup.exe"')
    print("下载完成")

def openo_llamam():
    '''运行ollama下载程序'''
    print("请完成ollama下载")
    system("C:/fcc/Downloads/OllamaSetup.exe")
    print("ollama下载完成")

def downloed_deepseek():
    '''下载deepseek(目前仅支持1.5b版本)'''
    print("开始下载deepseek")
    system("ollama run deepseek-r1:1.5b")
    print("下载完成")

def web():
    '''下载web拓展'''
    print("请完成下载Microsoft拓展")
    open("https://microsoftedge.microsoft.com/addons/detail/page-assist-a-web-ui-fo/ogkogooadflifpmmidmhjedogicnhooa?hl=zh-CN")
    print("Microsoft拓展下载完成")

def start_use():
    '''完成配置'''
    print("请点击 Select a model 选择模型")
    open("extension://ogkogooadflifpmmidmhjedogicnhooa/options.html")
    print("配置完成")
    print("deepseek部署完成")

title()
downloed_ollamam()
openo_llamam()
downloed_deepseek()
web()
start_use()