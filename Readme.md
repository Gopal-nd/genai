# GenAI

gen ai

trryst

[Google Paper](https://arxiv.org/pdf/1706.03762)


## openAI
GPT = (Geneative Pretrained Transformer)   works on tarained data
chatGPT =  (GPT + aiAgent) aiAgent will give the current details to gpt
 
## how an llm works

it works on the transformer (google paper)

1. Phase 1

convert the text -> tokens 

[tokenizer](https://tiktokenizer.com)

vector Embeddings => they will give  the Symentic Meaning

vector embedding will make the 3d graph and place the different words in the x,y,z positions


[vector visualizer view](https://projector.tensorflow.org/)

Positionl Encoding

text = "people set on chair"
text = "chair set on people" 

there is difference in the both text

this to get the position of tokens

self evoluation
tokens talk to each other to adjust

(one head and multi head)

here there will be chance to change the vector embeding to make proper symentic meaning


next is it will be send the neural network




## woking phases

1. training phase

in taraing ai  will give the output and the loss calculated and used to train in backend
 eg. asking 2+2 if u give wrong ans , it will hint of answer 


2. inferencing phase

the linear will give the heigest probility (temperature)

### Assignments / Home work

1. create your own tokanizer
2. write a article on explaing all the garganse 


## Day 2 

### GIGO 
Garbage input Garbage Out

if we give garbage input we get the garbage output

it is called as prompt engineering

if we write the  AI prompt  our self Output -> excellent
but, if we let the AI Prompt to written by AI then the Output => very bad

e.g. write a function to add two numbers function in c

but if u give the prompt to give


#### prompt types / styles

1. alpace prompt 
2. Inst Format (llama2)  
    wrapping strings <s> steps to make a coffee </s>
3. ChatML 
    {role:"system",content:"you are an assistant", role:'user', content:'what is lru cache?'}

openAI api call example   |    zero short prompting
gemini api call           |


#### prompt methods

1. zero short prompting -> talking directly 

2. system prompt and user prompt -> giving inital prompt

3. few short (with few example) -> same as system prompt but giving the context and the example and giving the examples
system = """
example:
input: 2+2
output :2+2 is 4 which is calculated by adding the 2 with 2

input: 3*10
output: 3 * 10 is 30 which is calculated by multi the 3 with 10

input: why the sky is blue
output: sorry i can only assistent with the maths?

"""


getting better and better on  conversation again and again


just like deepseek working below
4. thought chaining ->
system_prompt = """
you are an ai assistent with the experties in breaking down the problem and then resolve the user query 

for the given input , analyze the input and break down the problem step by step atleast  think 5-6steps , on how to solve the problem

"""

now make make a api call for all the modle and send the pick the best and make the chain of thoughts of all of them

5. self-consistency prompting (HW)

get the multiple reponse and pick the common response among all of them
e.g whta is greator? 9.8 or 9.11

6. persona-based prompting(HW)
you are hitesh sir
    tone,hinglish , examples, say on the start up if course asked give the affeliate link, 

7. role-playing prompting (HW)
you are an ai codding assistant who is expert in teaching how to code

Cot + persona + Role

**contextual prompting
multimodle prompting **

need coding 

multi agent orch

#### cost calculation

input - 1M tokens  $2.50
cached input - 1M tokens $1.20
output - 1M tokens  $10



virtual interview
tech support 
virtual girl friend

how can i train the model on data e.g. 10tb data


## day 3

giving the super power to llms

llms -> brian
tools -> body

example weather agent, stocks, news

Next word prediction model

[Next Word](https://colab.research.google.com/drive/1DMbV9Qnw0ni_CfBgogAAPrda6aD7hHP5?usp=sharing)



### Day4 Fine Tuning

1. get the token from hugging face
2. select the model 
3. fine ture it with data
4. push the model to hugging face

#### Methods of fine tuning

1. full parameter fine tune
2. LoRA 


## 5 day

RAG Application (Retreval Agrumented Generation)

an ai teachnique that combain the power of information retrival with large lanuguage model (llms) to enhance the accureacy and context-awerness of ai generateed response , it works by first searching for the relevent data(web , documents, database) and feed the context to the llm to get the accuret result


------------------ Basic Rag

1. indexing - > break down the content -> make it inito chuks -> store it in database -> qdrantDB

2. retreving -> based on the user query -> we search the semiler chuks -> from the data base

3. generation -> using the chuncks and the user query -> we give that to the llm -> llm will give output

----------------- Advanced Rag
RAG CHAIN 

. Query Transformation/ translation
. Routing
. Query construction
. Indexing
. Retrival
. Generation

## Query Transformation/ translation

more abstarction
|
| {Question} = re-write the query (rag rusion, multi query)
|
|
|
less abstraction

[diagram](https://app.eraser.io/workspace/W1ItJUWco1xYkXrVLsMR)

parallel Query (Fan Out) Retrival
- make the 3-4 queryes  for the {user query}
- then make vector serch -> you will get the chunks
- now filter all the unique chunks
- use them to llm with the chinks and user query


Reseprocate rank Fusion
- same as parllel but we write ranking algo - more no of same chunks

Query Decomposition
- abstract (step back prompting) e.g what is programing
- less abstact (chain of thought) e.g ex. python programing to make the text split at a char
- make differt query for the user query, break down the question in step by step 
- ex. think machine learning

step back prompting white paper

HyDE -> hypothetical document embedding (need the large model)
|
+
user query => based on the user query create documentation for this -> genarte embeding from he documetion -> give that to model + user query



## Routing (langraph)

### logical routing
-- it will redirect to the correct data-source
- it works on the grouping
- name spacing (qdrant collections)
- like seperating the user data and source

e.g:
i have 3 data source
1. python
2. javascript
3. gamining

based on the user query pick the best source

-like school
    - finincial Records
    - employee
    - techical details
    - resurch paper

- create multiple vector database , make the collections in vector database

- parse , user query and rank the collection and search the db

### semantic Routing
- if u know there are only few possibliity 

## Query construction Knowledge Graph (relationships)
take the chunks and store them in the both vector db and graph db

when user ask question -> searcg in vector db ,from the vector db get the entities -> then make the graph serach in graph db then get all connected nodes, (with this context it have context of all things related to other entities)

(to have relational graph)

knowledeg Graph
knowledge -> some thing 
Graph -> relation ship with entities knowledge


making the chunks  and storing in the vector db

now lets make the cunks as node and make relations to each others
## neo4j
- graph database  - cypher Qyery

now we have three ways-> raw, langchain , memory

usecase: ai assistents, medical usecase, question and answer


#### code a auto rabbit
#### resume preprations + voice + video + rattings
#### edutech products
#### TA Hiring

## new libraryes
1. browser use
2. tavilySearch



