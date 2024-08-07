# Diagrammatic representation of data

"""
    Data
    |- train-clean-100
    |    -> mfcc(28539,)
    |    -> transcript(28539,)
    |
    |- dev-clean
    |    -> mfcc(2703,)
    |    -> transcript(2703,)
    |
    |- test-clean
    |    -> mfcc(2620,)

    INTERPRETATION:

        Structure
            Root Directory:
                - `Data`

            subdirectories
                - `train-clean-100: training set`
                - `dev-clean: validation set`
                - `test-clean: test set`

            contents of each subdirectory
                training-clean-100
                    - mfcc(28539,): contains 28,539 MFCC feature files.
                    - transcipt(28539,): contains 2,703 transcript files.

"""


