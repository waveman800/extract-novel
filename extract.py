from openai import OpenAI
import json
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

SYSTEM_PROMPT = """
你是一个专业的对话提取助手。你的任务是从输入的文本中提取人物对话，仅提取直接引语部分。

规则：
1. 只提取人物说的话（直接引语），不提取描述性文本
2. 确保每段对话都有明确的说话人
3. 如果一段文本中没有对话，则返回空数组
4. 对话必须是完整的，不要提取半句话
5. 不要提取旁白或描述性文字
6. 如果对话被分割或不完整，需要将其完整提取

请按照以下格式提取信息：
{TypeScript}

请以 JSON 格式输出提取的信息。

示例输入：
{Input}

示例输出：
{Output}

注意：
- 只输出符合模式的 JSON 数据
- 不要添加任何解释或额外信息
- 确保输出的每条记录都包含完整的对话
- 如果找不到有效的对话，返回空数组 []
"""

TYPE_SCRIPT = """
```TypeScript
    script: Array<Dict( // {task_description}
    {attributes}
    )>
```
"""

def get_typescript(schema, type_script_str):
    script = schema['attributes']
    script_str = ',\n    '.join([f"{s['name']}: {s['type']} // {s['description']} " for s in script])
    type_script_str = type_script_str.format(task_description=schema['task_description'], attributes=script_str)
    return type_script_str

def system_prompt(schema):
    return SYSTEM_PROMPT.format(TypeScript=get_typescript(schema, TYPE_SCRIPT), Input=schema['example'][0]['text'], Output=json.dumps(schema['example'][0]['script'], indent=4, ensure_ascii=False))

