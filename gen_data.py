
letters = 'aAàÀảẢãÃáÁạẠăĂằẰẳẲẵẴắẮặẶâÂầẦẩẨẫẪấẤậẬbBcCdDđĐeEèÈẻẺẽẼéÉẹẸêÊềỀểỂễỄếẾệỆfFgGhHiIìÌỉỈĩĨíÍịỊjJkKlLmMnNoOòÒỏỎõÕóÓọỌôÔồỒổỔỗỖốỐộỘơƠờỜởỞỡỠớỚợỢpPqQrRsStTuUùÙủỦũŨúÚụỤưƯừỪửỬữỮứỨựỰvVwWxXyYỳỲỷỶỹỸýÝỵỴzZ0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ '

f = open('./Data/All_tamquoc.txt','r',encoding='utf-8')
str = f.read()
mang_data = str.split('\n')
f.close()

# f = open('./Data/All_tiemdoco2.txt','w',encoding='utf-8')
# for i in range(1,len(mang_data)-1):
#
#     if mang_data[i] != mang_data[i-1] and mang_data[i-1] not in mang_data[i] and mang_data[i].strip()!='':
#         f.write(mang_data[i]+'\n')
# f.close()


f = open('./Data/All_tamquoc1.txt','w',encoding='utf-8')

for line in mang_data:
    line = line.strip()

    count_word = line.split(' ')
    new=''
    if len(count_word) > 17:
        for i in range(0,17):
            new += count_word[i] + ' '
    else:
        new = line.strip()
    if new  != '':
        f.writelines(new.strip()+'\n')

f.close()

# f = open('./Data/All_tamquoc.txt','w',encoding='utf-8')
# temp = 1
# for line in mang_data:
#     if line.strip() != '':
#         for i in line:
#             if i not in letters:
#                 print('dòng ',temp,' ki tu ',i)
#                 line=line.replace(i,'')
#                 temp+=1
#     f.write(line+'\n')
# f.close()

