import json
import time
from agent.apis import Thread, Message, Run, Assistant
from django.conf import settings
from agent.models import Agent


class OpenAiAssistant:

    def create_agent(self, name: str, instructions: str, tools: list | None = None, code: str | None = None):
        """
        Creates a new OpenAI Assistant and persists a corresponding Agent record with essential identifiers.
        """
        if tools is None:
            tools = []
        assistant = Assistant().create(name=name, instructions=instructions, tools=tools)
        return Agent.objects.create(
            name=name or getattr(assistant, "name", None),
            code=code or getattr(assistant, "id", None),
            identifiers={
                "assistant_id": getattr(assistant, "id", None),
                "provider": "openai",
            },
            instructions=instructions,
        )

    def run(self, assistant_id: str, content: str):
        thread, run = self.process_content_w_assistant(assistant_id, content)
        self.loop_until_complete_message(thread, run)
        return self.retrieve_message(thread)


    def process_content_w_assistant(self, assistant_id: str, content: str) -> tuple:
        thread = Thread().create()
        Message().create(thread.id, 'user', content)
        return thread, Run().create(thread.id, assistant_id)

    def retrieve_message(self, thread: Thread) -> str:
        messages = Message().list(thread.id)
        return json.loads(messages.data[0].content[0].text.value)

    def loop_until_complete_message(self, thread: Thread, run: Run) -> Run:
        elap = 0
        steps = 2
        while run.status != 'completed':
            print(f'Waiting for thread to finish... {run.thread_id} | Time : {elap}')
            time.sleep(steps)
            elap += steps
            run = Run().retrieve(thread.id, run.id)
            if elap >= settings.OPENAI_RUN_TIME_LIMIT:
                break
        return run

    def retrieve_run(self, thread: Thread, run: Run) -> object:
        return Run().retrieve(thread.id, run.id)