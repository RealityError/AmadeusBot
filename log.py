# -*- coding: utf-8 -*-
# @Time : 2023/1/13
# @Author : 白猫猫
# @File : log.py
# @Software: Vscode|虚拟环境|3.10.6|64-bit
"""该模块定义了通用的的日志记录Logger。



"""


from config import config
import loguru
import loguru
import sys

logger = loguru.logger
"""日志记录器对象。

默认信息:

- 格式: `%(asctime)s %(levelname)s %(name)s: %(message)s`
- 等级: `INFO` ，根据 `config.log_level` 配置改变
- 输出: 输出至log文件夹下

用法:
python
    ```
    from log import logger
    ```
"""

default_format: str = (
    "<g>{time:MM-DD HH:mm:ss}</g> "
    "[<lvl>{level}</lvl>] "
    "<c><u>{name}</u></c> | "
    "{message}"
)
"""默认日志格式"""


logger.add(
    r'./log/data_{time:YYYY_DD_HH}.log', 
    rotation='12 hour',
    level=config["log_level"],
    enqueue=True,
    format=default_format,
    )

