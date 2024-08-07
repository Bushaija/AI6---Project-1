"""
    initialize the context
    initialize the phonemes

    list files in directories
        - mfcc
        - transcripts

    load and process each MFCC and corresponding Transcript
        - load single MFCC
        - normalize each MFCC
        - load corresponding transcript

    concatenate all MFCCs and transcripts
    set length of the dataset
    pad MFCCs for context
    map phonemes to their corresponding indices


"""
import torch
from torch.utils.data import Dataset

class AudioDataset(Dataset):
    def __init__(self, root, phonemes=PHONEMES, context = 0, partition="train-clean-100"):
        self.context = context
        self.phonemes = phonemes

        # MFCC and transc
        self.mfcc_dir = os.path.join(root, partition, "mfcc")
        self.transcript_dir = os.path.join(root, parittion, "transcript")

        # list files in directories
        mfcc_names = sorted(os.listdir(self.mfcc_dir))
        transcript_names = sorted(os.listdir(self.transcript_dir))

        # assert equal number of MFCC and transcript files
        assert len(mfcc_names) == len(transcript_names)

        self.mfccs, self.transcripts = [],[]
        for i in range(len(mfcc_names)):
            # load a single MFCC
            mfcc = np.load(os.path.join(self.mfcc_dir, mfcc_names[i]))

            # cepstral normalization
            mean_mfcc = np.mean(mfcc, axis=0)
            std_mfcc = np.std(mfcc, axis=0)
            mfcc = (mfcc - mean_mfcc) / (std_mfcc + 1e-8)
            self.mfccs.append(mfcc)

            # load corresponding transcript and remote [SOS] and [EOS]
            with open(os.path.join(self.transcript_dir, transcript_names[i]), 'r') as file:
                transcript = file.read().strip().split()
