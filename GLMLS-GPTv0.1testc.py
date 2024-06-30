import requests
from colorama import Fore, Style
from PIL import ImageTk, Image

def ask_question(question):
    try:
        response = requests.post('http://ai.mxhmcp.link/ask', json={'input': question}, timeout=5)
        if response.status_code == 200:
            return response.json()['answer']
        else:
            return f"连接失败，状态码：{response.status_code}"
    except  as e:
        return f"连接失败，错误信息：{str(e)}"

if __name__ == '__main__':
    root = tk.Tk()
    root.title("金龙华光工作室(GLMLS)-AI")

    # 设置窗口初始大小
    root.geometry("300x200")

    label_title = ttk.Label(root, text="GLMLS-GPT v0.1test(2024/6/28-15:10)", font=("Arial", 16))
    label_title.grid(row=0, column=0, columnspan=2)
    print("Build in (2024/6/28-15:10) 所有权归金龙华光工作室(GLMLS)所有  官网:www.mxhmcp.link ")
    label_question = ttk.Label(root, text="请输入您的问题：")
    button_send = ttk.Button(root, text="发送")
    button_send.grid(row=2, column=1)
    
    text_answer = tk.Text(root, wrap=tk.WORD, width=40, height=10)
    text_answer.grid(row=3, column=0, columnspan=2)

    # 设置行和列的权重，使它们在窗口大小改变时自动调整
    for i in range(3):
        wconfigure(i, weight=1)
    for j in range(2):
        lumnconfigure(j, weight=1)

    root.mainloop()
