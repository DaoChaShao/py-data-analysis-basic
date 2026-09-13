import hashlib
import random

# 创建md5对象
md5_object = hashlib.md5()

# 传入要加密的字符串
input_password = 'admin'
md5_object.update(input_password.encode('utf-8'))

# 获取加密后的字符串
encrypted_password = md5_object.hexdigest()

print(encrypted_password)  # 输出：21232f297a57a5a743894a0e4a801fc3


# 由于可能出现的撞库问题，建议加密后的密码保存到数据库中，而不是直接保存明文密码。
# 另外，md5加密算法已经不安全，可使用“加盐”方法，如下：


def generate_random_numbers():
    """
    生成指定长度的随机数字
    :param : 1个数字长度
    :return: 随机数字符串
    """
    return random.randint(0, 9)


def generate_random_upper_letters():
    """
    生成指定长度的随机大写字母
    :param : 1个字母长度
    :return: 随机字母字符串
    """
    return chr(random.randint(65, 90))


def generate_random_lower_letters():
    """
    生成指定长度的随机小写字母
    :param : 1个字母长度
    :return: 随机字母字符串
    """
    return chr(random.randint(97, 122))


def generate_random_codes():
    '''
    生成指定长度的随机字符
    :param : 1个字符长度
    :return: 随机字符字符串
    '''
    code_list = []
    for i in range(16):
        random_category = random.randint(1, 3)
        if random_category == 1:
            code_list.append(str(generate_random_numbers()))
        elif random_category == 2:
            code_list.append(generate_random_upper_letters())
        elif random_category == 3:
            code_list.append(generate_random_lower_letters())
    # 随机打乱
    random.shuffle(code_list)
    code_outcome = ''.join(code_list)
    return code_outcome


print(f'随机生成的16位字符：{generate_random_codes()}')

# “加盐”后的md5加密算法如下：
# 创建随机“盐”
md5_salt = str(generate_random_codes())
md5_object_with_salt = hashlib.md5(b'md5_salt')  # 真·动态“加盐”

# 传入要加密的字符串
md5_object.update(md5_salt.encode('utf-8'))
# 获取加密后的字符串
encrypted_password_with_salt = md5_object_with_salt.hexdigest()
print(encrypted_password_with_salt)


def encrypt_keyinfo(salt, input_content):
    """
    加密密码
    :param salt: 加密作料
    :param input_content: 要加密的字符串
    :return: 加密后的字符串
    """
    encrypted_md5_object = hashlib.md5(salt)  # 创建加密对象
    encrypted_md5_object.update(input_content.encode('utf-8'))  # 传入要加密的字符串
    encrypted_content = encrypted_md5_object.hexdigest()  # 获取加密后的字符串
    return encrypted_content  # 返回加密后的字符串


def dump_data(dump_username, dump_password, dump_file_path):
    """
    重编码数据
    :return: 重编码后的字符串
    """
    with open(dump_file_path, 'w', encoding='utf-8') as hash_file:
        hash_file.write(dump_username + '\n' + dump_password + '\n')


def load_data(load_file_path):
    """
    加载数据
    :return: 加载后的字符串
    """
    with open(load_file_path, 'r', encoding='utf-8') as hash_file:
        hash_data = hash_file.readlines()
        hash_username = hash_data[0].strip()  # 这里可以直接读取
        hash_password = hash_data[1].strip()  # 注意：这里的密码是加密后的字符串，需要解密后才能使用
        return [hash_username, hash_password]


if __name__ == '__main__':
    # 测试：用户注册信息存储
    # 1.注册阶段
    username = 'admin'
    password = '123456'

    file_path = 'data/hashlib.txt'

    # 加密密码
    # 以不同的“用户名”做盐，为用户实现“相对的”动态加密
    encrypted_password = encrypt_keyinfo(username.encode('utf-8'), password)

    # 存储用户数据
    dump_data(username, encrypted_password, file_path)

    # 2.登录阶段
    # 读取用户数据
    [load_username, load_password] = load_data(file_path)
    print(f'用户名：{load_username}, 密码：{load_password}')

    # 解密密码
    # 重新将密码进行加密，和存入的密码进行比较
    encrypted_password_for_login = encrypt_keyinfo(username.encode('utf-8'), password)
    print(f'原密码：{password}, 登录后再加密后的密码：{encrypted_password_for_login}')
    # 再加密的密码 和 读取出来的密码 进行比较
    if encrypted_password_for_login != load_password:
        print('密码错误，登录失败')
    else:
        print('密码一致，登录成功')
