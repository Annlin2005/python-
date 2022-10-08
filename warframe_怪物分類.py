
Grinner = {
    '輕型裝甲' : {
            '輕型裝甲' : [
                '屠夫',
                '重擊手',
                '烈焰刀客',
                '天蠍',
                '盾槍兵',
                '禁衛軍'
            ]
        },
        '中型裝甲' : {
            '中型裝甲' : [
                '槍兵',
                '菁英槍兵',
                '騎兵',
                '追蹤者',
                '怒焚者',
                '弩砲',
                '沙漠惡徒',
                '開膛者'
            ] 
        },
        '重型裝甲' : {
           '重型裝甲' : [
                '重機槍手',
                '火焰轟擊者',
                '轟擊者',
                '指揮官'
           ] 
        },
        'Boss' : {
            'Boss' : [
                'Captain_Vor',
                'Councilor_Vay_Hek',
                'General_Sargas_Ruk',
                'The_Grustrag_Three',
                'Kela_De_Thaym',
                'Lieutenant_Lech_Kril',
                'Tyl_Regor'
            ]
        }
}
Corpus = {
        '船員' : {
            '船員' : [
                '船員',
                '菁英船員',
                '監工船員',
                '狙擊手船員',
                'Corpus_技師'
            ]
        },
        '恐鳥' : {
            '恐鳥' : [
                '恐鳥',
                '紫色熔岩恐鳥',
                '白色熔岩恐鳥',
                '磁軌炮恐鳥',
                '震盪波恐鳥'
            ]
        },
        '魚鷹' : {
           '魚鷹' : [
                '無人機',
                '吸血魚鷹',
                '地雷魚鷹',
                'oxium魚鷹',
                '清道夫無人機',
                '護盾魚鷹'
           ] 
        },
        '單位' : {
            '單位' : [
                '雷射欄杆',
                '監視器'
            ]
        },
        'Boss' : {
            'Boss' : [
                'Alad_V',
                'Ambulas',
                'Harvester',
                'Hyenda_Pack',
                'Jackal',
                'Raptor',
                'Sgt_Nef_Anyo'
            ]
        }
}
Infested = {
    '步行者' : {
            '步行者' : [
                '疾衝者',
                '奔跳者'
            ]
        },
        '爬行者' : {
            '爬行者' : [
                '爬行者',
                '嘔心爬行者',
                '劇毒爬行者',
                '電擊爬行者',
                '噴吐爬行者'
            ]
        },
        '遠古' : {
            '遠古' : [
                '遠古治癒者',
                '遠古干擾者',
                '遠古劇毒者'
            ]
        },
        'Boss' : {
            'Boss' : [
                'Phorid',
                'Lephantis'
            ]
        } 
        
}
print('Grinner派系')
print("-->")
for Grinner,Grinner_info in Grinner.items() :
    print(Grinner_info)
print('Corpus派系')
print("-->") 
for Corpus,Corpus_info in Corpus.items() :
    print(Corpus_info)
print('Infested派系')
print("-->") 
for Infested,Infested_info in Infested.items() :
    print(Infested_info)



    






