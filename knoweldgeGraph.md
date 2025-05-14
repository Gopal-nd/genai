# knowledge Graph - Introduction

### Basic Rag
1. Intexing
2. Retrival

let's take an example of the PDF file 
index the chunks of pdf and store in the vector db

then on retreval make the **serch** and find the relevent chunks

then feed the conyext to the AI

**It WIll Make only (Similarity Search)**

### knowlede graph (entities relationships)

node and edges -> with the relationships

#### knowlede graph (non liner )
1. Construction
2. Retrival

first get the pin point node and get the relevent nodes
storing the relatiosn in the vector db


#### process
1. starting point -> first  make the vector db search and get the relevent chunks and also the relations in the graph db

2. graph search -> use the enties to start the graph search we can generate the relations to the query

3. output -> give the cunks and the relations to the llm

---

know we have the both Both vector db and graph DB

all the (memory will saved in the Graph DB)
store the user queryes and chat in the simple graph , and then save in the Graph DB -> the add the context


### neo4j

It will work using cyper queryes
it will have the label and properties

CREATE (n:Student{name:'Gopal'}) RETURN n

MATCH (n:Student) RETURN n LIMIT 25

MATCH (n) RETURN n LIMIT 25

### implementation [graph](https://js.langchain.com/v0.1/docs/modules/data_connection/experimental/graph_databases/neo4j/)

[inpython](https://python.langchain.com/docs/integrations/graphs/neo4j_cypher/)

[graph constructions](https://python.langchain.com/docs/how_to/graph_constructing/)


## mem 0

keep the history pas 10 messages and the old will be the knowledge graph 
if new messahe came , rmove last one and add to the knowledge graph

like push in to queue when excread the 10 add the knowladeg graph to thaat and pass the context

##
sesameAllLabs









