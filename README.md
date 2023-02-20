# python + pytest 测试框架

### main.py
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
    conifg - 配置文件目录
    test_cases(功能) / test_requests(接口) - 用例编写目录
    pytest.ini - pytest的配置文件