import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import numpy as np
from keras.layers import Input, LSTM, Dense
from keras.models import Model

# Define the model
num_encoder_tokens = 100  # Replace with the actual number of encoder tokens
latent_dim = 256  # Replace with the desired latent dimension size
num_decoder_tokens = 200  # Replace with the actual number of decoder tokens

# Example data
encoder_input_data = np.random.random((1000, 50, num_encoder_tokens))
decoder_input_data = np.random.random((1000, 60, num_decoder_tokens))
decoder_target_data = np.random.random((1000, 60, num_decoder_tokens))

# Continue the code with the rest of the model training and architecture

encoder_inputs = Input(shape=(None, num_encoder_tokens))
encoder_lstm = LSTM(latent_dim, return_state=True)
_, state_h, state_c = encoder_lstm(encoder_inputs)
encoder_states = [state_h, state_c]

decoder_inputs = Input(shape=(None, num_decoder_tokens))
decoder_lstm = LSTM(latent_dim, return_sequences=True, return_state=True)
decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)
decoder_dense = Dense(num_decoder_tokens, activation="softmax")
decoder_outputs = decoder_dense(decoder_outputs)

model = Model([encoder_inputs, decoder_inputs], decoder_outputs)

# Train model
batch_size = 32  # Replace with your desired batch size
epochs = 10  # Replace with the desired number of epochs
model.compile(optimizer="rmsprop", loss="categorical_crossentropy")
model.fit([encoder_input_data, decoder_input_data], decoder_target_data,
          batch_size=batch_size,
          epochs=epochs,
          validation_split=0.2)

# Define the interface model
encoder_model = Model(encoder_inputs, encoder_states)

decoder_state_input_h = Input(shape=(latent_dim,))
decoder_state_input_c = Input(shape=(latent_dim,))
decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]

decoder_outputs, state_h, state_c = decoder_lstm(
    decoder_inputs, initial_state=decoder_states_inputs)
decoder_states = [state_h, state_c]
decoder_outputs = decoder_dense(decoder_outputs)

decoder_model = Model(
    [decoder_inputs] + decoder_states_inputs,
    [decoder_outputs] + decoder_states)

reverse_target_token_index = {}  # Replace with your mapping from indices to tokens
target_token_index = {}  # Replace with your mapping from tokens to indices
max_decoder_seq_length = 100  # Replace with the maximum length of your decoder sequence


# Define a function for responses
def generate_response(input_seq):
    states_value = encoder_model.predict(input_seq)

    target_seq = np.zeros((1, 1, num_decoder_tokens))
    target_seq[0, 0, target_token_index['\t']] = 1.

    stop_condition = False
    response = ''
    while not stop_condition:
        output_tokens, h, c = decoder_model.predict(
            [target_seq] + states_value)

        sample_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_token = reverse_target_token_index[sample_token_index]
        sampled_token = reverse_target_token_index[sample_token_index]
        response += sampled_token

        if sampled_token == '\n' or len(response) > max_decoder_seq_length:
            stop_condition = True

        target_seq = np.zeros((1, 1, num_decoder_tokens))
        target_seq[0, 0, sample_token_index] = 1.

        states_value = [h, c]

        return response

class ChatbotGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Chatbot")
        self.geometry("500x600")
        self.resizable(False, False)
        self.initialize_ui()

    def initialize_ui(self):
        self.chat_history = ScrolledText(self, width=50, height=15)
        self.chat_history.config(state="disabled")
        self.chat_history.pack(pady=10)

        self.user_input_label = tk.Label(self, text="User Input").pack(pady=5)
        self.user_input = ttk.Entry(self, width=40)
        self.user_input.pack(pady=5)

        self.submit_button = ttk.Button(self, text="Submit", command=self.submit_user_input)
        self.submit_button.pack(pady=5)

    def submit_user_input(self):
        user_input = self.user_input.get()
        self.user_input.delete(0, 'end')

        self.chat_history.config(state='normal')
        self.chat_history.insert('end', 'User: ' + user_input + '\n')

        input_seq = np.zeros((1, max_decoder_seq_length, num_encoder_tokens), dtype="float32")
        for t, token in enumerate(user_input.split()):
            if token in input_token_index:
                input_seq[0, t, input_token_index[token]] = 1.

        response = generate_response(input_seq)

        self.chat_history.insert("end", "Chatbot: " + response + '\n')
        self.chat_history.config(state="disable")


if __name__ == '__main__':
    input_token_index = {}
    tokens = ['hello', 'hi', 'how', 'are', 'you', 'doing', 'day', 'going', '?']  # Replace with your list of tokens
    target_token_index = {}  # Replace with your mapping from tokens to indices
    target_token_index['\t'] = len(target_token_index)  # Add this line

    for i, token in enumerate(tokens):
        input_token_index[token] = i
        target_token_index[token] = i  # Update target_token_index

    app = ChatbotGUI()
    app.mainloop()