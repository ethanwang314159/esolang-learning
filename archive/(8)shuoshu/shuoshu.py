import sys
def shuoshu_parse(shuoshu):
    shuoshu=shuoshu.strip()
    result=[]
    for i in shuoshu.split('\n'):
        if i.count('吱')!=len(i):
            raise ValueError('Invalid program')
        result.append(len(i))
    return result
def shuoshu_preprocess(parse):
    stack=[]
    matches={}
    for i,j in enumerate(parse):
        if j==5:
            stack.append(i)
        if j==6:
           matched=stack.pop()
           matches[matched]=i
           matches[i]=matched
    return matches
def shuoshu_run(parse,preprocess):
    cp=0
    reg=0
    stack=[0]
    while cp<len(parse):
        if parse[cp]==0:
            pass
        if parse[cp]==1:
            reg=stack[-1]
        if parse[cp]==2:
            stack.append(reg)
        if parse[cp]==3:
            ch=sys.stdin.read(1)
            reg=ord(ch)%256
        if parse[cp]==4:
            print(chr(reg),end='')
        if parse[cp]==5:
            if reg==0:
                cp=preprocess[cp]
        if parse[cp]==6:
            if reg!=0:
                cp=preprocess[cp]
        if parse[cp]==7:
            reg=(reg+1)%256
        if parse[cp]==8:
            reg=(reg-1)%256
        if parse[cp]==9:
            stack[-1]=(stack[-1]+1)%256
        if parse[cp]==10:
            stack[-1]=(stack[-1]-1)%256
        if parse[cp]==11:
            stack.pop()
        if parse[cp]>11:
            stack.append((parse[cp]-12)%256)
        cp+=1
def shuoshu(code):
    parse=shuoshu_parse(code)
    prep=shuoshu_preprocess(parse)
    shuoshu_run(parse,prep)
def shuoshu_test():
    a=sys.argv
    if len(a)!=2:
        print('Usage: shuoshu <file>')
    f=a[1]
    with open(f,'r',encoding='utf-8',errors='ignore') as f:
        c=f.read()
    shuoshu(c)
if __name__=='__main__':
    shuoshu_test()