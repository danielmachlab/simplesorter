
raw = {}
pnc = {}


with open("mvp1.txt") as file:
    line = file.readline()

    while line:
        elmts = line.split(',')
        raw.update({elmts[0].strip(): ''})

        line = file.readline()



with open("mvp2.txt") as file:
    line2 = file.readline()
    while line2:
        elmts = line2.split(',')
        names = elmts[1].split(' ')
        protein_name = names[0]
        pnc.update({elmts[0]: protein_name})
        try:
            line2 = file.readline()
        except:
            print('Hit Except')
            break







for pc in pnc:
    # replace key pair in eid
    x = pnc.get(pc).strip()
    raw.update({pc: x})

for pro in raw:
    x = raw.get(pro).strip()
    print(pro.strip(), x, sep='\t', end="\n")


