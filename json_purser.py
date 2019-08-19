#coding:utf-8
import json
import csv
import re

f = open('tweet.js', 'r')
jsonData = json.load(f)

write_fp = csv.writer(open("all_tweet.csv", "w"))

#column用文字列
write_fp.writerow(["text"])

#ノイズ削除用pattern
rt_pattern = 'RT+'

for json_val in jsonData:
    match_result = re.match(rt_pattern, json_val['full_text'])
    if not match_result:
        write_fp.writerow([json_val['full_text'].replace('"', '').replace('\n', '').replace(' ', '')])
