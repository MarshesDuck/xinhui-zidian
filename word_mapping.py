"""
there are two ways to represent the "q" sound, but for readability of generated text,
I won't be including the version in the brackets below.

    "Q": {
        "qi": "کِ (ٿِ)‎",
        "qia": "کِیَا (ٿِیَا)‎",
        "qian": "کِیًا (ٿِیًا)‎",
        "qiang": "کِیَانْ (ٿِیَانْ)‎",
        "qiao": "کِیَوْ (ٿِیَوْ)‎",
        "qie": "کِیَ (ٿِیَ)‎",
        "qin": "ٿٍ‎",  # omission on the wikipedia page, the version I'm using is کٍ
        "qing": "کٍْ (ٿٍْ)‎",
        "qiong": "کِیٌ (ٿِیٌ)‎",
        "qiu": "کِیُوْ (ٿِیُوْ)‎",
        "qu": "کِیُوِ (ٿِیُوِ)‎",
        "quan": "کِیُوًا (ٿِیُوًا)‎",
        "que": "کِیُوَ (ٿِیُوَ)‎",
        "qun": "کٌ (ٿٌ)‎"
    },
"""

phonetic_dict = {
    "A": {
        "a": "اَ‎",
        "ai": "اَیْ‎",
        "an": "اً‎",
        "ang": "اَنْ‎",
        "ao": "اَوْ‎"
    },
    "B": {
        "ba": "بَا‎",
        "bai": "بَیْ‎",
        "ban": "بًا‎",
        "bang": "بَانْ‎",
        "bao": "بَوْ‎",
        "bei": "بُوِ‎",
        "ben": "بٌ‎",
        "beng": "بٍْ‎",
        "bi": "بِ‎",
        "bian": "بِیًا‎",
        "biao": "بِیَوْ‎",
        "bie": "بِیَ‎",
        "bin": "بٍ‎",
        "bing": "بِیٍٔ‎",
        "bo": "بُوَ‎",
        "bu": "بُ‎"
    },
    "C": {
        "ca": "ڞَا‎",
        "cai": "ڞَیْ‎",
        "can": "ڞًا‎",
        "cang": "ڞَانْ‎",
        "cao": "ڞَوْ‎",
        "ce": "ڞَ‎",
        "cen": "ڞٍ‎",
        "ceng": "ڞْ‌ٍ‎",
        "ci": "ڞِ‎",
        "cong": "ڞْو‎",
        "cou": "ڞِوْ‎",
        "cu": "ڞُ‎",
        "cuan": "ڞُوًا‎",
        "cui": "ڞُوِ‎",
        "cun": "ڞٌ‎",
        "cuo": "ڞُوَ‎",
        "cha": "چَا‎",
        "chai": "چَیْ‎",
        "chan": "چًا‎",
        "chang": "چَانْ‎",
        "chao": "چَوْ‎",
        "che": "چَ‎",
        "chen": "چٍ‎",
        "cheng": "چٍْ‎",
        "chi": "چِ‎",
        "chong": "چْو‎",
        "chou": "چِوْ‎",
        "chu": "چُ‎",
        "chuai": "چُوَیْ‎",
        "chuan": "چُوًا‎",
        "chuang": "چُوَانْ‎",
        "chui": "چُوِ‎",
        "chun": "چٌ‎",
        "chuo": "چُوَ‎"
    },
    "D": {
        "da": "دَا‎",
        "dai": "دَیْ‎",
        "dan": "دًا‎",
        "dang": "دَانْ‎",
        "dao": "دَوْ‎",
        "de": "دْ‎",
        "dei": "دِْ‎",
        "deng": "دٍْ‎",
        "di": "دِ‎",
        "dia": "دِیَا‎",
        "dian": "دِیًا‎",
        "diao": "دِیَوْ‎",
        "die": "دِیَ‎",
        "ding": "دٍ‎",
        "diu": "دِیُوْ‎",
        "dong": "دْو‎",
        "dou": "دِوْ‎",
        "du": "دُو‎",
        "duan": "دُوًا‎",
        "dui": "دُوِ‎",
        "dun": "دٌ‎",
        "duo": "دُوَ‎"
    },
    "E": {
        "e": "عَ‎",
        "er": "عَر‎",
        "en": "ءٌ"
    },
    "F": {
        "fa": "فَا‎",
        "fan": "فًا‎",
        "fang": "فَانْ‎",
        "fei": "فِ‎",
        "fen": "فٌ‎",
        "feng": "فٍْ‎",
        "fo": "فُوَ‎",
        "fou": "فِوْ‎",
        "fu": "فُ‎"
    },
    "G": {
        "ga": "قَا‎",
        "gai": "قَیْ‎",
        "gan": "قًا‎",
        "gang": "قَانْ‎",
        "gao": "قَوْ‎",
        "ge": "قْ‎",
        "gei": "قِ‎",
        "gen": "قٍ‎",
        "geng": "قٍْ‎",
        "gong": "قْو‎",
        "gou": "قِوْ‎",
        "gu": "قُ‎",
        "gua": "قُوَا‎",
        "guai": "قُوَیْ‎",
        "guan": "قُوًا‎",
        "guang": "قُوَانْ‎",
        "gui": "قُوِ‎",
        "gun": "قٌ‎",
        "guo": "قُوَ‎"
    },
    "H": {
        "ha": "خَا‎",
        "hai": "خَیْ‎",
        "han": "خًا‎",
        "hang": "خَانْ‎",
        "hao": "خَوْ‎",
        "he": "حَ‎",
        "hei": "حِ‎",
        "hen": "حٍ‎",
        "heng": "حٍْ‎",
        "hong": "خْو‎",
        "hou": "خِوْ‎",
        "hu": "خُ‎",
        "hua": "خُوَا‎",
        "huai": "خُوَیْ ‎",
        "huan": "خُوًا‎",
        "huang": "خُوَانْ‎",
        "hui": "خُوِ‎",
        "hun": "خٌ‎",
        "huo": "خُوَ‎"
    },
    "J": {
        "ji": "ݣِ‎",
        "jia": "ݣِیَا‎",
        "jian": "ݣِیًا‎",
        "jiang": "ݣِیَانْ‎",
        "jiao": "ݣِیَوْ‎",
        "jie": "ݣِیَ‎",
        "jin": "ݣٍ‎",
        "jing": "ݣٍْ‎",
        "jiong": "ݣِیٌ‎",
        "jiu": "ݣِیُوْ‎",
        "ju": "ݣِیُوِ‎",
        "juan": "ݣِیُوًا‎",
        "jue": "ݣِیُوَ‎",
        "jun": "ݣٌ‎"
    },
    "K": {
        "ka": "کَا‎",
        "kai": "کَیْ‎",
        "kan": "کًا‎",
        "kang": "کَانْ‎",
        "kao": "کَوْ‎",
        "ke": "کْ‎",
        "ken": "کٍ‎",
        "keng": "کٍْ‎",
        "kong": "کْو‎",
        "kou": "کِوْ‎",
        "ku": "کُ‎",
        "kua": "کُوَا‎",
        "kuai": "کُوَیْ‎",
        "kuan": "کُوًا‎",
        "kuang": "کُوَانْ‎",
        "kui": "کُوِ‎",
        "kun": "کٌ‎",
        "kuo": "کُوَ‎"
    },
    "L": {
        "la": "لَا‎",
        "lai": "لَیْ‎",
        "lan": "لًا‎",
        "lang": "لَانْ‎",
        "lao": "لَوْ‎",
        "le": "لَ‎",
        "lei": "لُوِ‎",
        "leng": "لٍْ‎",
        "li": "لِ‎",
        "lia": "لِیَا‎",
        "lian": "لِیًا‎",
        "liang": "لِیَانْ‎",
        "liao": "لِیَوْ‎",
        "lie": "لِیَ‎",
        "lin": "لٍ‎",
        "ling": "لِیٍٔ‎",
        "liu": "لِیُوْ‎",
        "long": "لْو‎",
        "lou": "لِوْ‎",
        "lu": "لُ‎",
        "lv": "لِیُوِ‎",
        "luan": "لُوًا‎",
        "lue": "لُوَ‎",
        "lun": "لٌ‎",
        "luo": "لُوَ‎"
    },
    "M": {
        "ma": "مَا‎",
        "mai": "مَیْ‎",
        "man": "مًا‎",
        "mang": "مَانْ‎",
        "mao": "مَوْ‎",
        "me": "مَ‎",
        "mei": "مُوِ‎",
        "men": "مٌ‎",
        "meng": "مٍْ‎",
        "mi": "مِ‎",
        "mian": "مِیًا‎",
        "miao": "مِیَوْ‎",
        "mie": "مِیَ‎",
        "min": "مٍ‎",
        "ming": "مِیٍٔ‎",
        "miu": "مِیُوْ‎",
        "mo": "مُوَ‎",
        "mou": "مِوْ‎",
        "mu": "مُ‎"
    },
    "N": {
        "na": "نَا‎",
        "nai": "نَیْ‎",
        "nan": "نًا‎",
        "nang": "نَانْ‎",
        "nao": "نَوْ‎",
        "ne": "نَ‎",
        "nei": "نُوِ‎",
        "nen": "نٌ‎",
        "neng": "نٍْ‎",
        "ni": "نِ‎",
        "nian": "نِیًا‎",
        "niang": "نِیَانْ‎",
        "niao": "نِیَوْ‎",
        "nie": "نِیَ‎",
        "nin": "نٍ‎",
        "ning": "نِیٍٔ‎",
        "niu": "نِیُوْ‎",
        "nong": "نْو‎",
        "nu": "نُ‎",
        "nv": "نِیُوِ‎",
        "nuan": "نُوًا‎",
        "nve": "نِیُوَ‎",
        "nuo": "نُوَ‎"
    },
    "O": {
        "o": "عِو‎",
        "ou": "عِوْ‎"
    },
    "P": {
        "pa": "پَا‎",
        "pai": "پَیْ‎",
        "pan": "پًا‎",
        "pang": "پَانْ‎",
        "pao": "پَوْ‎",
        "pei": "پُوِ‎",
        "pen": "پٌ‎",
        "peng": "پٍْ‎",
        "pi": "پِ‎",
        "pian": "پِیًا‎",
        "piao": "پِیَوْ‎",
        "pie": "پِیَ‎",
        "pin": "پٍ‎",
        "ping": "پِیٍٔ‎",
        "po": "پُوَ‎",
        "pou": "پِوْ‎",
        "pu": "پُ‎"
    },
    "Q": {
        "qi": "کِ‎",
        "qia": "کِیَا‎",
        "qian": "کِیًا‎",
        "qiang": "کِیَانْ‎",
        "qiao": "کِیَوْ‎",
        "qie": "کِیَ‎",
        "qin": "کٍٍ‎",
        "qing": "کٍْ‎",
        "qiong": "کِیٌ‎",
        "qiu": "کِیُوْ‎",
        "qu": "کِیُوِ‎",
        "quan": "کِیُوًا‎",
        "que": "کِیُوَ‎",
        "qun": "کٌ‎"
    },
    "R": {
        "ran": "ژًا‎",
        "rang": "ژَانْ‎",
        "rao": "ژَوْ‎",
        "re": "ژَ‎",
        "ren": "ژٍ‎",
        "reng": "ژٍْ‎",
        "ri": "ژِ‎",
        "rong": "ژٌ‎",
        "rou": "ژِوْ‎",
        "ru": "ژُو‎",
        "ruan": "ژُوًا‎",
        "rui": "ژُوِ‎",
        "run": "ژٌ‎",
        "ruo": "ژُوَ‎"
    },
    "S": {
        "sa": "سَا‎",
        "sai": "سَیْ‎",
        "san": "سًا‎",
        "sang": "سَانْ‎",
        "sao": "سَوْ‎",
        "se": "سَ‎",
        "sen": "سٍ‎",
        "seng": "سٍْ‎",
        "si": "سِْ‎",
        "song": "سٌ‎",
        "sou": "سِوْ‎",
        "su": "سُ‎",
        "suan": "صُوًا‎",
        "sui": "صُوِ‎",
        "sun": "صٌ‎",
        "suo": "صُوَ‎",
        "sha": "شَا‎",
        "shai": "شَیْ‎",
        "shan": "شًا‎",
        "shang": "شَانْ‎",
        "shao": "شَوْ‎",
        "she": "شَ‎",
        "shei": "شُوِ‎",
        "shen": "شٍ‎",
        "sheng": "شٍْ‎",
        "shi": "شِ‎",
        "shou": "شِوْ‎",
        "shu": "شُ‎",
        "shua": "شُوَا‎",
        "shuai": "شُوَیْ‎",
        "shuan": "شُوًا‎",
        "shuang": "شُوَانْ‎",
        "shui": "شُوِ‎",
        "shun": "شٌ‎",
        "shuo": "شُوَ‎"
    },
    "T": {
        "ta": "تَا‎",
        "tai": "تَیْ‎",
        "tan": "تًا‎",
        "tang": "تَانْ‎",
        "tao": "تَوْ‎",
        "te": "تْ‎",
        "teng": "تٍْ‎",
        "ti": "تِ‎",
        "tian": "تِیًا‎",
        "tiao": "تِیَوْ‎",
        "tie": "تِیَ‎",
        "ting": "تٍ‎",
        "tong": "طْو‎",
        "tou": "تِوْ‎",
        "tu": "تُ‎",
        "tuan": "طُوًا‎",
        "tui": "طُوِ‎",
        "tun": "طٌ‎",
        "tuo": "طُوَ‎"
    },
    "W": {
        "wa": "وَا‎",
        "wai": "وَیْ‎",
        "wan": "وًا‎",
        "wang": "وَانْ‎",
        "wei": "وِ‎",
        "wen": "وٌ‎",
        "weng": "وٍْ‎",
        "wo": "وَ‎",
        "wu": "وُ‎"
    },
    "X": {
        "xi": "ثِ‎",
        "xia": "ثِیَا‎",
        "xian": "ثِیًا‎",
        "xiang": "ثِیَانْ‎",
        "xiao": "ثِیَوْ‎",
        "xie": "ثِیَ‎",
        "xin": "ثٍ‎",
        "xing": "ثٍْ‎",
        "xiong": "ثِیٌ‎",
        "xiu": "ثِیُوْ‎",
        "xu": "ثِیُوِ‎",
        "xuan": "ثِیُوًا‎",
        "xue": "ثِیُوَ‎",
        "xun": "ثٌ‎"
    },
    "Y": {
        "ya": "یَا‎",
        "yan": "یًا‎",
        "yang": "یَانْ‎",
        "yao": "یَوْ‎",
        "ye": "یَ‎",
        "yi": "ءِ‎",
        "yin": "ءٍ‎",
        "ying": "یٍ‎",
        "yong": "یٌ‎",
        "you": "یُوْ‎",
        "yu": "یُوِ‎",
        "yuan": "یُوًا‎",
        "yue": "یُوَ‎",
        "yun": "ىٌ"
    },
    "Z": {
        "za": "زَا‎",
        "zai": "زَیْ‎",
        "zan": "زًا‎",
        "zang": "زَانْ‎",
        "zao": "زَوْ‎",
        "ze": "زَ‎",
        "zei": "زِْ‎",
        "zen": "زٍ‎",
        "zeng": "زٍْ‎",
        "zi": "زِ‎",
        "zong": "ظْو‎",
        "zou": "زِوْ‎",
        "zu": "زُو‎",
        "zuan": "زُوًا‎",
        "zui": "ظُوِ‎",
        "zun": "ظٌ‎",
        "zuo": "ظُوَ‎",
        "zha": "جَا‎",
        "zhai": "جَیْ‎",
        "zhan": "جًا‎",
        "zhang": "جَانْ‎",
        "zhao": "جَوْ‎",
        "zhe": "جَ‎",
        "zhei": "جُوِ‎",
        "zhen": "جٍ‎",
        "zheng": "جٍْ‎",
        "zhi": "جِ‎",
        "zhong": "جْو‎",
        "zhou": "جِوْ‎",
        "zhu": "جُ‎",
        "zhua": "جُوَا‎",
        "zhuai": "جُوَیْ‎",
        "zhuan": "جُوًا‎",
        "zhuang": "جُوَانْ‎",
        "zhui": "جُوِ‎",
        "zhun": "جٌ‎",
        "zhuo": "جُوَ‎"
    },
}
