#using streamlit chatbot functions

import streamlit as st
import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models



# init
vertexai.init(project="miracleinternproj1", location="us-central1")


# Safety settings
safety_settings = {
  generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
  generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
  generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
  generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

# Init model
model = GenerativeModel(
    "gemini-1.5-flash-preview-0514",
    system_instruction=["""Our company is Miracle Software Systems. We are based out of Novi, Michigan. 
        Here is some information about our company:
        Who We Are
        Incorporated in 1994, we have come a long way from our roots. 
        Growing from the days of MRP to ERP transition and the birth of the Internet, we are now a leader in the IT world, working with the latest technologies to innovate and help businesses across the globe evolve.
        Headquartered in Novi, Michigan with over 2500 Miraclites across the globe, Miracle is a privately owned, minority-certified firm focussed on helping our customers transform digitally."""]
)



def main():
  st.title(" Chatbot")
  st.caption(" A Streamlit chatbot powered by Vertex AI")

  # init sess state
  if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

  # chat
  for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

  # input
  if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    # vertex ai call 
    response = model.start_chat().send_message(
        [prompt],
        generation_config={"max_output_tokens": 8192},  # Adjust max tokens as needed
        safety_settings=safety_settings
    )

    #store history
    st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    #print output
    st.chat_message("assistant").write(response.text)

if __name__ == "__main__":
  main()