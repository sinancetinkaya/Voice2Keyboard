# Voice2Keyboard

Bu uygulamayı klavye kullanma zorluğu çeken insanlara bir kolaylık olsun diye yazdım.

Uygulama config.ini dosyasında belirtilmiş olan hotkey tuşlarına basıldığında bellir bir süre mikrofondan sesi dinler.
Dinlediği bu sesi Google Ses Tanıma Motoruna gönderir ve geri dönen metni klavyeden aktif olarak programa gönderir.

Programın çalışan halini Voice2Keyboard / [v2k.zip](Voice2Keyboard/v2k.zip) dosyasını indererek kullanabilirsiniz

Dil değişikliğini config.ini dosyasında aşağıdaki gibi yapabilirsiniz 
```
[parameters]
;You can change it to your language
lang=TR

;Hotkey for listening, Control + Alt + s is default. But you can pick up another key
hotkey_listen=0x53
```


# Voice2Keyboard

I wrote this program to help for those who have difficulties using a keyboard.

Program records audio from microphone when the hotkeys are pressed.
Then sends the audio to the Google Speech Recognition Engine and gets back the text. 
Then simulates the keyboard and types the text.

You can download compiled binary from Voice2Keyboard / [v2k.zip](Voice2Keyboard/v2k.zip)

You can specify your language in config.ini as below
```
[parameters]
;You can change it to your language
lang=EN

;Hotkey for listening, Control + Alt + s is default. But you can pick up another key
hotkey_listen=0x53
```
