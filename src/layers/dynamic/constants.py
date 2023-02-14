""" 
Constants for dynamic part
"""
# constants and hyperparameters for dynamic layers

"""
Unit transformation
"""
TICKS_PER_SECOND = 100

def seconds_to_ticks(seconds):
  return seconds * TICKS_PER_SECOND

def ticks_to_seconds(ticks):
  return ticks / TICKS_PER_SECOND

"""
Skill coefficient table
"""
SKILL_DAMAGE_COEFF = {
  "aeromancer": 
  [
    0.00000,
    0.0164,
    0.0101,
    0.0083,
    0.00731,
    0.00671,
    0.00631,
    0.00601,
    0.00576,
    0.00559,
    0.00544,
    0.00591,
    0.00620,
  ],
  "battlemaster": 
  [
    0.00000,
    0.0164,
    0.0101,
    0.00829,
    0.00732,
    0.00671,
    0.00629,
    0.00599,
    0.00576,
    0.00558,
    0.00543,
    0.00591,
    0.00620,
  ],
  "berserker": 
  [
    0.00000,
    0.0164,
    0.0102,
    0.00832,
    0.00732,
    0.00671,
    0.00631,
    0.00601,
    0.00576,
    0.00559,
    0.00543,
    0.00591,
    0.00620,
  ],
  "blade": 
  [
    0.00000,
    0.0164,
    0.0101,
    0.00827,
    0.00729,
    0.00669,
    0.00628,
    0.00597,
    0.00575,
    0.00557,
    0.00542,
    0.00589,
    0.00619,
  ],
  "blaster": 
  [
    0.00000,
    0.0164,
    0.0102,
    0.00831,
    0.00731,
    0.00671,
    0.00631,
    0.00601,
    0.00576,
    0.00559,
    0.00543,
    0.00590,
    0.00620,
  ],
  "demonic": 
  [
    0.00000,
    0.0164,
    0.0103,
    0.00836,
    0.00735,
    0.00677,
    0.00635,
    0.00604,
    0.00577,
    0.00562,
    0.00548,
    0.00596,
    0.00623,
  ],
  "destroyer": 
  [
    0.00000,
    0.0164,
    0.0101,
    0.00828,
    0.00731,
    0.00671,
    0.00629,
    0.00599,
    0.00576,
    0.00558,
    0.00543,
    0.00590,
    0.00620,
  ],
  "devilhunter": 
  [
    0.00000,
    0.0233,
    0.0132,
    0.0103,
    0.00881,
    0.00789,
    0.00729,
    0.00683,
    0.00646,
    0.00621,
    0.00597,
    0.00649,
    0.00681,
  ],
  "gunslinger": 
  [
    0.00000,
    0.0233,
    0.0132,
    0.0103,
    0.00881,
    0.00789,
    0.00729,
    0.00683,
    0.00646,
    0.00621,
    0.00597,
    0.00649,
    0.00681,
  ],
  "infighter": 
  [
    0.00000,
    0.0164,
    0.0102,
    0.00832,
    0.00732,
    0.00671,
    0.00631,
    0.00601,
    0.00576,
    0.00559,
    0.00543,
    0.00591,
    0.00620,
  ],
  "lancemaster": 
  [
    0.00000,
    0.0212,
    0.0120,
    0.00940,
    0.00801,
    0.00717,
    0.00662,
    0.00621,
    0.00588,
    0.00565,
    0.00543,
    0.00591,
    0.00620,
  ],
  "reaper": 
  [
    0.00000,
    0.0164,
    0.0101,
    0.00829,
    0.00731,
    0.00671,
    0.00629,
    0.00599,
    0.00576,
    0.00558,
    0.00543,
    0.00590,
    0.00620,
  ],
  "scouter": 
  [
    0.00000,
    0.0164,
    0.0102,
    0.00831,
    0.00731,
    0.00671,
    0.00631,
    0.00601,
    0.00576,
    0.00559,
    0.00543,
    0.00590,
    0.00620,
  ],
  "sorceress": 
  [
    0.00000,
    0.0164,
    0.0101,
    0.00828,
    0.00731,
    0.00671,
    0.00629,
    0.00599,
    0.00576,
    0.00558,
    0.00543,
    0.00590,
    0.00620,
  ],
  "striker": 
  [
    0.00000,
    0.0164,
    0.0101,
    0.00831,
    0.00731,
    0.00671,
    0.00629,
    0.00599,
    0.00576,
    0.00559,
    0.00543,
    0.00591,
    0.00620,
  ],
  "summoner": 
  [
    0.00000,
    0.0164,
    0.0102,
    0.00834,
    0.00732,
    0.00672,
    0.00631,
    0.00602,
    0.00577,
    0.00561,
    0.00545,
    0.00592,
    0.00621,
  ],
  "warlord": 
  [
    0.00000,
    0.0164,
    0.0102,
    0.00832,
    0.00732,
    0.00671,
    0.00632,
    0.00601,
    0.00576,
    0.00559,
    0.00543,
    0.00591,
    0.00620,
  ],
}


"""
Jewel convert list
"""
DAMAGE_JEWEL_LIST = [
    0,
    0.03,
    0.06,
    0.09,
    0.12,
    0.15,
    0.18,
    0.21,
    0.24,
    0.30,
    0.40
]

COOLDOWN_JEWEL_LIST = [
    0,
    0.02,
    0.04,
    0.06,
    0.08,
    0.10,
    0.12,
    0.14,
    0.16,
    0.18,
    0.20
]

"""
Rune convert list
"""

# 질풍 / Rune Galewind
RUNE_GW = {
    "고급": 0.05,
    "희귀": 0.08,
    "영웅": 0.12,
    "전설": 0.14
}

# 속행 / Rune Quick Recharge
RUNE_QR = {
    "고급": 'rune_qr_1',
    "희귀": 'rune_qr_2',
    "영웅": 'rune_qr_3',
    "전설": 'rune_qr_4'
}

# 광분 / Rune RAGE
RUNE_RG = {
    "고급": 'rune_rg_1',
    "희귀": 'rune_rg_2',
    "영웅": 'rune_rg_3',
    "전설": 'rune_rg_4'
}

# 출혈 / Rune Bleed
RUNE_BD = {
    "고급": 'rune_bd_1',
    "희귀": 'rune_bd_2',
    "영웅": 'rune_bd_3',
    "전설": 'rune_bd_4',
}

# 심판 / Rune Judgement
RUNE_JM = {
    "고급": 'rune_jm_1',
    "희귀": 'rune_jm_2',
    "영웅": 'rune_jm_3',
    "전설": 'rune_jm_4',
}

# 이외 룬 처리 / rest runes
RUNE_NONE = {
    "고급": None,
    "희귀": None,
    "영웅": None,
    "전설": None,
}
RUNE_ALL = {
    "질풍": RUNE_GW,
    "속행": RUNE_QR,
    "광분": RUNE_RG,
    "출혈": RUNE_BD,
    "집중": RUNE_NONE,
    "단죄": RUNE_NONE,
    "심판": RUNE_JM,
    "압도": RUNE_NONE,
    "풍요": RUNE_NONE,
    "수호": RUNE_NONE,
    "정화": RUNE_NONE,
}

def get_rune_effect(category, level):
    return RUNE_ALL[category][level]

