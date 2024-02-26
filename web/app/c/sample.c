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

void xor_encrypt_decrypt(char *input, char *output, int length)
{
    char key = 'K'; // 暗号化/復号化キー
    for (int i = 0; i < length; i++)
    {
        output[i] = input[i] ^ key;
    }
}

void encrypt_image_file(char *input_filename, char *output_filename)
{
    FILE *input_file = fopen(input_filename, "rb");
    FILE *output_file = fopen(output_filename, "wb");

    if (input_file == NULL || output_file == NULL)
    {
        printf("File could not be opened\n");
        return;
    }

    fseek(input_file, 0, SEEK_END);
    long file_size = ftell(input_file);
    fseek(input_file, 0, SEEK_SET);

    char *buffer = (char *)malloc(file_size);
    char *output = (char *)malloc(file_size);

    fread(buffer, 1, file_size, input_file);
    xor_encrypt_decrypt(buffer, output, file_size);
    fwrite(output, 1, file_size, output_file);

    free(buffer);
    free(output);

    fclose(input_file);
    fclose(output_file);
}