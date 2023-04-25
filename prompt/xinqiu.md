## write a sender to login in xin qiu and send updates

```text

i have one user story need your help.

User Story:  `US7`
description: i want build a python class `XinQiu.py`, by invoking method `send` with parameter `event`
Acceptance Criteria:
    1. given event.content = null, should return error and log errors
    2. given event.content = `test`, should send successfully


implementation strategy:

1. open web page `https://wx.zsxq.com/dweb2/index/group/48884842581428` 
2. find a UI component `<p>` by class `.ql-editor p`
3. fill `event.content` under `<p>` in second step
4. find submit button `submit` by class `submit-btn`
5. click `submit` button
6. check webpage if information inserted 

could you help me analysis the `US7` and use python implement it

```

![img.png](imgs/xinqiu/1.png)
![img.png](imgs/xinqiu/2.png)