## Samples for Yating Automatic Speech Recognition service

Here are samples for you to test and better understand how to use Yating ASR services.

## Getting started

### Installation

```bash
# install portaudio first if you develop on MAC OS X
brew install portaudio

pip install --global-option='build_ext' --global-option='-I/usr/local/include' --global-option='-L/usr/local/lib' -r requirements.txt

# please check PyAudio site: https://people.csail.mit.edu/hubert/pyaudio/
# if you encouter some issues while installing PyAudio
```

### Usage
```bash

#Step 1: Preprocess the audio file(change file name to test.m4a)
python preprocess_voice.py

#Step 2: Convert audio to text
python wav2text.py

```
see the detail document in [the SDK repository page](https://github.com/TaiwanAILabs-Yating/asr-sdk-python)
