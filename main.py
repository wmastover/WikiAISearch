from queryGPT import queryGPT
from queryGPT import getTopic
from wikiAPIs import query_wikipedia
from wikiAPIs import get_wikipedia_page_details
from vectorise import vectorise_text
from vectorise import find_relevant_text


question = input("whats your question?")

topic = getTopic(question)

wikiPage  = query_wikipedia(topic)

content, wikiLink  = get_wikipedia_page_details(wikiPage)

vectors, sentances = vectorise_text(content)

BestParagraph = find_relevant_text(question, vectors, sentances)

print(BestParagraph)

print(queryGPT(f"question: {question} \n\n\n document: {BestParagraph}"))
print(wikiLink)
