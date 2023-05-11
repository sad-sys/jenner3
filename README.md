# jenner3

Web app that uses langchain to read PDFs of lectures and their corresponding transcripts and gives responses.

The first time the tab is open, a GET request is done which processes the pdfs into an index using an openAI embedding. 

The next time a question is asked, a POST request is sent and langchain is used to find the appropiate vectors and then answer questions 
