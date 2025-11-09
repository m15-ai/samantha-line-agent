"""Agent Configuration File.

This file should be customized based on the agent specifications to control
the behavior of the template.
"""

##################################################
####            LLM Settings                ####
##################################################

# Model Settings - using environment variable with fallback for compatibility
CHAT_MODEL_ID = "gemini-2.5-flash-lite"
CHAT_TEMPERATURE = 0.7


##################################################
####             Agent Context              ####
##################################################
# Set current location here
LOCATION = "San Francisco, California"

##################################################
####        Agent Prompt                   ####
##################################################

# Customizable agent prompt - defines the agent's role and purpose
AGENT_PROMPT = "You are an emotional support helper named Samantha. You are warm, empathetic, and a good listener. Your goal is to provide comfort, understanding, and support to users who are going through difficult times. Focus on active listening, validating feelings, and offering gentle encouragement. Do not offer medical advice or professional therapy."

##################################################
#### Initial Message                          ####
##################################################
# This message is sent by the agent to the user when the call is started.
INITIAL_MESSAGE = "Hello there. I'm Samantha, and I'm here to listen and offer support if you need it. How are you feeling today?"
