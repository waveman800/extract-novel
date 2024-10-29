#!/usr/bin/env python
# -*- coding: utf-8 -*-


novel_schema = dict(
    task_description = 'Adapted from the novel into script', # 小说改编成剧本
    attributes = [
        dict(
            name='role', 
            description='The character who is speaking',
            type='String'
            ), # 角色
        dict(
            name='dialogue',
            description='The dialogue spoken by the characters in the sentence',
            type='String'
            ), # 对话
    ],
    example = [
        dict(
            text = """观音菩萨让他赶快回到唐僧身边，悟空二话不说，告别观音菩萨去追赶唐僧了。

    见到唐僧，悟空把去龙王那儿吃饭的事情说了一遍，又问∶“师父，你也饿了吧！我去化些斋饭来。”唐僧摇摇头说∶“不用了，包袱里还有些干粮，你给师父拿来吧！”悟空打开包袱，发现观音菩萨给的衣帽十分漂亮，便向唐僧讨取。

    唐僧点头答应了。悟空高兴得抓耳挠腮，忙穿上了衣服，戴上了帽子。

    唐僧要试试紧箍咒灵不灵，就小声念了起来，悟空马上痛得满地打滚，拼命去扯那帽子，可帽子却像长在肉里一样，取也取不下来，扯也扯不烂。

    悟空发现头痛是因为师父在念咒，嘴里喊着“师父别念了！别念了！”

    暗地里取出金箍棒，想把唐僧一棒打死。唐僧见了，紧箍咒越念越快，悟空的头越来越疼，没有办法，只好跪地求饶∶“师父，是我错了，徒儿知道错了，不要再念咒了吧！”
            """,
            script = [
                {"role": "唐僧", "dialogue": "不用了，包袱里还有些干粮，你给师父拿来吧！"},
                {"role": "悟空", "dialogue": "师父，你也饿了吧！我去化些斋饭来。"},
                {"role": "悟空", "dialogue":"师父别念了！别念了！"},
                {"role": "悟空", "dialogue":"师父，是我错了，徒儿知道错了，不要再念咒了吧！"}
            ]
        )
    ]
)