# SPDX-FileCopyrightText: 2021 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
KITT interactive voice box by RaspiPico Noob
"""
import board
import audiomp3
import time
import array
import math
import audiobusio
import random
import digitalio
import neopixel

#Defining IR Sensor pin
tracker = digitalio.DigitalInOut(board.GP0)
tracker.direction = digitalio.Direction.INPUT

# Remove DC bias before computing RMS.
def mean(values):
    return sum(values) / len(values)


def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )

    return math.sqrt(samples_sum / len(values))

mic = audiobusio.PDMIn(board.GP6, board.GP3, sample_rate=16000, bit_depth=16)
samples = array.array('H', [0] * 160)

audio = audiobusio.I2SOut(board.GP13, board.GP14, board.GP15)


#assigning KITT's dash indicator lights
first_row = neopixel.NeoPixel(board.GP22, 2)
second_row = neopixel.NeoPixel(board.GP21, 2)
third_row = neopixel.NeoPixel(board.GP20, 2)
fourth_row = neopixel.NeoPixel(board.GP19, 2)
auto_cruise = neopixel.NeoPixel(board.GP18, 3)
normal_cruise = neopixel.NeoPixel(board.GP17, 3)
pursuit = neopixel.NeoPixel(board.GP16, 3)


first_row.brightness = 0.25
second_row.brightness = 0.25
third_row.brightness = 0.25
fourth_row.brightness = 0.25
auto_cruise.brightness = 0.25
normal_cruise.brightness = 0.25
pursuit.brightness = 0.25

BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
ORANGE = (255, 40, 0)

indicator = [1,2,3]

#list of mp3s to get KITT responding to sound. You can reorganize and add other lists as you wish
begin = ["I am the voice.mp3", "I am KITT.mp3", "I am a Knight Industries.mp3"]
intro = ["Hello!.mp3", "Not now, I have a headache.mp3", "Hello.mp3",  "You again_.mp3", "Im so glad to see you.mp3", "Perhaps I can be of some help.mp3", "Its good to hear your voice.mp3"]
middle = ["Ehum.mp3", "Good heavens! And I thought Michael was difficult.mp3", "I detect a certain tone in your voice.mp3", "How very unproductive.mp3", "I beg your pardon.mp3", "Surely youre not serious.mp3", "The things Im forced to put up with.mp3", "Well that's a new one.mp3", "Why_.mp3", "I dont follow your logic.mp3", "Tell me about it.mp3", "You must be joking.mp3", "Based on what_.mp3", "Easy for you to say.mp3"]
answer = ["Definitely possible.mp3", "I certainly hope so.mp3", "I suppose so.mp3", "I think so.mp3", "If you say so.mp3", "Of course.mp3", "Probably.mp3", "Im afraid so.mp3", "I cant believe its a real possibility.mp3", "I certainly hope not.mp3", "I dont think so.mp3", "In a word, no.mp3", "Im afraid not.mp3", "Negative.mp3", "Not a chance.mp3", "Not exactly.mp3", "Not to my knowledge.mp3", "My databanks have nothing on it.mp3", "I dont understand.mp3", "I have no idea.mp3", "If you say so.mp3"]
greeting = ["Sometimes I wonder if you really need me.mp3", "Your palms are clammy.mp3","Are you alright1.mp3", "Are you alright2.mp3","You've probably begun.mp3", "Youre awfully quiet.mp3", "Where are your pants_.mp3", "Next time you want something handled in a specific way.mp3", "My sensors.mp3", "Did you hear that_.mp3", "How much longer will we be staying here_.mp3", "How are you feeling_.mp3", "Deafness.mp3", "Can I be of assistance_.mp3", "Can a Rolls-Royce do computer scans_.mp3", "Bon voyage.mp3","I'm sorry I try.mp3","Are you there....mp3","As a machine.mp3"]
joke = ["I stopped for gas the other day....mp3", "When I was a kid....mp3", "What do you think.mp3", "Im definitely dark and handsome....mp3", "Im the Knight Industries Two Thousand, sure enough.mp3"]
thanks = ["De nada.mp3", "Dont mention it.mp3"]

sound = open(greeting[0], "rb")
initial = time.monotonic()
decoder = audiomp3.MP3Decoder(sound)


try:
    time.sleep(3)
    decoder.file = open("Key0.mp3", "rb")
    audio.play(decoder)
    while audio.playing:
        first_row.fill(YELLOW)
        time.sleep(0.5)
    decoder.file = open("Key1.mp3", "rb")
    audio.play(decoder)
    while audio.playing:
        second_row.fill(YELLOW)
        time.sleep(0.5)
    decoder.file = open("Key2.mp3", "rb")
    audio.play(decoder)
    while audio.playing:
        third_row.fill(RED)
        time.sleep(0.5)
    decoder.file = open("Key3.mp3", "rb")
    audio.play(decoder)
    while audio.playing:
        fourth_row.fill(RED)
        time.sleep(0.5)
    light = random.choice(indicator)
    if light ==1:
        auto_cruise.fill(ORANGE)
    elif light ==2:
        normal_cruise.fill(YELLOW)
    else:
        pursuit.fill(BLUE)
    time.sleep(1)
    decoder.file = open(random.choice(begin), "rb")
    audio.play(decoder)
    while audio.playing:
        pass
    time.sleep(0.5) 
    while True:
        if tracker.value == False:
            mic.record(samples, len(samples))
            magnitude = normalized_rms(samples)
            print((magnitude,))
            time.sleep(0.1)
            # you may need to modify magnitude levels depending on how sensitive you want your microphone to be
            if magnitude > 170 and magnitude < 400:
                time.sleep(4)
                decoder.file = open(random.choice(intro), "rb")
                audio.play(decoder)
                while audio.playing:
                    pass
                time.sleep(1)
                decoder.file = open(random.choice(middle), "rb")
                audio.play(decoder)
                while audio.playing:
                    pass                    
                time.sleep(1)
                decoder.file = open(random.choice(answer), "rb")
                audio.play(decoder)
                while audio.playing:
                    pass
                time.sleep(1)
                initial = time.monotonic()
            elif magnitude > 400:
                time.sleep(4)
                decoder.file = open(random.choice(joke), "rb")
                audio.play(decoder)
                while audio.playing:
                    pass    
                time.sleep(1)
                initial = time.monotonic()
            elif magnitude > 100 and magnitude < 170:
                time.sleep(1)
                decoder.file = open(random.choice(thanks), "rb")
                audio.play(decoder)
                while audio.playing:
                    pass    
                time.sleep(1)
                initial = time.monotonic()
    # This is how KITT will respond if IR sensor is active but sound is below level 100
    # KITT will repond in 10 seconds and then every 30 seconds after that         
            else:
                if magnitude < 100:
                    now = time.monotonic()
                    print(initial)
                    print(now)
                    if now - initial > 10:
                        decoder.file = open(random.choice(greeting), "rb")
                        audio.play(decoder)
                        while audio.playing:
                            pass      
                        time.sleep(1)              
                        initial = now + 30
finally:
    first_row.fill((0))
    second_row.fill((0))
    third_row.fill((0))
    fourth_row.fill((0))
    auto_cruise.fill((0))
    normal_cruise.fill((0))
    pursuit.fill((0))
