PHONEMES = [
            '[SIL]',   'AA',    'AE',    'AH',    'AO',    'AW',    'AY',
            'B',     'CH',    'D',     'DH',    'EH',    'ER',    'EY',
            'F',     'G',     'HH',    'IH',    'IY',    'JH',    'K',
            'L',     'M',     'N',     'NG',    'OW',    'OY',    'P',
            'R',     'S',     'SH',    'T',     'TH',    'UH',    'UW',
            'V',     'W',     'Y',     'Z',     'ZH',    '[SOS]', '[EOS]']


"""
    INTERPRETATION:

        - This is a list of phonetic symbols used to represent different sounds
        in speech data.

        1. contents:
            contains phonemes in English
                - vowels: `AA` `AE` `AH` etc
                - consonants: `B` `CH` `D` etc

        2. purpose:
            This list is used for labeling and processing speech data
            mapping audio frames --> specific phonetic symbols during spe. recog. task

        3. specificial tokens
            - [SIL] --> represent silence
            - [SOS] --> marks the start of a sequence
            - [EOS] --> marks the end of a sequence

        Intuition:
            when processing speech data, each frame of audio can be labeled with one of
            these phonemes, enabling the model to learn the mapping from audio features to
            phonetic symbols
"""

