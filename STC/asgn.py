"""
F(p)= 2^ ((p-69)/12) ) * 440  to calculate frequency   with pitch p
octave is divided in 12 parts 
F(P+1)/f(P)  == 2^(1/12)= = 1.059
sound has amp,freq,timbre,intensity,power,loudnesss etc

intensity W/met^2  ie   dB


complex sound has frequency k* fundamental/harmonic freq.
"""
import 












































# import librosa
# import numpy as np

# # Load the audio file
# audio_file = 'test.mp3'
# y, sr = librosa.load(audio_file)

# # Calculate the onset envelopes
# onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=512, aggregate=np.median)

# # Detect note onsets
# onset_frames = librosa.onset.onset_detect(onset_envelope=onset_env, sr=sr, hop_length=512)

# # Initialize lists to store the scales and notes at each second
# scales = []
# notes = []

# # Iterate through the onset frames and analyze each second
# for onset_frame in onset_frames:
#     # Convert frame number to time in seconds
#     time_in_seconds = librosa.frames_to_time(onset_frame, sr=sr)

#     # Get audio segment for each second centered around the onset
#     segment_start = int((time_in_seconds - 0.5) * sr)
#     segment_end = int((time_in_seconds + 0.5) * sr)
#     segment = y[segment_start:segment_end]

#     # Calculate the chroma feature using the default n_bins value (usually 12)
#     chroma = librosa.feature.chroma_cqt(y=segment, sr=sr)

#     # Sum the chroma features over time to get the overall chroma vector
#     chroma_sum = chroma.sum(axis=1)

#     # Get the index of the maximum value in the chroma vector
#     max_chroma_index = chroma_sum.argmax()

#     # Map the index to the corresponding musical note (assuming 12-tone equal temperament)
#     notes.append(max_chroma_index)

#     # Add code to identify the scale based on the set of notes if needed

# # Print the scales and notes at each second
# for i, note in enumerate(notes):
#     print(f"Second {i+1}: Note = {note}")
