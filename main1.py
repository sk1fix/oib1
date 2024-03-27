# def decryption(path: str) -> None:
#     key = {}

#     with open('decrypted.txt','w+', encoding='UTF-8') as write_f:
#         with open(path, 'r', encoding='UTF-8') as file:
#             for line in file:
#                 temp = ''
#                 line = line.strip()
#                 for i in line:
#                     try:
#                         temp += key[str(i)]
#                     except:
#                         temp += str(i)
#                 write_f.write(temp + '\n')


def frequency_analysis(path):
    key={}
    k=0
    a=[]
    with open('decrypted.txt','w+',encoding='UTF-8') as wr:
        with open(path, 'r', encoding='UTF-8') as file:
            for line in file:
                temp = ''
                line = line.strip()
                for i in line:
                    try:
                        key[i]+=1
                    except:
                        key[i]=0
                    k+=1
            for i in key:
                a.append([str(i), key[i]/k])
            sorted_data = sorted(a, key=lambda x: x[1], reverse=True)
            for i in sorted_data:
                wr.write(i[0] + ' : ' + str(i[1]) + '\n')

    



def main():
    path = 'encrypted.txt'
    frequency_analysis(path)



if __name__ == "__main__":
    main()