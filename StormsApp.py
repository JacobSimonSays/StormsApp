import streamlit as st
import datetime
from zoneinfo import ZoneInfo

header = st.container()

with header:
	st.title('STORMS Spell List')

col1, col2, col3 = st.columns((1,1,1))
error_box = st.container()

with col3:
	status = st.select_slider('', ['Unlock', 'Lock'])
	if status == 'Lock':
		locked = True
	elif status == 'Unlock':
		locked = False
	time = st.text('Last Locked: ' + datetime.datetime.now(ZoneInfo('America/Chicago')).strftime('%I:%M:%S'))
with col1:
	name = st.radio('Class', ['Bard', 'Cleric', 'Druid', 'Wizard'], disabled = locked) #['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Rogue', 'Wizard'])
	
with col2:
	level = st.radio('Level', [1, 2, 3, 4, 5], disabled = locked)

level_one, gap1, level_two = st.columns((2,1,2))
level_three, gap2, level_four = st.columns((2,1,2))
level_five = st.container()

c1a, c1b, c1c, c2a, c2b, c2c, c3a, c3b, c3c, c4a, c4b, c4c, c5 = 0,0,0,0,0,0,0,0,0,0,0,0,0

if name == 'Cleric':
	if level >= 1:
		with level_one:
			st.subheader('Level 1')
			c1a = st.slider('Blessing from Wounds', 0, 3*level, disabled = locked)
			c1b = st.slider('Heal', 0, 1, disabled = locked)
			c1c = st.slider('Summon Ally', 0, 3*level, disabled = locked)
	if level >= 2:
		with level_two:
			st.subheader('Level 2')
			c2a = st.slider('Blessing from Harm', 0, 3*(level-1), disabled = locked)
			c2b = st.slider('Create Zombie', 0, 3*(level-1), disabled = locked)
			c2c = st.slider('Release', 0, 3*(level-1), disabled = locked)
	if level >= 3:
		with level_three:
			st.subheader('Level 3')
			c3a = st.slider('Create Vampire', 0, 3*(level - 2), disabled = locked)
			c3b = st.slider('Greater Heal',0, 3*(level - 2), disabled = locked)
			c3c = st.slider('Resurrect', 0, 3*(level - 2), disabled = locked)
	if level >= 4:
		with level_four:
			st.subheader('Level 4')
			c4a = st.slider('Create Lich', 0, 3*(level - 3), disabled = locked)
			c4b = st.slider('Mass Healing', 0, 3*(level - 3), disabled = locked)
			c4c = st.slider('Phoenix Tears', 0, 3*(level - 3), disabled = locked)
	if level == 5:
		with level_five:
			st.subheader('Level 5')
			arch = st.radio('Archetype', ['None', 'Necromancer', 'Priest'], horizontal = True, disabled = locked)
			if arch == 'None':
				c5 = 0
			elif arch == 'Necromancer':
				c5 = 2
				if c4b + c3b + c3c + c1b + c1c > 0:
					with error_box:
						st.error('Selected Spells Violate Archetype')
			elif arch == 'Priest':
				c5 = 2
				if c4a + c3a + c2b > 0:
					with error_box:
						st.error('Selected Spells Violate Archetype')

