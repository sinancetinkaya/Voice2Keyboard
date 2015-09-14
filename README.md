# Voice2Keyboard

Bu uygulamayı hem deneme olsun diye hem de klavye kullanma zorluğu çeken insanlara bir kolaylık olsun diye yazdım.

Uygulama config.ini dosyasında belirtilmiş olan hotkey tuşlarına basıldığında bellir bir süre mikrofondan sesi dinler.
Dinlediği bu sesi Google Ses Tanıma Motoruna gönderir ve geri dönen metni klavyeden aktif olarak programa gönderir.

Programın çalışan halini Voice2Keyboard / [v2k.zip](Voice2Keyboard/v2k.zip) dosyasını indererek kullanabilirsiniz

Dil değişikliğini config.ini dosyasında aşağıdaki gibi yapabilirsiniz 
```
[parameters]
;You can change your language
**lang=EN**

;Hotkey for listening, Control + Alt + s is default. But you can pick up another key
hotkey_listen=0x53
```


# Voice2Keyboard

I wrote this program as an exercise as well as to help for those who have difficulties when using keyboard.

Program starts to record audio from microphone when the hotkeys specified in the config.ini file are pressed.
Then sends the audio to Google Speech Recognition Engine and types the received text from the keyboard.

You can download working compiled binary file from Voice2Keyboard / [v2k.zip](Voice2Keyboard/v2k.zip)

You can specify your language in config.ini as below
```
[parameters]
;You can change your language
**lang=EN**

;Hotkey for listening, Control + Alt + s is default. But you can pick up another key
hotkey_listen=0x53
```
