%%writefile config.yaml

dataset: 'train-clean-100'
mfcc_features: 28
vocab_size: 42

 # Set your context
context: 0
activations: "GELU"

learning_rate: 0.002
dropout: [0.4]
cepstral_normalization: True
optimizers: "AdamW"
scheduler: "ReduceLROnPlateau"

epochs: 40
batch_size: 4200

weight_decay: 0
loss: "CrossEntropyLoss"

weight_initialization: "kaiming_uniform"

"""
    1. dataset: 'train-clean-100'
    purpose:
        specifies the name of the dataset being used
        dataset name may include subsets or portions such as `train-clean-100-25%`

    2. mfcc_feature: 28
    purpose:
        indicates the number of MFCC(Mel-Frequency Cepstral Coefficient) features
        to be used. This value is typically the number of features

    3. vocab_size: 42
    purpose:
        the size of vocabulary, which corresponds to the number of unique phonemes
        or tokens(including special tokens) in the dataset.

    4. context
    purpose:
        sets the size of context window used in the model.
        a value 0 means not context frames are used around each input frame.

    5. activations: "GELU"
    purpose
        activation function used in neural network.
        GELU stands for Gaussian Error Linear Unit
        GELU weights the input by its probability under Gaussian Distribution

    6. learning_rate: 0.002
    purpose:
        optimization hyperparameters
        controls the step size during gradient descent

    7. dropout: [0.4]
    purpose:
        regularization hyperparameters
        used to prevent overfitting and improve model performance
        dropout --> means ignore some layer outputs during training
        [0.4] --> percentage which specifies the probability of dropiing unit.
              --> means 40% of neurons will be randomly ignored during training.
              --> this prevents the model to rely on some neurons.

    8. cepstral_normalization: True
    purpose:
        technique used to improve robustness of features, such as MFCC
        specifies whether or not to apply normalization.

    9. optimizers: "AdamW"
    purpose:
        specifies the optimizer to be used during training the model
        "AdamW" is a variant of Adam optimizer with weight decay.

    10. scheduler: "ReduceLRonPlateau"
    purpose:
        this is the learning rate scheduler to be used.
        "ReduceLRonPlateau" reduces the learning rate when a
        metric has stopped improving.

    11. batch_size: 4200
    purpose:
        the number of samples per batch used during training.
        large batch size (e.g 32, 64)
            - provides more frequent updates
            - lead to more noise but help the model escape local minima
            - requires less memory

        large batch size(e.g 250, 512)
            - provides more stable and accurate gradient estimates
            - leads to faster convergence but can get stuck in local minima
            - requires more memory
        advice
            - choose moderate batch size
            - adjust learning_rate
            - use learning_rate schedules and Adam(adaptive learning rates)
            - experiment with different batch sizes

    12. weight_decay: 0
    purpose:
        - the weight decay factor applied during optimization to prevent overfitting
        - a value of 0 means no weight decay is applied

    13. loss: "CrossEntropyLoss"
    purpose:
        - specificies the loss function used to train the model
        - "CrossEntropyLoss" is commonly used for classification tasks.

    14. weight_initialization: "kaiming_uniform"
    purpose:
        - method used to initialize the weights of the neural network.
        - "kaiming_uniform" is method that helps to maintain the variance
        throughout the network layers
"""
