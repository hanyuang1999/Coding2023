import json
#label-studio == 1.7.1
def transform(jsonA):
    # 解析jsonA文件的内容
    text = jsonA['text']

    # 初始化jsonB的内容
    text_B = list(text)
    labels_B = ['O'] * len(text)

    if 'label' in jsonA:
        labels_A = jsonA['label']
        for label in labels_A:
            start = label['start']
            end = label['end']
            entity_type = label['labels'][0]

            # 根据起始坐标和结束坐标标记实体
            labels_B[start] = "B-" + entity_type
            for i in range(start + 1, end):
                labels_B[i] = "I-" + entity_type

    # 构造jsonB
    jsonB = {
        'id': jsonA['id'],
        'text': text_B,
        'labels': labels_B
    }

    return jsonB


# 读取jsonA.json文件
with open('./jsonA.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 处理每一段文字并保存结果
result = []
for item in data:
    print('1')
    jsonB = transform(item)
    result.append(jsonB)

# 将结果写入jsonB.json文件
with open('./jsonB.txt', 'w', encoding='utf-8') as f:
    for item in result:
        line = json.dumps(item, ensure_ascii=False)
        f.write(line + '\n')
