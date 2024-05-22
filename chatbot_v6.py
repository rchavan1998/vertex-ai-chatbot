import streamlit as st
import vertexai
from vertexai.generative_models import GenerativeModel, ChatSession
import vertexai.preview.generative_models as generative_models


# Init
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
  st.title("Miracle Software Systems Chatbot")
  st.caption("Implantation for Streamlit chatbot using Vertex AI")

  # new chat
  if st.button("Start New Chat"):
    st.session_state["chat_session"] = ChatSession(model=model)
    st.session_state["chat_history"] = [{"role": "assistant", "content": "Ask our Miracle bot anything. except the current time !"}] 
    # st.session_state["welcome_shown"] = False

  # Init session state if no ongoing chat
  if "chat_session" not in st.session_state:
    st.session_state["chat_session"] = ChatSession(model=model)
    st.session_state["chat_history"] = [{"role": "assistant", "content": "Ask our Miracle bot anything. except the current time !"}]  
  chat_session = st.session_state["chat_session"]
  chat_history = st.session_state["chat_history"]

  # welcome
#   if not st.session_state.get("welcome_shown", False):
#     st.chat_message("assistant").write(
#       "Ask our Miracle bot anything. Except the current time! Start talking to the bot now ... "
#     )
#     st.session_state["welcome_shown"] = True

  # Chat loop
  if prompt := st.chat_input():
    st.session_state["chat_history"].append({"role": "user", "content": prompt})
    response = chat_session.send_message(
      content=prompt,
      generation_config={"max_output_tokens": 8192},
      safety_settings=safety_settings,
    )
    st.session_state["chat_history"].append({"role": "assistant", "content": response.text})

  # print chat
  for message in chat_history:
    with st.chat_message(message["role"]):
      st.markdown(message["content"])


if __name__ == "__main__":
  main()