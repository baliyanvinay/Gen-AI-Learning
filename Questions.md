# Questions & Answers
### What are tensors in AI/Maths?
A tensor is just a container that holds numbers in different shapes—like a single number, a list, a grid, or even a stack of grids.<br>
Tensors are a mathematical concept that has been around for over a century. They come from fields like:
- Linear Algebra
- Multilinear Algebra
- Differential Geometry
- Physics (especially in Einstein’s theory of general relativity)

#### 🌡️ Tensor Analogy: Temperature in a City
| Tensor Type   | Rank | Real-World Example                                                                 | Description                          |
|---------------|------|-------------------------------------------------------------------------------------|--------------------------------------|
| Scalar        | 0    | Temperature at one location at one time → `32°C at Powai at 2 PM`                  | Just one number                      |
| Vector        | 1    | Temperatures at multiple locations at the same time → `[32, 30, 33]`               | A list of numbers                    |
| Matrix        | 2    | Temperatures at multiple locations over multiple times                             | A grid of numbers (rows × columns)  |
| 3D Tensor     | 3    | Temperatures across cities, locations, and times                                   | A stack of matrices (cube)          |
| 4D Tensor     | 4    | Temperatures across cities, locations, times, and days                             | A shelf of cubes (multi-day data)   |

#### Example use in AI 
- 1D Tensor (Vector): A simple list of values (e.g., features or word embeddings)
- 2D Tensor (Matrix): Rows and columns (e.g., tabular data or model weights)
- 3D Tensor: Used in NLP for sequences of word embeddings
- 4D Tensor: Used in computer vision for batches of images
- 5D Tensor: Used in video processing or 3D medical imaging
----
### What are vectors?
A vector is a list of numbers that represent a position in a space and a direction and magnitute. <br>
The magnitude of the vector is the distance between the two points, and the direction refers to the direction of displacement from A to B. <br>
A vector is what is needed to "carry" the point A to the point B; the Latin word vector means 'carrier'.<br>
In other words, a magnitude of a vector is the scaler from a origin, if plotted. 

#### Example of a 2D Vector in X/Y plain
<p align="left">
  <img src="https://github.com/user-attachments/assets/cfeb979c-fd94-4e29-9188-f87ceaa64959" width="400" height="300"/>
</p>

### How vectors are used in AI?
Vectors can be used to represent information in AI/ML. <br>
- For example, a customer might be represented as [age, income, spending_score] = [25, 50000, 80].
- Words, sentences, and even entire documents are converted into dense vectors called embeddings.
- These vectors capture semantic meaning and can be used to find similar items using cosine similarity or Euclidean distance.

Let's take an example of customers representing age, income (in 1000), spending_score.
With customers A, B, C and D with vectors as [25, 50, 80], [30, 60, 70], [22, 45, 85] and D[40, 90, 30] respectively. 
<p align="left">
  <img src="https://github.com/user-attachments/assets/fd295f8d-0897-4ec5-85ac-6fee53b51f45" width="400" height="300"/>
</p>
<em>From the heat map with vectors similarity score, we can see the similarity among customers.</em>

---
### Why transformers/models run better on GPUs and not on CPUs?
- Transformers are a type of deep learning model that process large amounts of data using matrix operations—especially multiplication and addition of large arrays of numbers. These operations are repeated millions (or billions) of times during training and inference.
- #### 🖥️ CPUs vs. GPUs: What's the Difference?
| Feature | CPU (Central Processing Unit)	| GPU (Graphics Processing Unit) |
| ----------- | ------------------------- | ------------------------------ | 
| Core Count  |	Few powerful cores (usually 4–16) |	Thousands of smaller cores |
| Parallelism |	Good at sequential tasks | Excellent at parallel tasks |
| Optimized | For	General-purpose computing |	High-throughput computations |
| Speed for AI |	Slower for large models	| Much faster for matrix-heavy tasks |

---
#### 🚀 Why GPUs Are Better for Transformers
- Parallel Processing: GPUs can perform thousands of operations at once. Transformers need to process huge matrices, and GPUs can do this in parallel, making them much faster.
- Memory Bandwidth: GPUs have higher memory bandwidth, which means they can move data around faster—critical for large models.
- Specialized Hardware: Modern GPUs (like NVIDIA's) have Tensor Cores, which are specifically designed for deep learning tasks.

### What does the parameters mean for a LLM?

---
###  What is a dimension in an embedding model?
Dimension refers to one of the numerial components in a vector that represents a data point. <br>
In a 4D vector, [0.12, -0.45, 0.88, 0.33], each number represents a dimension. Each dimension captures some latent feature of the data such as gender, tense, formality and etc. However, these features are not explicitly labeled — they are learned automatically by the model during training.

---
### What is vector embedding?
A vector embedding is a way of representing data, especially complex or non-numeric data like words, images, or documents as a list (or vector) of numbers in a continuous, high-dimensional space. These embeddings are designed so that similar items are close together in this space, and dissimilar items are far apart.

---
### What is red teaming in AI?

---
### What is few shots prompting?
Few-shot prompting is a technique used in Generative AI (especially in models like GPT) to guide the model's behavior by giving it a few examples of the task you want it to perform. <br>
```Answer the question, 88 is 44, 66 is 33, so 222 is?```
In the above example, prompt helps the model understand context or format.

---
### What is chain of thoughts in prompting?
Chain of Thought (CoT) prompting is a technique where you ask the AI to explain its reasoning step by step before giving the final answer. <br>
```Take step by step approach and solve this question for me, x+7 = 10```

---
### What is tool-augmented prompting?
Tool-augmented prompting is a technique where a Generative AI model uses external tools or systems to enhance its capabilities during a task. Instead of relying only on its internal knowledge, the model can call tools to get more accurate, updated, or specialized results.

---
### How do you deploy a large model efficiently on low resource environments?

