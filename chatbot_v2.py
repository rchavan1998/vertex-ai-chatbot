import base64
import vertexai
from vertexai.generative_models import GenerativeModel, Part
import vertexai.preview.generative_models as generative_models


def multiturn_generate_content():
  vertexai.init(project="miracleinternproj1", location="us-central1")
  model = GenerativeModel(
    "gemini-1.5-flash-preview-0514",
    system_instruction=[textsi_1]
  )
  chat = model.start_chat()
  print(chat.send_message(
      ["""hi"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))
  print(chat.send_message(
      ["""tELL ME ABOUT MIRACLE"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))
  print(chat.send_message(
      ["""Where is it based ?"""],
      generation_config=generation_config,
      safety_settings=safety_settings
  ))

textsi_1 = """Our company is Miracle Software Systems . We are based out of Novi, Michigan. 

Here is some information about our company:
Who We Are
Incorporated in 1994, we have come a long way from our roots. Growing from the days of MRP to ERP transition and the birth of the Internet, we are now a leader in the IT world, working with the latest technologies to innovate and help businesses across the globe evolve. Headquartered in Novi, Michigan with over 2500 Miraclites across the globe, Miracle is a privately owned, minority-certified firm focussed on helping our customers transform digitally.

Miracle has a proven record of evolving over the past three decades to fulfil our customer’s technology needs and deliver with the highest quality. Our Global Delivery Model, with multiple locations worldwide, allows us to provide our customers with cost-effective, high-quality and innovative solutions and services. We are proud to say that we are serving 42 of today’s Fortune 100 and challenge our team members to be innovative with everything that they do.

The Miracle Way
At Miracle, we believe in an Always-Available, Innovation-First approach that enables us to be a trusted partner for our customers in their transformation journeys. We emphasize on putting our customers and employees first, which is at the core of our success as we continue to go above and beyond with game-changing innovations."""

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

multiturn_generate_content()

