from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import GPT4AllEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

# Set the directory for the Vector Database and load document using PyPDFLoader
vdb_dir = 'vdb'
loader = PyPDFLoader('Literature Review.pdf')
documents = loader.load()

# Initialize a text splitter with specified chunk size and split document into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
print("Save to database %s." % vdb_dir)

# Create Chroma vector store using GPT4AllEmbeddings
vectordb  = Chroma.from_documents(documents=texts, embedding=GPT4AllEmbeddings(), persist_directory=vdb_dir)
vectordb.persist()
print("Done")