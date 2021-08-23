yes = 'yes'
# test_1059715 ={}

test_1059715 = \
{
	"name":"Huinan",
	"dynasty":1055036,
	"female":yes,
	"religion":"vajrayana",
	"culture":"han",
	"father":1059714,
	"time_905_1_1":{
		"birth":yes
	},
	"time_937_1_1" : {
		"death":yes
	}
}
# print (test_1059715)

import yaml
import json
tang_1415220 = { #拓跋他 Tuoba Ta, Xianbei name 它大翰 Tadahan.",
    "name" : "Tadahan",
    "dynasty" : 1029300 ,#Tuoba",
    "religion" : "tengri_pagan",
    "culture" : "xianbei",
    "father" : 1415301,
    "416.1.1" : {
    "birth" : "yes",
    "name" : "Ta"
    },
    "488.10.17" : {
    "death" : "yes"
    }
}

# print(tang_1415220)
han = '''
1059718 = {
	name="Yuanzhong"
	dynasty=1055036
	religion="vajrayana"
	culture="han"
	father=1059714
	trait=education_diplomacy_3
	trait=intellect_good_1
	mother=304194
	920.1.1={
		birth=yes # maybe
	}
	974.1.1 = {
		death=yes
	}
}
'''
j = json.dumps(han)

pass