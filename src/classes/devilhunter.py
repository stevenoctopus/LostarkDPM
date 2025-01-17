"""
Actions & Buff bodies of devilhunter
"""
from src.layers.static.character_layer import CharacterLayer
from src.layers.dynamic.buff_manager import BuffManager
from src.layers.dynamic.skill_manager import SkillManager
from src.layers.dynamic.skill import Skill
from src.layers.dynamic.buff import Buff
from src.layers.core.utils import seconds_to_ticks
from src.layers.static.constants import AWAKENING_DAMAGE_PER_SPECIALIZATION


# 핸드건 치명타 피해량 특화 계수
SPEC_COEF_1 = 0.75 / 699
# 샷건 스킬 피해량 특화 계수
SPEC_COEF_2 = 0.25 / 699
# 라이플 스킬 물/마방관 특화 계수
SPEC_COEF_3 = 0.25 / 699

CLASS_BUFF_DICT = {
  'Specialization': {
    'name': 'specialization',
    'buff_type': 'stat',
    'effect': 'specialization',
    'duration': 999999,
    'priority': 7,
  },
  'Pistoleer_3': {
    'name': 'pistoleer',
    'buff_type': 'stat',
    'effect': 'pistoleer_3',
    'duration': 999999,
    'priority': 7,
  },
  'Synergy_1': {
    'name': 'synergy_1',
    'buff_type': 'stat',
    'effect': 'synergy_1',
    'duration': 8,
    'priority': 7,
  },
  'Synergy_2': {
    'name': 'synergy_1',
    'buff_type': 'stat',
    'effect': 'synergy_1',
    'duration': 12,
    'priority': 7,
  },
  'Fierce': {
    'name': 'fierce',
    'buff_type': 'stat',
    'effect': 'fierce',
    'duration': 6,
    'priority': 9,
  },
}


######## Finalize Skill #########
# finalize skill by tripod and rune
def finalize_skill(skill: Skill):
  name  = skill.get_attribute('name')
  tripod = skill.get_attribute('tripod')
  rune = skill.get_attribute('rune')
  # connect actions
  if name == 'AT02 유탄' and tripod[2] == '2' and rune[:2] =='출혈':
    skill.triggered_actions.append('extend_bleed')
  # apply tripods
  if name == 'AT02 유탄':
    if tripod[0] == '3':
      skill.triggered_actions.append('activate_synergy')
  elif name == '나선의 추적자':
    if tripod[0] == '2':
      skill.triggered_actions.append('activate_synergy')
  elif name == '이퀄리브리엄':
    if tripod[0] == '2':
      skill.triggered_actions.append('activate_synergy2')
  elif name == '끊임없는 맹공':
    if tripod[0] == '2':
      skill.triggered_actions.append('activate_fierce')

######## Actions #########
# 유탄 출혈 시간 갱신 action
def extend_bleed(buff_manager: BuffManager, skill_manager: SkillManager, skill_on_use: Skill):
  def duration_increase(buff: Buff):
    if buff.name == '출혈':
      buff.duration += seconds_to_ticks(3)
  buff_manager.apply_function(duration_increase)

# 치적 시너지 등록
def activate_synergy(buff_manager: BuffManager, skill_manager: SkillManager, skill_on_use: Skill):
  if (skill_on_use.get_attribute('name') == 'AT02 유탄' 
      or skill_on_use.get_attribute('name') == '나선의 추적자'):
    buff_manager.register_buff(CLASS_BUFF_DICT['Synergy_1'], skill_on_use)
    
def activate_synergy2(buff_manager: BuffManager, skill_manager: SkillManager, skill_on_use: Skill):
  if (skill_on_use.get_attribute('name') == '이퀄리브리엄'):
    buff_manager.register_buff(CLASS_BUFF_DICT['Synergy_2'], skill_on_use)
    
# 맹공 버프 등록
def activate_fierce(buff_manager: BuffManager, skill_manager: SkillManager, skill_on_use: Skill):
  buff_manager.register_buff(CLASS_BUFF_DICT['Fierce'], skill_on_use)
    

######## Buff bodies ########
def specialization(character: CharacterLayer, skill: Skill, buff: Buff):
    s = character.get_attribute('specialization')
    s_multiplier_1 = (1 + s * AWAKENING_DAMAGE_PER_SPECIALIZATION)
    s_handgun_additional_crit_damage = s * SPEC_COEF_1
    s_shotgun_multiplier = (1 + s * SPEC_COEF_2)
    s_rifle_defense_reduction_rate = s * SPEC_COEF_3
    if skill.get_attribute('identity_type') == 'Awakening':
      s_dm = skill.get_attribute('damage_multiplier')
      skill.update_attribute('damage_multiplier', s_dm * s_multiplier_1)
    elif skill.get_attribute('identity_type') == "Handgun":
      s_acd = skill.get_attribute('crit_damage')
      skill.update_attribute('crit_damage', s_acd + s_handgun_additional_crit_damage)
    elif skill.get_attribute('identity_type') == 'Shotgun':
      s_dm = skill.get_attribute('damage_multiplier')
      skill.update_attribute('damage_multiplier', s_dm * s_shotgun_multiplier)
    elif skill.get_attribute('identity_type') == 'Rifle':
      s_drr = skill.get_attribute('defense_reduction_rate')
      skill.update_attribute('defense_reduction_rate', s_drr + s_rifle_defense_reduction_rate)
    # 치명타 적중 시 방관 증가 트포 처리
    # 이퀄리브리엄 - 급소 사격
    if (skill.get_attribute('name') == '이퀄리브리엄' and skill.get_attribute('tripod')[2] == '2'):
      s_drr = skill.get_attribute('defense_reduction_rate')
      c_cr = character.get_attribute('crit_rate')
      skill.update_attribute('defense_reduction_rate', s_drr + 0.50 * c_cr)
    # 데스페라도
    if (skill.get_attribute('name') == '데스페라도' and skill.get_attribute('tripod')[1] == '1'):
      s_drr = skill.get_attribute('defense_reduction_rate')
      c_cr = character.get_attribute('crit_rate')
      skill.update_attribute('defense_reduction_rate', s_drr + 0.25 * c_cr)

# 핸드거너 각인
def pistoleer_3(character: CharacterLayer, skill: Skill, buff: Buff):
    if skill.get_attribute('identity_type') == 'Awakening':
      s_dm = skill.get_attribute('damage_multiplier')
      skill.update_attribute('damage_multiplier', s_dm * 1.50)
    elif skill.get_attribute('identity_type') == "Handgun":
      s_dm = skill.get_attribute('damage_multiplier')
      skill.update_attribute('damage_multiplier', s_dm * 1.75)

# 치적 시너지 (8초)
def synergy_1(character: CharacterLayer, skill: Skill, buff: Buff):
    s_acr = skill.get_attribute('crit_rate')
    skill.update_attribute('crit_rate', s_acr + 0.10)

# 맹공 버프(6초)
def fierce(character: CharacterLayer, skill: Skill, buff: Buff):
    c_as = character.get_attribute('attack_speed')
    c_ms = character.get_attribute('movement_speed')
    c_cr = character.get_attribute('cooldown_reduction')
    character.update_attribute('attack_speed', c_as + 0.08)
    character.update_attribute('movement_speed', c_ms + 0.08)
    character.update_attribute('cooldown_reduction', c_cr + 0.05)