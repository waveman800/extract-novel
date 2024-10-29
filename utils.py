#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   utils.py
@Time    :   2024/06/16 08:05:08
@Author  :   不要葱姜蒜
@Version :   1.0
@Desc    :   None
'''

import os
from typing import Dict, List, Optional, Tuple, Union

from tqdm import tqdm
import tiktoken
import re

enc = tiktoken.get_encoding("cl100k_base")

class ReadFiles:
    """
    class to read files
    """

    def __init__(self, file_path):
        self.file_path = file_path

    def get_content(self, max_token_len=None, cover_content=0):
        """读取文件内容并分割，不做长度限制"""
        with open(self.file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 按段落分割内容
        paragraphs = content.split('\n\n')
        
        # 移除空段落
        paragraphs = [p.strip() for p in paragraphs if p.strip()]

        # 直接返回所有段落，不做长度检查
        return paragraphs