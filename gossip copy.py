import os
import openai
#https://jman4190.medium.com/how-to-build-a-gpt-3-chatbot-with-python-7b83e55805e6
#https://python.plainenglish.io/create-ai-content-generator-with-python-flask-and-openai-gpt-3-407a19f096b
#https://slacker.ro/2020/08/28/the-ultimate-guide-to-openais-gpt-3-language-model/

openai.api_key = "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"
completion = openai.Completion()

#input prompt
session_prompt = "•\tUsing kind of the supernatural or spookiness as a way of rethinking technologies and then we'll talk a little bit about what you'll do at a class between here and next Tuesday as well.\n•\tSo i'll skip over that we've been through it a few times we just going to start very kind of briefly with a kind of a shared conversation, so I didn't bite each view to kind of open up.\n•\tslack at the table that your ass spend a little bit of time looking through the cases that you've brought in, so I invite you to have a look at find an example of a technology or a thing.\n•\tA creative project that in the world that highlights kind of a perspective that that's missing from the book already like what what isn't in there and why.\n•\tAnd we'll use this as a jumping off point to kind of think about kind of our collective frictions with technology so in groups about kind of your tables.\n•\tJust spend like 10 minutes debriefing on the examples that you brought in, and thinking about the kind of collective frictions with technology that these highlights.\n•\tWhat are the additional kind of things that these are kind of saying about our relationship to technology and what we want to pay attention to.\n•\tAs a group, and we'll use this for our conversation today in terms of what we do with what we've noticed okay.\n•\tSo i'll give you about 10 minutes, just to kind of debrief in small groups you've got whiteboard tables, you want to take notes you've got whiteboard pens in front of you, and a sketch notes and things like that and we'll debrief in about 10 minutes okay.\n•\tWe just a briefing on the example before name so kind of prompted like what are the, what are the friction and he's an example Thailand.\n•\tOur.\n•\tLike.\n•\tGod.\n\n\nCreate gossip about this conversation starting with \"Hey Maggie Mo-ers, Gossip Dan here. And I have the biggest news ever. One of my many sources, Melanie91, sends us this:\" and ending with 2 funny questions and XOXO\n\n\n\nHey Maggie Mo-ers, Gossip Dan here. And I have the biggest news ever. One of my many sources, Melanie91, sends us this:\n\nApparently a bunch of technology experts were sitting around discussing the supernatural and how it can be used to re-think technology. Can you believe it? And they were even talking about how to use it in class!\n\nI have two questions for you:\n\n1. Do you think this is a good idea?\n2. What would you do if your teacher said you had to use the supernatural to re-think technology?\n\nXOXO"

#request
response = openai.Completion.create(
engine="text-davinci-002",
prompt=session_prompt
temperature=1,
max_tokens=224,
top_p=1,
frequency_penalty=0.31,
presence_penalty=0.15
)

print(response)


