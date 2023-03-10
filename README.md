# python + pytest + allure测试框架集合

### 环境配置
    使用前在 cmd 或 commend 命令窗口中运行 requiment.txt 文件
    运行命令：
        pip install -r requiment.text

### main.py
    解释：这种方式方便一次性运行所创建的用例
    运行参数：
        -s: 输出用例中的调试信息
        -v: 输出用例更加详细的信息
        -q: 简化控制台的输出
        -k: 执行用例含 ”关键字“ 的用例
        -m: 执行指定的用例
    
    执行方式：
        0.运行指定参数
            pytest.main([’参数1‘,'参数2',...])
        1.运行当前目录和子目录下所有的用例
            pytest.main(['./']) 或 pytest.main()
        2.运行指定目录下用例
            pytest.main(['./test_cases', '参数'])
        3.运行指定模块下用例
            pytest.main(['./test_cases/test_one.py'])
        4.运行匹配包含关键字的用例(匹配目录名、模块名、类名、用例名)
            pytest.main(['-k', '关键字'])
        5.自己慢慢研究吧…

### 目录结构
    data - 数据存放目录
        1. yaml类型文件：可配置一些字段参数
        2. json类型文件
    untils - 工具集合文件(可进行读取操作) / 发送测试报告
    cases - 用例编写目录
    report - 报告目录
    pytest.ini - pytest的配置文件

### pytest.ini配置文件详细参数
    1. addopts配置[更改默认命令行选项,省去重复性命令工作]：
        -s：表示输出调试信息，用于显示测试函数中print()打印的信息
        -v：未加前只打印模块名，加v后打印类名、模块名、方法名，显示更详细的信息
        -q：表示只显示整体测试结果
        -vs：这两个参数可以一起使用
        -n：支持多线程或者分布式运行测试用例（前提需安装：pytest-xdist插件）
        –html：生成html的测试报告（前提需安装：pytest-html插件） 如：pytest -vs --html ./reports/result.html
        --capture=sys: 输出异常行为，如：-vs --html ./reports/result.html --capture=sys --self-contained-html
    2. testpaths[指定用例目录配置]：
        例：testpaths = ./test_cases
    3. markers[注册mark标记, 用例的装饰器]：
        例：markers = 
                p0: 优先级为P0
                dev: 设置为开发环境
                test: 设置为测试环境
        使用方法：
            在用例中加入注释的方式使用如下：
                @pytest.mark.test
                test_cases: