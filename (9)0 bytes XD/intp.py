import sys
def intp(code):
    if code == '0':
        print('0')
        return
    if code == '1':
        while True:
            print('1')

def intp_test():
    a=sys.argv
    if len(a)!=2:
        print('Usage: intp <file>')
        return
    f=a[1]
    with open(f,'r',encoding='utf-8',errors='ignore') as f:
        c=f.read()
    intp(c)

if __name__=='__main__':
    intp_test()