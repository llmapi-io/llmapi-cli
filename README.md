# 介绍

llmapi_cli 是一个可以直接和chatgpt/gpt3以及更多大语言模型聊天的命令行工具，基于llmapi.io接口
同时llmapi_cli也提供了Python module (LLMClient)
更多信息请访问: https://llmapi.io

## 安装(Install)

```bash
# 使用pip库
python3 -m pip install llmapi_cli
```

```bash
# 本地开发使用
python3 setup.py develop
```

## 使用(Usage)

```bash
# 初次使用时需要配置apikey和bot类型,成功后将缓存
llmapi_cli --apikey="your key in llmapi.io" --bot=chatgpt
```

```bash
# 如果你有自己的bot key(即llm官方的key，如openai's api key)
# 可以配置使用，聊天次数将不受限制
llmapi_cli --apikey="your key in llmapi.io" --bot=chatgpt --bot_key="your key in openai(or others)"
```

```bash
# 后续使用可以直接执行
llmapi_cli
# 或者切换bot
llmapi_cli --bot=gpt3
```

### screenshot
![image](imgs/llmapi_cli_demo.png)

# 当前支持的LLM
 - `chatgpt`:openai的官方ChatGPT api
 - `gpt3`:openai的官方GPT-3 api

