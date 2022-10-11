from datetime import datetime
from platform import python_branch
import pyaudio
import wave

def RecordStart(filename, record_secs = 1200):
  form_1 = pyaudio.paInt16 # 16-bit resolution
  chans = 1 # 1 channel
  samp_rate = 44100 # 44.1kHz sampling rate
  chunk = 4096 # 2^12 samples for buffer
  #record_secs = 1200 # seconds to record
  dev_index = 1 # device index found by p.get_device_info_by_index(ii)
  wav_output_filename = filename #str(today)+'.wav' # name of .wav file
  p = pyaudio.PyAudio()
  info = p.get_host_api_info_by_index(0)
  numdevices = info.get('deviceCount')


  for dev in range(p.get_device_count()):
    print(p.get_device_info_by_index(dev).get('name'))  

#for i in range(0, numdevices):
#    if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
#        print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'))


  audio = pyaudio.PyAudio() # create pyaudio instantiation

# create pyaudio stream
  stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)
  print("recording")
  frames = []

# loop through stream and append audio chunks to frame array
  for ii in range(0,int((samp_rate/chunk)*record_secs)):
    data = stream.read(chunk)
    frames.append(data)

  print("finished recording")

# stop the stream, close it, and terminate the pyaudio instantiation
  stream.stop_stream()
  stream.close()
  audio.terminate()

# save the audio frames as .wav file
  wavefile = wave.open(wav_output_filename,'wb')
  wavefile.setnchannels(chans)
  wavefile.setsampwidth(audio.get_sample_size(form_1))
  wavefile.setframerate(samp_rate)
  wavefile.writeframes(b''.join(frames))
  wavefile.close()

today = datetime.today().strftime('%Y%m%d')
file_name = str(today) + ".wav"
RecordStart(file_name,1200)


#import toGoogleDrive

#toGoogleDrive.toGoogleDrive(file_name)