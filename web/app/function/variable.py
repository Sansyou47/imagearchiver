# オリジナル画像の保存先
imgLocation_origin = 'images/origin/'
# リサイズ画像の保存先
imgLocation_resized = 'images/downsize/'
supportedExtentionList = ['jpg', 'jpeg', 'png']

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