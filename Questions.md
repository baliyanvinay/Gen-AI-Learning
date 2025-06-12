# Questions & Answers
### What are tensors in AI/Maths?
Tensors are a mathematical concept that has been around for over a century. They come from fields like:
- Linear Algebra
- Multilinear Algebra
- Differential Geometry
- Physics (especially in Einstein’s theory of general relativity)

### Why transformers/models run better on GPUs and not on CPUs?
- Transformers are a type of deep learning model that process large amounts of data using matrix operations—especially multiplication and addition of large arrays of numbers. These operations are repeated millions (or billions) of times during training and inference.
- #### 🖥️ CPUs vs. GPUs: What's the Difference?
| Feature | CPU (Central Processing Unit)	| GPU (Graphics Processing Unit) |
| ----------- | ------------------------- | ------------------------------ | 
| Core Count  |	Few powerful cores (usually 4–16) |	Thousands of smaller cores |
| Parallelism |	Good at sequential tasks | Excellent at parallel tasks |
| Optimized | For	General-purpose computing |	High-throughput computations |
| Speed for AI |	Slower for large models	| Much faster for matrix-heavy tasks |

#### 🚀 Why GPUs Are Better for Transformers
- Parallel Processing: GPUs can perform thousands of operations at once. Transformers need to process huge matrices, and GPUs can do this in parallel, making them much faster.
- Memory Bandwidth: GPUs have higher memory bandwidth, which means they can move data around faster—critical for large models.
- Specialized Hardware: Modern GPUs (like NVIDIA's) have Tensor Cores, which are specifically designed for deep learning tasks.

### What does the parameters mean for a LLM?
###  What is a dimension in an embedding model?
### What is vector embedding?
### What is red teaming in AI?
