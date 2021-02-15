# 原神圣遗物面板自动识别 flask 版本(用于部署于云函数)

基于：https://github.com/kyloris0660/GenshinArtifactRecorder
改造而来

返回格式:json
请求方式:POST
请求参数:
"image":"iVBORw0KGgoAAAANSUhEUgAAAjoA......"(base64 的图片)
返回参数:
case1:false,500
case2:
"{'name': '乐团的晨光', 'set_pieces': '生之花', 'main_stat': '生命值', 'main_stat_value': '3,155', 'star': 5, 'lv': 12, 'vice_stat0': '元素精通', 'vice_stat0_value': '40', 'vice_stat1': '暴击率', 'vice_stat1_value': '2.7%', 'vice_stat2': '防御力', 'vice_stat2_value': '42', 'vice_stat3': '生命值', 'vice_stat3_value': '4.7%', 'set_name': '流浪大地的乐团'}",200
