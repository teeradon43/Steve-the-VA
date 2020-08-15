# This is a virtual assistant program that gets the date, current time, responds back with a random greeting, and returns information on a person

#pip install pyaudio
#pip install SpeechRecognition
#pip install gTTS
#pip install wikipedia

#Import libraries
import speech_recognition as sr
import os
from gtts import gTTS
import datetime
import warnings
import calendar
import random
import wikipedia

#Ignore any warning messages
from wikipedia import wikipedia

warnings.filterwarnings('ignore')
#Record Audio and return as a string
def recordAudio():

    r = sr.Recognizer() #Creating a recognizer object

    #Open the microphone and start recording
    with sr.Microphone() as source:
        print(get_device_count())
        print('พูดอะไรก็ได้...')
        audio = r.listen(source)

    #Use Googles speech recognition
    data = ''
    try:
        data = r.recognize_google(audio,None,'th')
        print('คุณพูดว่า: '+data)
    except sr.UnknownValueError: #Check for unknown errors
        print('Google Speech Recognition could not understand the audio, unknown error')
    except sr.RequestError as e:
        print('Request results from Google Speech Recognition service error '+e)

    return data

# get the virtual assistant response
def assistantResponse(text):

    print(text)

    #Convert the text to speech
    myobj = gTTS(text= text, lang='th',slow=False)

    #Save the converted audio to a file
    myobj.save('assistant_response.mp3')

    #Play the converted file
    os.system('start assistant_response.mp3')

# function for wake words or phrase
def wakeWord(text):
    WAKE_WORDS = ['สวัสดี', 'โอเคคอมพิวเตอร์', 'hello'] #A list of wake words

    text = text.lower() # Converting the text to all lower case words

    #Check if the users command/text contains a wake word/phrase
    for phrase in WAKE_WORDS:
        if phrase in text:
            return True

    #If the wake word isn't found in the text from the loop so it returns false
    return False

#get the current date
def getDate():

    now = datetime.datetime.now()
    my_date = datetime.datetime.today()

    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    day_names = ['วันอาทิตย์', 'วันจันทร์', 'วันอังคาร', 'วันพุธ', 'วันพฤหัส', 'วันศุกร์', 'วันเสาร์']

    month_names = ['มกราคม', 'กุมพาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน',
                   'กรกฎาคม', 'สิงหาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']
    return 'วันนี้'+day_names[int(now.strftime("%w"))] +'ที่ ' +str(dayNum) +' '+month_names[monthNum-1]

# return a random greeting response function
def greeting(text):

    #Greeting inputs
    GREETING_INPUTS = ['สวัสดี', 'hello']

    #Greeting responses
    GREETING_RESPONSES = ['สวัสดี', 'เป็นยังไงบ้าง', 'ว่ายังไง']

    #If the uses input is a greeting, then return a randomly chosen greeting response
    for word in GREETING_INPUTS:
        if text.__contains__(word):
            return random.choice(GREETING_RESPONSES)

    #If no greeting was detected then return an empty string
    return ''

#get a person first and last name from the text
def getPerson(text):

    wordList = text.split() #Splitting the text into a list of words

    for i in range(0, len(wordList)):
        if i + 3 <= len(wordList) -1 and wordList[i].lower() == 'who' and wordList[i+1].lower() == 'is':
            return wordList[i+2] + ' ' + wordList[i+3]

while True:

    #Record the audio
    text = recordAudio()
    response = ''

    # check for the wake words
    if(wakeWord(text) == True):

        #Check for greetings by the user
        response = response + greeting(text)

        #Check to see if the user said anything having to do with the date
        if(text.__contains__('วันที่เท่าไหร่')):
            get_date = getDate()
            response = response + ' ' + get_date

        #Check to see iff the use said anything haveing to do with the tiem
        if('time' in text):
            now = datetime.datetime.now()
            meridiem =''
            if now.hour >= 12:
                meridiem = 'p.m' # Post Meridiem (PM) after midday
                hour = now.hour - 12
            else:
                meridiem = 'a.m'
                hour = now.hour

            #Convert minute into a proper string
            if now.minute < 10:
                minute = '0'+str(now.minute)
            else:
                minute = str(now.minute)

            response = response + ' It is ' + str(hour) + ':' + minute + ' ' + meridiem +' .'


        #Check to see if the user said 'who is'
        if(text.__contains__('ใครคือ')):
            person = getPerson(text)
            wiki = wikipedia.summary(person, sentences=2)
            response = response + ' ' + wiki

        #Have the assistant respond back using audio and the text from response
        print('Response = ' + response)
        assistantResponse(response)

