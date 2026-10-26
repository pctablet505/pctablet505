**I make machine-learning models fit, and run fast, on hardware smaller than they were built for. Then I measure what each change actually bought.**

<a href="https://github.com/pctablet505/glm53-flash-single-gpu">
<img src="https://raw.githubusercontent.com/pctablet505/glm53-flash-single-gpu/main/assets/throughput-progression.svg" width="100%" alt="Bar chart of decode speed in tokens per second after each change: 8.7, then 10.77 (the baseline), 11.77, 13.53 with a gather kernel, and 16.50 with the most-used experts kept on the GPU. A 20.48 setup with router pruning was not shipped because it degraded the output.">
</a>

**GLM-5.3-Flash: a model nearly twice the size of the GPU's memory, made 39% faster.** Most of its weights sit in 288 experts per layer, and each token uses only 8, so most of the model can live in system memory. Plain offloading then ran it at 10.8 tokens a second, waiting on expert reads. I wrote a gather kernel that reads experts in wide blocks (13.5). Then I moved more of the model off the GPU and used the freed memory to cache the experts the router picks most: 35% of them get 74% of the picks. That reached 16.5 at peak and 15.0 as shipped. Staging experts in groups took long-prompt reading from 614 to about 1,750 tokens a second. One of the eight bugs on the way gave no error at all. **[How it works, and that bug →](https://github.com/pctablet505/glm53-flash-single-gpu)**

**Open source: [100 merged pull requests in 38 projects](https://github.com/search?q=is%3Apr+author%3Apctablet505+is%3Amerged+-user%3Apctablet505&type=pullrequests) I don't maintain** (counted 26 October 2026). Most are in Keras and KerasHub. There I built the export path from a trained model to a LiteRT file a phone can run, and extended it to PyTorch-trained models. Others are fixes in pip, pydantic, pyright, typeshed, poetry and pytest plugins.

**[Porchlamp](https://porchlamp.org/): which open-source projects answer a stranger's pull request?** It follows over a million pull requests to 11,000 projects and judges the 4,000+ with enough of them. Stars barely predict the answer.

**[RL Alpha Labs](https://rlalphalabs.com/): trading research judged after real costs and tax, not by its best backtest.** The ideas that failed are published with their reasons.

**Earlier, on phones, all closed source:**
- models made 3x faster on a phone's NPU and DSP, and quantization-aware training that cut memory bandwidth by 75%;
- a damaged-barcode reader taken from 70% to 90% accuracy with over 10 million synthetic images;
- a phone-drop detector cut from millions of parameters to under 20, at 95% less power.

Job history and the longer story: **[pctablet505.github.io](https://pctablet505.github.io/)**
