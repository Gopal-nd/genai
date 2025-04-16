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




