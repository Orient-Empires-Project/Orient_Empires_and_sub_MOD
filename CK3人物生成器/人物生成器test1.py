import re
# from tqdm import tqdm
import csv
import codecs
# filenamelist = ['东方王朝王国头衔',
# '东方王朝帝国头衔'
# ]
# for filename in filenamelist:
#     with codecs.open(filename+".csv", "r", encoding="utf-8-sig") as csvFile:
#         reader = csv.reader(csvFile)
#         x = {}
#         for item in reader:
#     #        if reader.line_num == 1:
#     #            continue
#             x[item[0]] = item[-1]
#             # print(item[-1])

# pass
yes = True
no = False
class CK3_Date:
    def __init__(self, *paras) -> None:
        if  len(paras)==1:
            self.year = paras[0].split('.')[0]
            self.month = paras[0].split('.')[1]
            self.day = paras[0].split('.')[2]
        else:
            self.year = paras[0]
            self.month = paras[1]
            self.day = paras[2]
    def __eq__(self, other: object) -> bool:
        selfyears= int(self.year)+int(self.month)/12+int(self.day)/12/30
        otheryears= int(other.year)+int(other.month)/12+int(other.day)/12/30
        return selfyears==otheryears
    def __lt__(self, other: object) -> bool:
        selfyears= int(self.year)+int(self.month)/12+int(self.day)/12/30
        otheryears= int(other.year)+int(other.month)/12+int(other.day)/12/30
        return selfyears<otheryears
    def __le__(self, other: object) -> bool:
        selfyears= int(self.year)+int(self.month)/12+int(self.day)/12/30
        otheryears= int(other.year)+int(other.month)/12+int(other.day)/12/30
        return selfyears<=otheryears
    def __ge__(self, other: object) -> bool:
        selfyears= int(self.year)+int(self.month)/12+int(self.day)/12/30
        otheryears= int(other.year)+int(other.month)/12+int(other.day)/12/30
        return selfyears>=otheryears
    def __gt__(self, other: object) -> bool:
        selfyears= int(self.year)+int(self.month)/12+int(self.day)/12/30
        otheryears= int(other.year)+int(other.month)/12+int(other.day)/12/30
        return selfyears>otheryears

    # 检测是否是CK3合法时间。指1.1.1至1453.12.31之间。不考虑小月和闰月。
    def check_period(self) -> bool:
        if int(self.year)>1453 or int(self.year)<0:
            return False
        if int(self.month)>12 or int(self.month)<1:
            return False
        if int(self.day)>31 or int(self.day)<1:
            return False
        return True

    def check_ck3_period(*paras) -> bool:#month:str=None, day:str=None
        if  len(paras)==1:
            date_to_check = CK3_Date(paras[0])
        else:
            date_to_check = CK3_Date(paras[0], paras[1], paras[1])
        return date_to_check.check_period()

    def __str__(self) -> str:
        date_str = "%s.%s.%s"%(self.year,self.month,self.day)
        return date_str
    
class CK3_Event:
    def __init__(self, *paras) -> None:
        if len(paras)==5:
            self.year = paras[0] # year
            self.month = paras[1] #month
            self.day = paras[2] #day
            self.ck3_date = CK3_Date(self.year, self.month, self.day)
            self.eventtype = paras[3] #eventtype
            self.eventcontent = paras[4] #eventcontent
        elif type(paras[0])==type(CK3_Date('1.1.1')):
            self.ck3_date = paras[0] # CK3_Date
            self.year = self.ck3_date.year
            self.month = self.ck3_date.month
            self.day = self.ck3_date.day
            self.eventtype = paras[1] #eventtypettype
            self.eventcontent = paras[2] #eventcontent # can be a event or a event list
        elif type(paras[0])==type(''):
            self.year = paras[0].split('.')[0]
            self.month = paras[0].split('.')[1]
            self.day = paras[0].split('.')[2]
            self.ck3_date = CK3_Date(self.year, self.month, self.day)
            self.eventtype = paras[1] #eventtypettype
            self.eventcontent = paras[2] #eventcontent # can be a event or a event list

    def __str__(self) -> str:
        if type(self.eventcontent) == type(''):
            ret_str = ''

            ev_str = '''
    %s.%s.%s = {
        %s = %s
    }
            ''' % (self.year,self.month,self.day,self.eventtype,self.eventcontent)
            return ret_str+ev_str
        elif type(self.eventcontent) == type([]):
            ret_str = ''

            ev_str_begin = '''
    %s.%s.%s = {''' % (self.year,self.month,self.day)# TODO print a list
            ev_str_list = ''''''
            for detail in self.eventcontent:
                ev_str_list += str(detail)
                
            ev_str_end = '''
    }
            '''
            return ret_str+ev_str_begin+ev_str_list+ev_str_end
