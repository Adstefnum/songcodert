

#hpw to decrypt the sound

def text_to_notes(text):

	notes = {"A":"A3","B":"A#3","C":"B3","D":"C3","E":"C#3","F":"D3","G":"D#3","H":"E3","I":"F3","J":"F#3","K":"G3","L":"G#3","M":"A4","N":"A#4","O":"B4","P":"C4","Q":"C#4","R":"D4","S":"D#4","T":"E4","U":"F4","V":"F#4","W":"G4","X":"G#4","Y":"A5","Z":"G#6"}
	notes_list = []

	for t in text:
		if t.upper() in notes.keys():
			notes_list.append(notes[str(t.upper())])

	return notes_list



def notes_to_freqs(notes_list):

	freqs = {"A3":"220","A#3":"233","B3":"247","C3":"131","C#3":"139","D3":"147","D#3":"156","E3":"165","F3":"175","F#3":"185","G3":"196","G#3":"208","A4":"440","A#4":"466","B4":"494","C4":"262","C#4":"277","D4":"294","D#4":"311","E4":"330","F4":"349","F#4":"370","G4":"392","G#4":"415","A5":"880","G#6":"1661"}
	freqs_list = []

	for n in notes_list:
		if n in freqs.keys():
			freqs_list.append(freqs[str(n)])

	return freqs_list



def play_notes(freqs_list):

	dur = 0
	import winsound

	for f in freqs_list:
		if int(f) == 220 or int(f) < 440 :
			dur = 3000

		elif int(f) == 440 or int(f) < 880 :
			dur = 4000

		elif int(f) == 880 or int(f) < 1760 :
			dur  = 5000

		winsound.Beep(int(f),dur)

def encrypt(text):
	notes_list = text_to_notes(text)
	freqs_list = notes_to_freqs(notes_list)
	play_notes(freqs_list)






	
