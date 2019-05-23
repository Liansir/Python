[TOC]

# Log

- logging

- logging模块提供模块级别的函数记录日志

- 包括四大组件 

- 日志相关概念

  - 日志级别(level)
    - 不同的用户关注不同的程序信息
      - DEBUG 
      - INFO 
      - NOTICE 
      - WARNING
      - ERROR 
      -  CRITICAL 
      - ALERT
      - EMERGENCY

  - 日志信息
    - time
    - 地点
    - level
    - 内容 



## logging模块级别日志

- 使用以下几个函数 

- Logging.basicConfig(**kwargs)   对root logger进行一次性配置
  - 只在第一次调用时起作用
  - 不配置logger则使用默认值 
    - 输出： sys.stderr 
    - 级别：WARNING
    - 格式：level: log_name:content

## logging模块的处理流程

- 四大组件

  - 日志器(Logger): 产生日志的一个接口
  - 处理器(Handler)：把产生的日志发送到相关的目的地
  - 过滤器(Filter): 更精细的控制那些日志输出 
  - 格式器(Formatter): 对输出进行格式化

- Logger

  - 产生一个日志
  - 操作
    - Logger.setLevel()
    - Logger.addHandler()
    - Logger.addFilter()
    - Logger.debug: 同理，info, error等
    - Logger.exception():
    - Logger.log()
  - 如何得到一个logger对象
    - 实例化
    - Logging.getLogger()

- Handler

  - 把log发送到指定位置
  - 方法
    - setLevel 
    - setFormat 
    - addFilter, removeFilter

  - 不需要直接使用，Handler是基类

- Format类

  - 直接实例化
  - 可以继承Format添加特殊内容
  - 三个参数
    - fmt
    - datefmt 
    - style

- Filter类

  - 可以被Handler和Logger类使用
  - 控制传递过来的信息的具体内容

[logging](https://www.cnblogs.com/yyds/p/6901864.html)









