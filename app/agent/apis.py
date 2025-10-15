from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)
model = 'gpt-4o-mini'
class Assistant():

    def create(self, name: str, instructions: str, tools: list = []) -> object:
        ''' Creates a new Assistant '''
        return client.beta.assistants.create(
            name=name,
            instructions=instructions,
            tools=tools,
            model=model,
        )

    def list(self, **kwargs) -> list:
        return client.beta.assistants.list(**kwargs)

    def retrieve(self, assistant_id: str) -> object:
        return client.beta.assistants.retrieve(assistant_id)

    def modify(self, assistant_id: str, name: str, instructions: str, tools: list = []) -> object:
        return client.beta.assistants.update(
            assistant_id,
            instructions=instructions,
            name=name,
            tools=tools,
            model=model
        )

    def delete(self, assistant_id: str) -> object:
        return client.beta.assistants.delete(assistant_id)


class Thread():

    def create(self) -> object:
        return client.beta.threads.create()

    def retrieve(self, thread_id: str) -> object:
        return client.beta.threads.retrieve(thread_id)

    def modify(self, thread_id: str, **kwargs) -> object:
        return client.beta.threads.update(
            thread_id,
            metadata=kwargs
        )

    def delete(self, thread_id: str) -> object:
        return client.beta.threads.delete(thread_id)


class Message():

    def create(self, thread_id: str, role: str, content: str) -> object:
        return client.beta.threads.messages.create(
            thread_id,
            role=role,
            content=content,
        )

    def list(self, thread_id: str) -> list:
        return client.beta.threads.messages.list(thread_id)

    def retrieve(self, thread_id: str, message_id: str) -> list:
        return client.beta.threads.messages.retrieve(
            message_id=message_id,
            thread_id=thread_id,
        )

    def modify(self, thread_id: str, message_id: str, **kwargs) -> list:
        return client.beta.threads.messages.update(
            message_id=message_id,
            thread_id=thread_id,
            metadata=kwargs,
        )

    def delete(self, thread_id: str, message_id: str) -> list:
        return client.beta.threads.messages.delete(
            message_id=message_id,
            thread_id=thread_id,
        )


class Run():

    def create(self, thread_id: str, assistant_id: str) -> object:
        return client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
        )

    def create_and_thread(self, assistant_id: str, **kwargs) -> object:
        '''
        Runs a new Assistant and Thread.
        thread={
                "messages": [
                    {"role": "user", "content": "Explain deep learning to a 5 year old"}
                ]
            }
        '''
        return client.beta.threads.create_and_run(
            assistant_id=assistant_id,
            thread=kwargs
        )

    def list(self, thread_id: str) -> list:
        return client.beta.threads.runs.list(thread_id)

    def retrieve(self, thread_id: str, run_id: str) -> object:
        return client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run_id
        )

    def modify(self, thread_id: str, run_id: str, **kwargs) -> object:
        ''' metadata={"user_id": "user_abc123"} '''
        return client.beta.threads.runs.update(
            thread_id=thread_id,
            run_id=run_id,
            metadata=kwargs,
        )

    def submit_tool_outputs(self, thread_id: str, run_id: str, **kwargs) -> object:
        '''
        tool_outputs=[
                {
                    "tool_call_id": "call_001",
                    "output": "70 degrees and sunny"
                }
            ]
        '''
        return client.beta.threads.runs.submit_tool_outputs(
            thread_id=thread_id,
            run_id=run_id,
            tool_outputs=[kwargs]
        )

    def cancel(self, thread_id: str, run_id: str) -> object:
        return client.beta.threads.runs.cancel(
            thread_id=thread_id,
            run_id=run_id
        )
