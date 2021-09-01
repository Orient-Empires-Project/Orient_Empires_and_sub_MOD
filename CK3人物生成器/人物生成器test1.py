import re
# from tqdm import tqdm
import csv
import codecs
'''
# class trait:
#     def __init__(self, traitName, traitValue) -> None:
#         self.key = traitName
#         self.value = traitValue
#     def __str__(self) -> str:
#         return '    %s = %s\n'% (self.key, self.value)


# class OldPerson:
#     def __init__(self) -> None:
#         self.id = None # number
#         self.id_comment = None
#         self.name = None
#         self.dynasty = None # number
#         self.religion = None
#         self.culture = None
#         self.traitlist = []
#         self.martial = None # number
#         self.father = None
#         self.mother = None

#         self.eventlist =[
#             # Event("730.1.1","birth"),
#             # Event("790.1.1","death")
#         ]
#     def __str__(self) -> str:
#         id_str = '%d = {' % (self.id)
#         id_comment_str = ' '+self.id_comment+'\n'
#         name_str = '    name = %s\n' % (self.name)
#         dynasty_str = '    dynasty = %d\n' % (self.dynasty)
#         religion_str = '    religion = %s\n' % (self.religion)
#         culture_str = '    culture = %s\n' % (self.culture)
#         trait_str=''
#         for trait in self.traitlist:
#             trait_str += '    trait = %s\n' % (trait)
#         martial_str = '    martial = %d\n' % (self.martial) if self.martial != None else ''
#         father_str = '    father = %s\n' % (self.father) if self.father!=None else ''
#         mother_str = '    father = %s\n' % (self.mother) if self.mother!=None else ''
#         event_str= ''
#         end_str = '}'
#         for event in self.eventlist:
#             event_str += (str(event)+'\n')
#         return id_str+id_comment_str+\
#                 name_str+\
#                 dynasty_str+\
#                 religion_str+\
#                 culture_str+\
#                 trait_str+\
#                 martial_str+\
#                 father_str+\
#                 mother_str+\
#                 event_str+\
#                 end_str

# Cao = OldPerson()
# Cao.id = 1059714
# Cao.id_comment = '# Guiyi Cao family'
# Cao.name = "Yijin"
# Cao.dynasty = 1055036
# Cao.religion="vajrayana"
# Cao.culture="han"

# Cao.traitlist.append('education_martial_4')
# Cao.traitlist.append('ambitious')
# Cao.father = 'han0010'
# Cao.mother = 'han0011'
# Cao.eventlist.append(Event("842.1.1","birth","yes"))
# Cao.eventlist.append(Event("916.1.1","add_spouse","304194"))
# Cao.eventlist.append(Event("935.1.1","death","yes"))
# print (Cao)
# pass
'''
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

class Event:
    # def __init__(self, year, month, day, eventtype, eventcontent) -> None:
    #     self.year = year
    #     self.month = month
    #     self.day = day
    #     self.eventtype = eventtype
    #     self.eventcontent = eventcontent

    def __init__(self, year_month_day, eventtype, eventcontent) -> None:
        self.year = year_month_day.split('.')[0]
        self.month = year_month_day.split('.')[1]
        self.day = year_month_day.split('.')[2]
        self.eventtype = eventtype
        self.eventcontent = eventcontent# can be a event or a event list

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
        %s.%s.%s = {
            ''' % (self.year,self.month,self.day)# TODO print a list
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
        eventdetailstr = '''
                %s = %s
        ''' % (self.reason,self.detail)
        return eventdetailstr

class Person:
    def __init__(self) -> None:
        # self.id = None # number
        # self.id_comment = None
        # self.name = None
        # self.dynasty = None # number
        # self.religion = None
        # self.culture = None
        # self.traitlist = [] # a list of trait
        # self.martial = None # number
        # self.father = None
        # self.mother = None
        self.id = 0 # number
        self.id_comment = "None"
        self.name = "None"
        self.dynasty = 0 # number
        self.religion = "None"
        self.culture = "None"
        self.traitlist = [] # a list of trait
        self.martial = 0 # number
        self.father = 0
        self.mother = 0
        self.eventlist =[
            # Event("730.1.1","birth"),
            # Event("790.1.1","death")
        ]
    def __str__(self) -> str:
        id_str = '%d = {' % (self.id)
        id_comment_str = ' '+self.id_comment+'\n'
        name_str = '    name = %s\n' % (self.name)
        dynasty_str = '    dynasty = %d\n' % (self.dynasty)
        religion_str = '    religion = %s\n' % (self.religion)
        culture_str = '    culture = %s\n' % (self.culture)
        trait_str=''
        for trait in self.traitlist:
            # trait_str += str(trait)
            trait_str += '    trait = %s\n' % (trait)
        martial_str = '    martial = %d\n' % (self.martial) if self.martial != None else ''
        father_str = '    father = %s\n' % (self.father) if self.father!=None else ''
        mother_str = '    father = %s\n' % (self.mother) if self.mother!=None else ''
        event_str= ''
        end_str = '}'
        for event in self.eventlist:
            event_str += (str(event)+'\n')
        return id_str+id_comment_str+\
                name_str+\
                dynasty_str+\
                religion_str+\
                culture_str+\
                trait_str+\
                martial_str+\
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
    Chao.eventlist.append(Event("842.1.1","birth","yes"))
    Chao.eventlist.append(Event("916.1.1","add_spouse","304194"))
    Chao.eventlist.append(Event("935.1.1","death",[Eventdetail("death_reason","death_dungeon"),Eventdetail("killer","張撒八")]))
    # TODO 925.12.28 = { effect = { imprison = 194325 } }
    print (Chao)