if name == 'Druid':
	if level >= 1:
		with level_one:
			st.subheader('Level 1')
			c1a = st.slider('Attunement to Fire', 0, 3*level, disabled = locked)
			c1b = st.slider('Eagle Eye', 0, 3*level, disabled = locked)
			c1c = st.slider('Entangle', 0, 3*level, disabled = locked)
	if level >= 2:
		with level_two:
			st.subheader('Level 2')
			c2a = st.slider('Attunement to Water', 0, 3*(level-1), disabled = locked)
			c2b = st.slider('Mist Cloak', 0, 3*(level-1), disabled = locked)
			c2c = st.slider('Serpent Fangs', 0, 3*(level-1), disabled = locked)
	if level >= 3:
		with level_three:
			st.subheader('Level 3')
			c3a = st.slider('Attunement to Earth', 0, 3*(level - 2), disabled = locked)
			c3b = st.slider('Bear Strength',0, 3*(level - 2), disabled = locked)
			c3c = st.slider('Corrosion', 0, 3*(level - 2), disabled = locked)
	if level >= 4:
		with level_four:
			st.subheader('Level 4')
			c4a = st.slider('Attunement to Air', 0, 3*(level - 3), disabled = locked)
			c4b = st.slider('Call Lightning', 0, 3*(level - 3), disabled = locked)
			c4c = st.slider('Wolf Pack', 0, 3*(level - 3), disabled = locked)
	if level == 5:
		with level_five:
			st.subheader('Level 5')
			arch = st.radio('Archetype', ['None', 'Wild Heart', 'Avatar'], horizontal = True, disabled = locked)
			if arch == 'None':
				c5 = 0
			elif arch == 'Wild Heart':
				c5 = 2
				if c4a + c3a + c2a + c1a > 0:
					with error_box:
						st.error('Selected Spells Violate Archetype')
			elif arch == 'Avatar':
				c5 = 2
				if c4c + c3b + c2c + c1b > 0:
					with error_box:
						st.error('Selected Spells Violate Archetype')

if name == 'Wizard':
	if level >= 1:
		with level_one:
			st.subheader('Level 1')
			c1a = st.slider('Heat Weapon', 0, 3*level, disabled = locked)
			c1b = st.slider('Force Bolt', 0, 3*level, disabled = locked)
			c1c = st.slider('Shove', 0, 3*level, disabled = locked)
	if level >= 2:
		with level_two:
			st.subheader('Level 2')
			c2a = st.slider('Banish', 0, 3*(level-1), disabled = locked)
			c2b = st.slider('Counterspell', 0, 3*(level-1), disabled = locked)
			c2c = st.slider('Ice Ball', 0, 3*(level-1), disabled = locked)
	if level >= 3:
		with level_three:
			st.subheader('Level 3')
			c3a = st.slider('Hold Person', 0, 3*(level - 2), disabled = locked)
			c3b = st.slider('Icy Blast',0, 3*(level - 2), disabled = locked)
			c3c = st.slider('Lightning Bolt', 0, 3*(level - 2), disabled = locked)
	if level >= 4:
		with level_four:
			st.subheader('Level 4')		
			c4a = st.slider('Dragged Below', 0, 3*(level - 3), disabled = locked)
			c4b = st.slider('Fireball', 0, 2, disabled = locked)
			c4c = st.slider('Shatter', 0, 3*(level - 3), disabled = locked)
	if level == 5:
		with level_five:
			st.subheader('Level 5')
			arch = st.radio('Archetype', ['None', 'Battlemage', 'Evoker'], horizontal = True, disabled = locked)
			if arch == 'None':
				c5 = 0
			elif arch == 'Battlemage':
				c5 = 2
				if c4b + c3c + c2c + c1b > 0:
					with error_box:
						st.error('Selected Spells Violate Archetype')
			elif arch == 'Evoker':
				c5 = 2
				if c4a + c4c + c3a + c3b + c2a + c2b + c1a + c1c > 0:
					with error_box:
						st.error('Selected Spells Violate Archetype')

c4 = c5 + c4a + c4b + c4c
c3 = c4 + c3a + c3b + c3c
c2 = c3 + c2a + c2b + c2c
c1 = c2 + c1a + c1b + c1c

l4 = 3/2*(abs(level-3)+(level-3))
l3 = 3/2*(abs(level-2)+(level-2))
l2 = 3/2*(abs(level-1)+(level-1))
l1 = 3/2*(abs(level)+(level))

if c4 > l4 or c3 > l3 or c2 > l2 or c1 > l1:
	with error_box:
		st.error('Selected Spells Exceed Current Level')
