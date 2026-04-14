# Python 学习笔记仓库

这是一个用于记录个人 Python 学习与练习的仓库，包含多个子项目与练手示例（例如一个简单的 Flask 示例与手写数字识别笔记本）。

## 主要内容概览

- `flask trial/`：非常简单的 Flask 演示（包含 `app.py` 和模板），用于练习 Web 表单与模板渲染。
- `handwriting recognition with MNIST/`：基于 MNIST 的手写数字识别笔记本（Jupyter Notebook），用于学习神经网络基础与实验记录。
- `Tutorial for beginners 100  cases of Python Algorithm/`：收集的 Python 算法练习与示例（很多小脚本，按主题组织）。

（仓库中还有更多小练习目录，按名称即可查看对应示例）

## Flask trial

建议使用虚拟环境并安装 Flask：

```powershell
# 在仓库根目录下创建并激活虚拟环境
python -m venv venv
.\venv\Scripts\Activate.ps1

# 安装 Flask
pip install flask

# 使用 flask CLI 运行示例
# 可通过 --app 参数直接指定文件路径
flask --app "flask trial/app.py" run

# 或者设置环境变量：
$Env:FLASK_APP = "flask trial/app.py"
flask run
```


## MNIST

如果你要查看或运行，进入
 `handwriting recognition with MNIST/handwriting recognition.ipynb`：

```powershell
pip install notebook jupyterlab
jupyter notebook "handwriting recognition with MNIST/handwriting recognition.ipynb"
```

或者在 JupyterLab 中打开该文件以获得更好的交互体验。

## 贡献与使用

- 这个仓库主要用于个人学习。如果你想复用或参考其中内容，欢迎按需复制文件并注明来源。


---

