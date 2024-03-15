#include <stdio.h>
#include <stdlib.h>

int fib(int n)
{
    if (n <= 1)
    {
        return n;
    }
    return fib(n - 1) + fib(n - 2);
}

// XOR暗号化/復号化関数
void xor_encrypt_decrypt(char *input, char *output, int length, char *key)
{
    int count = 0;
    // 入力データの各バイトに対してXOR演算を行う
    for (int i = 0; i < length; i++)
    {
        output[i] = input[i] ^ key[count]; // XOR演算
        count++;
        // 配列の次の要素が終端文字ならカウンタをリセット
        if (key[count] == '\0')
        {
            count = 0;
        }
    }
}

// 画像ファイルを暗号化する関数
void encrypt_image_file(char *input_filename, char *output_filename, char *secretkey)
{
    // ファイルをバイナリモードで開く
    FILE *input_file = fopen(input_filename, "rb");
    FILE *output_file = fopen(output_filename, "wb");

    // ファイルが開けなかった場合
    if (input_file == NULL || output_file == NULL)
    {
        printf("File could not be opened\n");
        return;
    }

    // ファイルサイズを取得
    fseek(input_file, 0, SEEK_END);
    long file_size = ftell(input_file);
    fseek(input_file, 0, SEEK_SET);

    // ファイルの内容を読み込む
    char *buffer = (char *)malloc(file_size);
    char *output = (char *)malloc(file_size);

    // ファイルの内容を暗号化
    fread(buffer, 1, file_size, input_file);
    xor_encrypt_decrypt(buffer, output, file_size, secretkey);
    fwrite(output, 1, file_size, output_file);

    // メモリを解放
    free(buffer);
    free(output);

    // ファイルを閉じる
    fclose(input_file);
    fclose(output_file);
}