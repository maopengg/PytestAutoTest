import streamlit as st
import sqlite3

# 连接到 SQLite 数据库
conn = sqlite3.connect('data.db')
c = conn.cursor()

# # 创建表
# c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
# conn.commit()

# 增加数据
def add_data(name, age):
    c.execute('''INSERT INTO users (name, age) VALUES (?, ?)''', (name, age))
    conn.commit()

# 删除数据
def delete_data(user_id):
    c.execute('''DELETE FROM users WHERE id = ?''', (user_id,))
    conn.commit()

# 查询数据
def get_data():
    c.execute('''SELECT * FROM users''')
    return c.fetchall()

# Streamlit 应用
st.title('SQLite 数据库操作示例')

# 添加数据
name = st.text_input('请输入姓名')
age = st.number_input('请输入年龄', min_value=0)
if st.button('添加数据'):
    add_data(name, age)

# 删除数据
delete_id = st.number_input('请输入要删除的用户 ID', min_value=1)
if st.button('删除数据'):
    delete_data(delete_id)

# 展示数据
st.write('当前数据库中的数据：')
data = get_data()
for row in data:
    print(row)
    st.write(row)

# 关闭数据库连接
conn.close()
