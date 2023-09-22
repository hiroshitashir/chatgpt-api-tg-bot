from typing import Tuple

#import torch
#from transformers import BartForConditionalGeneration, AutoTokenizer
#from transformers import pipeline, Conversation

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

class ConversationChatbot:
    # def __init__(self, model_name):
    #     self.model_name = model_name
    #     self.pipeline = pipeline("conversational", model=self.model_name)
    #     self.conversation = None

    # def get_response(self, message_text):
    #     if self.conversation is None:
    #         self.conversation = Conversation(message_text)            
    #     else:
    #         self.conversation.add_user_input(message_text)

    #     self.conversation = self.pipeline(self.conversation, \
    #                                       pad_token_id=self.pipeline.tokenizer.eos_token_id)
    #     return self.conversation.generated_responses[-1]

    def __init__(self, model_name) -> None:
        self.model_name = model_name
        tokenizer, model = self.load_model()

        # Define PAD Token = EOS Token = 50256
        tokenizer.pad_token = tokenizer.eos_token

        self.tokenizer = tokenizer
        self.model = model
        self.chat_history_ids = None

    def load_model(self):
        tokenizer = AutoTokenizer.from_pretrained(self.model_name, padding=True, padding_side="left")
        model = AutoModelForCausalLM.from_pretrained(self.model_name)
        return tokenizer, model

    def get_response(self, message_text):
        #import pdb; pdb.set_trace()
        # encode the new user input, add the eos_token and return a tensor in Pytorch
        new_user_input_ids = self.tokenizer.encode(message_text + self.tokenizer.eos_token, return_tensors='pt')

        # append the new user input tokens to the chat history
        bot_input_ids = torch.cat([self.chat_history_ids, new_user_input_ids], dim=-1) if self.chat_history_ids is not None else new_user_input_ids

        # generated a response while limiting the total chat history to 1000 tokens, 
        self.chat_history_ids = self.model.generate(bot_input_ids, max_length=1000, pad_token_id=self.tokenizer.eos_token_id)

        # pretty print last ouput tokens from bot
        response = self.tokenizer.decode(self.chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
        print("DialoGPT: {}".format(response))
        return response