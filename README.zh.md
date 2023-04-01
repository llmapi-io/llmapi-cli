<p align="center">
  <img width="180" src="https://avatars.githubusercontent.com/u/127706964?s=200&v=4" alt="LLMApi Cli">
  <h1 align="center">LLMApi Cli</h1>
  <p align="center">用命令行和大语言模型聊天（如ChatGPT） </p>
</p>

# 介绍

llmapi_cli 是一个可以直接和chatgpt/gpt3以及更多大语言模型聊天的命令行工具，基于`llmapi-server`接口。
同时llmapi_cli也提供了Python module (`LLMClient`)便于开发集成。

> 更多信息请访问:  [llmapi.io](https://llmapi.io)

## 安装

```bash
# 使用pip库
python3 -m pip install llmapi_cli
```

```bash
# 本地安装
python3 setup.py develop
```

## 使用

```bash
# 初次使用该命令行时，需要指定相关参数，在成功连接server后会缓存

# 如果访问自己搭建的llmapi-server:
llmapi_cli --host='http://127.0.0.1:5050' --bot=mock

# 如果要直接使用api.llmapi.io（这个是默认的host）
llmapi_cli --bot=mock --apikey='your apikey on llmapi.io'
```

```bash
# 再次使用时可以直接运行（使用本地缓存参数）:
llmapi_cli

# 或者动态修改llm类型:
llmapi_cli --bot=gpt3

# 或者像第一次使用一样全部重新指定参数
```

### 截图
![image](imgs/llmapi_cli_demo.png)

# 目前支持的bot type

> 更多信息查看:[llmapi-server](https://github.com/llmapi-io/llmapi-server)

警告: 目前仅供测试使用

 - `chatgpt`: openai 官方的 ChatGPT,[了解更多](https://openai.com/blog/introducing-chatgpt-and-whisper-apis)
 - `gpt3`: openai 官方的 GPT-3
 - `welm`: 腾讯微信的语言模型,[了解更多](https://welm.weixin.qq.com/docs/introduction/)
 - `newbing`: 微软的新bing.com, `非官方接口`

