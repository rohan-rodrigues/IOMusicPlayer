from pygame import mixer, time
import speech_recognition as sr


def find_word(arr, keyword):
    for x in arr:
        if x.lower() == keyword.lower():
            return True
    return False


def main():
    music_playing = False

    while True:
        time.Clock().tick(10)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak:")
            audio = r.listen(source)
        mixer.pre_init(44100, -16, 2, 512)
        mixer.init()

        try:
            input = r.recognize_google(audio)
            print(input)
            words_arr = input.split()
            if find_word(words_arr, "music"):
                print("Playing music")
                music_playing = True
                mixer.music.load(
                    "/Users/rohanrodrigues/Documents/Music/UnderControl.mp3")
                mixer.music.play()

            elif find_word(words_arr, "stop") or find_word(
                    words_arr, "pause"):
                print("PAUSED")
                mixer.music.pause()
                music_playing = False

            elif find_word(words_arr, "resume"):
                print("UNPAUSED")
                mixer.music.unpause()
                music_playing = True

            elif find_word(words_arr, "toggle"):
                if music_playing:
                    print("PAUSED")
                    mixer.music.pause()
                    music_playing = False
                else:
                    print("UNPAUSED")
                    mixer.music.unpause()
                    music_playing = True


        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))


if __name__ == "__main__":
    main()

