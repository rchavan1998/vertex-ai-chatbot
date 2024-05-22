#session state added

import streamlit as st
import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models

# init
vertexai.init(project="miracleinternproj1", location="us-central1")

# config
generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

# use these variables to moderate content qual
safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}




# init model
model = GenerativeModel(
    "gemini-1.5-flash-preview-0514",
    system_instruction=["""Our company is Miracle Software Systems. We are based out of Novi, Michigan. 
        Here is some information about our company:
        Who We Are
        Incorporated in 1994, we have come a long way from our roots. 
        Growing from the days of MRP to ERP transition and the birth of the Internet, we are now a leader in the IT world, working with the latest technologies to innovate and help businesses across the globe evolve.
        Headquartered in Novi, Michigan with over 2500 Miraclites across the globe, Miracle is a privately owned, minority-certified firm focussed on helping our customers transform digitally."""]
)
# run
# chat = model.start_chat()

def main():
    st.title("Miracle Software Systems Chatbot")
    st.session_state.chat = model.start_chat()

    #session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


    user_input = st.text_input("Ask our Miracle bot anything. except the current time ! ")

    #new chat
    if st.button("New Chat"):
         st.session_state.chat_history = []
         st.session_state.chat = model.start_chat()
    #     chat = model.start_chat()

    if st.button("Send"):
        if user_input:
            # call
            response = st.session_state.chat.send_message(
                [user_input],
                generation_config=generation_config,
                safety_settings=safety_settings
            )

        st.session_state.chat_history.append({"user": user_input, "model": response.text})
        # print(response.text)
        #streamlit response
        #st.write(response.text)
        #chat history display
        for message in st.session_state.chat_history:
            if message:
                st.write("You say : " + message["user"])
            
                st.write("Bot says : " + message["model"])

if __name__ == "__main__":
    main()