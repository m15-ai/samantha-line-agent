from chat import ChatNode
from prompts import get_initial_message

from line import Bridge, CallRequest, VoiceAgentApp, VoiceAgentSystem
from line.events import (
    UserStartedSpeaking,
    UserStoppedSpeaking,
    UserTranscriptionReceived,
)

# ---- call handler ----
async def handle_new_call(system: VoiceAgentSystem, _call_request: CallRequest):
    chat_node = ChatNode()
    chat_bridge = Bridge(chat_node)

    # Route audio/speaking through the node
    system.with_speaking_node(chat_node, chat_bridge)

    # Feed transcripts into the node
    chat_bridge.on(UserTranscriptionReceived).map(chat_node.add_event)

    # Stream responses; interrupt if the user starts talking again
    (
        chat_bridge.on(UserStoppedSpeaking)
        .interrupt_on(UserStartedSpeaking, handler=chat_node.on_interrupt_generate)
        .stream(chat_node.generate)
        .broadcast()
    )

    # Start the voice system and optionally send the first message
    await system.start()
    init_msg = get_initial_message()
    if init_msg:
        await system.send_initial_message(init_msg)
    await system.wait_for_shutdown()

# ---- app ----
app = VoiceAgentApp(handle_new_call)

# Cartesia builder wants an explicit entrypoint
if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "8000")))
