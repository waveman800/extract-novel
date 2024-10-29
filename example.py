from extract import system_prompt
from schema import novel_schema
from LLM import DeepseekChat
from utils import ReadFiles
from tqdm import tqdm
import json
import time

file_path = './data/西游记白话文.txt'
docs = ReadFiles(file_path).get_content(max_token_len=16384, cover_content=0)

sys_prompt = system_prompt(novel_schema)
model = DeepseekChat()

file_name = file_path.split('/')[-1].split('.')[0]
timestamp = int(time.time())
output_file = f'{file_name}_{timestamp}.jsonl'

for i in tqdm(range(len(docs))):
    doc = docs[i]
    try:
        response = model.chat(sys_prompt, doc)
        
        if not response:
            tqdm.write(f'第 {i} 条文档没有返回任何内容')
            continue
        
        tqdm.write(f'第 {i} 条文档的响应内容: {response}')
        
        response = json.loads(response)
        for item in response:
            with open(output_file, 'a', encoding='utf-8') as f:
                json.dump(item, f, ensure_ascii=False)
                f.write('\n')
                tqdm.write(f'已提取内容: {item}')
    except json.JSONDecodeError as e:
        tqdm.write(f'处理第 {i} 条文档时发生 JSON 解码错误: {e}')
        tqdm.write(f'响应内容: {response}')
    except Exception as e:
        tqdm.write(f'处理第 {i} 条文档时发生错误: {e}')
