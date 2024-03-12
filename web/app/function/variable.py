# オリジナル画像の保存先
imgLocation_origin = 'images/origin/'
# リサイズ画像の保存先
imgLocation_resized = 'images/downsize/'
# アプリでサポートされている拡張子リスト
supportedExtentionList = ['jpg', 'jpeg', 'png']
# 暗号化された画像の保存先
imgLocation_encrypted = 'images/encrypted/'

# def xor_cypher(input_string, key):
#     # 文字列をビット列に変換
#     input_bits = ''.join(format(ord(i), '08b') for i in input_string)
#     key_bits = ''.join(format(ord(i), '08b') for i in key)

#     # XOR演算
#     encrypted_bits = ''.join(str(int(input_bit) ^ int(key_bit)) for input_bit, key_bit in zip(input_bits, key_bits))

#     # ビット列を文字列に変換
#     encrypted_string = ''.join(chr(int(encrypted_bits[i:i+8], 2)) for i in range(0, len(encrypted_bits), 8))

#     return encrypted_string

# # 暗号化
# key = "secretkey"
# message = "Hello, World!"
# encrypted_message = xor_cypher(message, key)
# print(encrypted_message)

# # 復号化
# decrypted_message = xor_cypher(encrypted_message, key)
# print(decrypted_message)  # "Hello, World!"が出力される

# def string_to_binary(input_string):
#     x = ''
#     for i in input_string:
#         print(i)
#         x.join(format(ord(i), '08b'))
#         print(x)
#     return ''.join(format(ord(char), '08b') for char in input_string)

# # 使用例
# key = 'hoge'
# binary_key = string_to_binary(key)
# print(binary_key)

def xor_enc_dec(input, output, length):
    key = 'K'
    for i in range(length):
        output[i] = input[i] ^ ord(key)
        
def enc_file(inputfile, outputfile):
    with open(inputfile, 'rb') as f:
        data = f.read()
    length = len(data)
    data = bytearray(data)
    xor_enc_dec(data, data, length)
    with open(outputfile, 'wb') as f:
        f.write(data)
