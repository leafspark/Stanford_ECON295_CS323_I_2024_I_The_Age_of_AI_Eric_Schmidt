import pysrt

srt_files = ['chunk1.wav.srt', 'chunk2.wav.srt', 'chunk3.1.wav.srt', 'chunk3.2.wav.srt', 'chunk4.1.wav.srt', 'chunk4.2.wav.srt', 'chunk5.1.wav.srt', 'chunk5.2.wav.srt', 'chunk6.1.wav.srt', 'chunk6.21.wav.srt', 'chunk6.221.wav.srt', 'chunk6.222.wav.srt']
subs = pysrt.SubRipFile()

last_end_time = 0
for srt_file in srt_files:
    srt = pysrt.open(srt_file)
    if last_end_time > 0:
        srt.shift(seconds=last_end_time)
    subs.extend(srt)
    last_end_time = subs[-1].end.ordinal / 1000.0

subs.save('merged_output.srt')