class Eventdetail:
    def __init__(self,reason,detail) -> None:
        self.reason = reason
        self.detail = detail
    def __str__(self) -> str:
        eventdetailstr = '''\n        %s = %s''' % (self.reason,self.detail)
        return eventdetailstr

class Person:
    def __init__(self) -> None:
        self.id = None # should be a number but alse can be a str
        self.id_comment = ""
        self.name = "No name"
        self.dna = None
        self.female = 'no' 
        self.dynasty = None # should be a number but alse can be a str
        self.house = None # should be a number but alse can be a str
        self.religion = "No religion"
        self.culture = "No culture"

        self.diplomacy = None #外交
        self.martial= None #军事
        self.stewardship = None #财政
        self.intrigue = None #密谋
        self.learning = None #学识
        self.prowess = None #勇武
        self.fertility = None # 生育率
        self.health = None #健康

        self.traitlist = [] # a list of trait
        self.disallow_random_traits = "no" # TODO
        self.father = None
        self.mother = None
        self.eventlist =[
            # CK3_Event("730.1.1","birth"),
            # CK3_Event("790.1.1","death")
        ]
    def skill_to_str(self,skill:str) -> str:
        skillValue= eval("self."+skill)
        if skillValue == None:
            return ''
        elif skillValue == 'no':
            return ''
        # elif skillValue == 'yes':
        #     return '    %s = %s\n' % (skill,'yes')
        else:
            return f'    {skill} = {skillValue}\n'# TODO %全面换成f{}
    def __str__(self) -> str:
        id_str = '%s = {' % (self.id)
        id_comment_str = ' '+self.id_comment+'\n'
        name_str = '    name = %s\n' % (self.name)
        females_str = self.skill_to_str('female')
        dynasty_str = '    dynasty = %s\n' % (self.dynasty)
        house_str = self.skill_to_str('house')
        religion_str = self.skill_to_str('religion')
        culture_str = self.skill_to_str('culture')
        trait_str=''
        for trait in self.traitlist:
            # trait_str += str(trait)
            trait_str += '    trait = %s\n' % (trait)
        diplomacy_str = self.skill_to_str('diplomacy')
        martial_str = self.skill_to_str('martial')
        stewardship_str = self.skill_to_str('stewardship')
        intrigue_str = self.skill_to_str('intrigue')
        learning_str = self.skill_to_str('learning')
        prowess_str = self.skill_to_str('prowess')
        fertility_str = self.skill_to_str('fertility')
        health_str = self.skill_to_str('health')

        disallow_random_traits_str = self.skill_to_str('disallow_random_traits')

        father_str = self.skill_to_str('father')
        mother_str = self.skill_to_str('mother')
        event_str= ''
        end_str = '\n}'
        for event in self.eventlist:
            event_str += (str(event)+'')# 自带\n
        return id_str+id_comment_str+\
                name_str+\
                females_str+\
                dynasty_str+\
                house_str+\
                religion_str+\
                culture_str+\
                trait_str+\
                disallow_random_traits_str+\
                diplomacy_str+martial_str+stewardship_str+intrigue_str+learning_str+prowess_str+\
                fertility_str+health_str+\
                father_str+\
                mother_str+\
                event_str+\
                end_str
if __name__ == '__main__':
    Chao = Person()
    Chao.id = 1059714
    Chao.id_comment = '# Guiyi Cao family'
    Chao.name = "Yijin"
    Chao.dynasty = 1055036
    Chao.religion="vajrayana"
    Chao.culture="han"

    Chao.traitlist.append('education_martial_4')
    Chao.traitlist.append('ambitious')
    Chao.father = 'han0010'
    Chao.mother = 'han0011'
    Chao.martial = 15
    Chao.eventlist.append(CK3_Event("842.1.1","birth","yes"))
    Chao.eventlist.append(CK3_Event("916.1.1","add_spouse","304194"))
    Chao.eventlist.append(CK3_Event("935.1.1","death",[Eventdetail("death_reason","death_dungeon"),Eventdetail("killer","張撒八")]))
    # TODO 925.12.28 = { effect = { imprison = 194325 } }
    print (Chao)