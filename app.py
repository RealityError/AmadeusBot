# -*- coding: utf-8 -*-
# @Time : 2023/1/18
# @Author : 白猫猫
# @File : app.py
# @Software: Vscode|虚拟环境|3.10.6|64-bit
"""该模块提供异步web服务。
"""
from fastapi import FastAPI,Request,Response
import uvicorn
from log import logger
from config import config
from pydantic import BaseModel

app = FastAPI()




@app.on_event("startup")
def startup_event():

    logger.info("WEB服务启动")

@app.on_event("shutdown")
def shutdown_event():
    logger.info("WEB服务关闭")
    
    
#信息入口    
@app.post("/")
async def info(request:dict):
    logger.debug(str(request))
    return 0

if __name__ == "__main__":
    uvicorn.run(
        "app:app", 
        host=config["web"]["host"], 
        port=config["web"]["port"]
        )
