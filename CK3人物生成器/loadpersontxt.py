from 人物生成器test1 import *
import re
waitForAPerson = True
leftbracecount = 0 
eventdate = CK3_Date('2.2.2')
with open (r'C:\Users\Helly\Documents\PMOD\Orient_Empires_and_sub_MOD\CK3人物生成器\东方人物库\characters 原版\SWMH+E_tuhun copy.txt','r',encoding="utf-8") as personfile,\
    open(r'temp.txt','w',encoding="utf-8") as personfile2:
    f = personfile.readlines()
    for line in f:
        # print (line)
        t = line.replace('=',' = ').replace('  =',' =').replace('=  ','= ').split('#')[0].replace('{','{\n')#.replace('}','\n}')
        if "}" in t:
            # print ("old "+t)
            t = t.replace('}','\n}')
            # print ('new '+t)
        if t.count('=')>1:
            itemlist = t.split('=')
            newitemlist = []
            for item in itemlist:
                if re.search('[\w]+[\s]+[\w]+',item):
                    item = item.strip().replace(' ',' \n')
                newitemlist.append(item)
            t='='.join(newitemlist)
            pass
        if '\n' not in t:
            t=t+'\n'
        if t == '\n' or re.match('[\s]+$',t):
            continue


        personfile2.write(t)
        
# exit()
with open(r'temp.txt','r',encoding="utf-8") as personfile3,\
    open(r'C:\Users\Helly\Documents\PMOD\Orient_Empires_and_sub_MOD\CK3人物生成器\东方人物库\characters 原版\SWMH+E_tuhun_output.txt','w',encoding="utf-8") as personfile4:
    pf = personfile3.readlines()
    for line in pf:
        t = line.split('#')[0]
        if t == '':
            continue
        # print (t)
        if waitForAPerson:
            p = Person()
            waitForAPerson = not waitForAPerson
            leftbracecount = 0
            if re.search('[A-Za-z0-9]+ = {',t):
                p.id = t.split('=')[0].strip()
                # print (waitForAPerson)
                print("id  ="+p.id)
        else:# 开始读人
            if re.search('dynasty =',t):
                p.dynasty= t.split('=')[-1].strip()
                # print("dynasty = "+p.dynasty)
            if re.search('name =',t):
                p.name= t.split('=')[-1].strip()
                # print("name = "+p.name)
            if re.search('culture =',t):
                p.culture= t.split('=')[-1].strip()
                # print("culture = "+p.culture)
            if re.search('religion =',t):
                p.religion= t.split('=')[-1].strip()
                # print("religion = "+p.religion)
            if re.search('employer =',t):
                p.employer= t.split('=')[-1].strip()
                # print("employer = "+p.employer)
            # if re.search('culture =',t):
            #     p.culture= t.split('=')[-1].strip()
            #     print("culture = "+p.culture)
            if re.search('[0-9]+\.[0-9]+\.[0-9]+ =',t):
                eventdate = CK3_Date(t.split('=')[0].strip())
                leftbracecount += 1
                continue
            if leftbracecount>0 :
                if re.search('[A-Za-z0-9]+[\s]*=',t):
                    if t.split('=')[-1].strip()=='{':
                        leftbracecount+=1
                        timeblock2 = CK3_Event(eventdate,t.split('=')[0].strip(),[])# TODO 多层 pyparsing ？
                        # print ("t.split('=')[0].strip()"+t.split('=')[0].strip())
                        continue
                    else:
                        pass
                    if leftbracecount==1:
                        timeblock = CK3_Event(eventdate,t.split('=')[0].strip(),t.split('=')[-1].strip())
                        p.eventlist.append(timeblock)
                    elif leftbracecount==2 and re.search('[A-Za-z0-9]+[\s]*=',t):
                        timeblock2.eventcontent.append(Eventdetail(t.split('=')[0].strip(),t.split('=')[-1].strip()))
                        pass
                if '}' in t:
                    if leftbracecount==2:
                        p.eventlist.append(timeblock2)
                    leftbracecount+=-1
            elif '}' in t and not waitForAPerson:
                waitForAPerson = True
                print (p)
                personfile4.writelines(str(p)+'\n')

