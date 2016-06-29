import re

def rfile(name):
    f = open(name, 'r', encoding = 'utf-8')
    fr = f.read()
    f.close()
    return fr

def lname (fr):
    n = 0
    fr = fr.splitlines()
    for i, line in enumerate (fr):
        if '/teiHead' in line:
            n = i+1
    return str(n)

def wfile(text, name):
    fw = open(name, 'w', encoding = 'utf-8')
    fw.write(text)
    fw.close


def makearr(fr):
    arr = []
    fr = fr.splitlines()
    regex =  '<w lemma=".*" type=".*">.*</w>'
    for line in fr:
        l = re.search(regex, line)
        if l != None:
            if l.group() not in arr:
                arr.append(l.group())
    return arr

def makedict(arr, fr):
    d = {}
    for m in arr:
        d[m] = fr.count(m)
    return d

def makelist(d):
    text = ''
    for s in d:
        text = text + s + '\t' + str(d[s]) + '\n'
    return(text)

    
def fadj(fr):
    regex = '<w lemma=".*" type="l.f.*'
    adj = re.findall(regex, fr)
    return str(len(adj))


def main():
    wfile(lname(rfile('F.xml')), 'Строки заголовка.txt')
    wfile(fadj(rfile('F.xml')), 'Прилагательные.txt')
    wfile(makelist(makedict(makearr(rfile('F.xml')), (rfile('F.xml')))), 'Словарь.csv')
    
if __name__ == '__main__':
    main()
