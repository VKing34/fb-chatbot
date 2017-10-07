if __name__ == '__main__':
    output_characters = 'We copy you down, Eagle.\n'
    output_bytes = output_characters.encode('utf-8')
    with open('eagle.txt','wb') as fout:
        fout.write(output_bytes)