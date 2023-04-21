# AiWriter with ChatGPT

## AiWriter Plugin Architecture

* use `prompt` to record `AiWriter` pair developing logs
* use `resources` to save all templates and static files
* use `crawler` to spider and generate information `event`
* use `parser` to transform `event` to another one
* use `sender` to send `event` to multiple platform
* user `plan` to schedule crawler, parser, sender for business flow

## Features
[*] US1 - add sender-wechat open platform
[*] US2 - add crawler for https://gpt3demo.com/
[*] US3 - add parser-markdown 
[*] US4 - add parser-google translate 
[*] US5 - add plan-gpt3demo_to_wechat
[*] US6 - add main python to invoke relate plan

## Run project locally

```shell
pip install -r requirements.txt

export wechat_appid="replace me"
export wechat_appid="replace me"

python main -plan gpt3demo_to_wechat

```