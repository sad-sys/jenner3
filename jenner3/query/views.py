from django.shortcuts import render,redirect
from django.http import HttpResponse


from django import forms


from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator
import os

from .forms import QueryForm

global x 
x = "IDK"

global state
state = 1

def query(request):
    global state
    global index
    global x
    global response
    if request.method == 'POST':
        if state == 1:
                form = QueryForm(request.POST)
                if form.is_valid():
                    user_query = form.cleaned_data['user_query']
                    
                    print (user_query)

                    os.environ["OPENAI_API_KEY"] = "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"
                    pdf_folder_path = '/Users/sadiqkhawaja/Desktop/Brackets/Jenner/TestFolder/'
                    os.listdir(pdf_folder_path)

                    loaders = [UnstructuredPDFLoader(os.path.join(pdf_folder_path, fn)) for fn in os.listdir(pdf_folder_path)]
                    for fn in os.listdir(pdf_folder_path):
                        name, ext = os.path.splitext(fn)
                        if ext.lower() == ".pdf":
                            loader = UnstructuredPDFLoader(os.path.join(pdf_folder_path, fn))
                            documents = loader.load()
                            index = VectorstoreIndexCreator().from_documents(documents)
                    state = 2
                    return render(request, 'query.html', {'form': form})
        elif state == 2:
                form = QueryForm(request.POST)
                if form.is_valid():
                    user_query = form.cleaned_data['user_query']
                    print (user_query)
                    print ("Bottom")
                    print(x)
                    x = index.query_with_sources(user_query)

                    response = x  # Example response
                return render(request, 'query.html', {'form': form, 'response': response})

    else:
        form = QueryForm()
        return render(request, 'query.html', {'form': form})
                