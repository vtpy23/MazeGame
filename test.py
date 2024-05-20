import json

# Mở file JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Tạo một từ điển mới
new_dict = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Thêm từ điển mới vào danh sách
data.append(new_dict)

# Ghi danh sách đã cập nhật vào file JSON
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)